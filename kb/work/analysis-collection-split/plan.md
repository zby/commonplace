# Analysis collection implementation plan

## Commission

Written on 2026-10-03 at the operator's request, for the executor the operator
launches on it. The launch is the authority to implement; this file alone
starts nothing. The two design files authorize nothing by themselves.

It authorizes the profile replay of phase 2. It does not authorize an
analysis run, regeneration of any system, recovery of
a stopped run, or changes to the
[Sol run follow-up plan](../analyse-agentic-system-amendments/sol-run-follow-up-plan.md), which the operator
revises after this work.

## Intent

Analysis workers fail parts of their jobs. The operator's response is to
simplify each job so that an analyst holds only the analysis. This work
builds the structure for that. The operator will then regenerate every
analysis under the simplified method, once.

Two changes serve the intent:

1. **A self-contained analysis collection.** Analysts read a small contract
   that addresses analysis only, supplied to them by path. Publication,
   comparison and method authoring cannot add rules to analyst input later.
2. **A separate profile job.** The memory analyst traces and records. A later
   job classifies the accepted records into the memory comparison profile.

When a choice is not settled below or in the design files, choose what leaves
the analyst jobs with fewer concerns to hold, fewer references to resolve and
fewer instructions to reconcile. Do not buy that by dropping a rule a worker
needs, weakening source grounding, or removing independent review.

## End state

The work is done when all of this holds:

- `kb/agentic-system-analyses/` exists and is self-contained. It owns its
  contract, the analysis method, the member and run-state types, run state,
  `retained/` and `retained-archive/`. A run needs no method file, type or
  contract from another collection.
- Every job packet supplies the collection contract as a `read-first` path,
  and its bytes participate in the job's dependencies.
- No analyst packet contains a rule about publication, comparison writing or
  method authoring, except those listed with a reason in the result record.
- Publication places the accepted set at `retained/<system-slug>/`, moves a
  superseded set unchanged to `retained-archive/<run-id>/`, and writes no
  second review. The list of current analyses is generated at site build.
  Comparison tools and the site build enumerate current sets through one
  function.
- The memory job no longer produces the comparison profile. A profile job and
  a `verify-profile` job produce and check a `memory-profile.md` member after
  record verification closes and before synthesis.
- Workers can apply every registered term their contracts use without opening
  a file the packet does not supply, and the worker rules say so.
- The old `kb/agentic-systems/reports/` tree is byte for byte unchanged and
  excluded from validation and from the comparison population.
- Required tests and validation pass. Two decision records exist. A result
  record states what was done, measured and left.

The first regenerated analysis is the outcome check. It is not part of this
work and needs its own commission.

## Design authority

The design is settled in these files. Read them before acting. Where they and
this plan disagree, this plan governs; report the disagreement.

- [Collection design](./collection-design.md): ownership,
  publication, what moves, the contract's content, registered vocabulary,
  consumers and the Decisions section.
- [Profile job design](./profile-job-design.md): position in the
  run, inputs, output, verification, what existing jobs lose, and the replay.
- [Decision draft](./drafts/decision-draft.md): source for the first
  decision record, with two `TODO` revisit conditions.
- Drafts of [the analysis contract](./drafts/analysis-collection-contract.md),
  [the remaining contract of the old collection](./drafts/agentic-systems-contract.md)
  and [method maintenance](./drafts/method-maintenance.md). These are
  starting points. Revise them freely toward the end state.
- [Complexity measurements](./evidence/complexity-measurements.md): the
  five measures, their counting rules and the baseline per role.

Everything under `evidence/` records how the decisions were reached: the
measurements, the rejected shortening alternative and the earlier reasoning.
It is not design. Use it for baselines and for the decision records' context.
Do not take design from the `analyse-agentic-system-amendments` workshop;
its audits are background on observed failures.

The live code and method are evidence for how things work now. Inspect them
before relying on any path, count or interface named in the workshop files;
those were found by search on 2026-10-03 and may be stale.

## Boundaries

These bind every route.

- **Nothing is migrated.** No retained set, archive or run state moves into
  the new collection. Do not edit, move or delete anything under
  `kb/agentic-systems/reports/`, except adding a validation exclusion.
- **No run crosses the change.** Check for open runs before editing. A run
  opened under the old method finishes there or stays as stopped evidence. It
  is never resumed under the new method.
- **Analytical content is unchanged.** Definitions, record grammar, evidence
  rules, acceptance gates and the profile's axes, values and per-value
  evidence stay as they are. This work moves and separates; it does not
  redefine. The profile job reads accepted records and may read the frozen
  source, but declares no records and adds no evidence.
- **Independent review stays.** Do not remove reconciliation, record
  verification or synthesis verification, and do not fold `verify-profile`
  into code validation.
- **No worker exemption.** Do not tell workers to skip a root rule. The one
  stated deviation is the vocabulary rule, and only after the sufficiency
  check below shows the contracts carry what workers need.
- **Hand-authored reviews stay** in `kb/agentic-systems/reviews/`. A review
  is retired only when its system is regenerated, which is outside this work.
- **Repository rules apply**: explicit staging, relocation-command results
  committed alone, no compatibility shim without a consumer, no
  `commonplace-init` in this checkout, bare `commonplace-*` commands.
- **One owner at a time.** Other sessions edit this repository. Check status
  before each commit and stage only this work's files.

## Priorities and partial results

The two phases are ordered because the profile type and job instructions
should be written once, in the new collection. Phase 1 is useful without
phase 2. Phase 2 is not started on a failing phase 1.

Within phase 1, the order of value is: the collection with its contract
supplied to packets; then publication into stable paths with the generated
list; then the vocabulary sufficiency check; then the `opening` disposition.

If work stops early, leave the repository in a state where required checks
pass and no committed state mixes old and new paths for one consumer. Record
what is complete, what remains, and anything learned that changes the design.
A partial result with that record is acceptable. An unreported gap is not.

A negative finding is a result. If a check below fails, report it with its
evidence; do not adjust the check to pass.

## Supported route

This is one workable route. Take another if it reaches the end state inside
the boundaries, and say what you changed. Steps marked **fixed** have a
binding reason.

### Phase 1: collection, contract and publication

1. **Fixed: inventory before mutation.** Many consumers read these paths and
   type identities: workflow, set, analysis, publication, validation and
   matrix code, tests, scripts, the skill projections, site configuration,
   command and validation reference pages, landscape synthesis, taxonomy
   refresh and the transfer scan. Follow
   [change a contract that several consumers read](../../instructions/change-a-contract-that-several-consumers-read.md)
   and keep the inventory with its dispositions. A missed consumer fails
   silently later.
2. Relocate the analysis method and the member types. **Fixed:** commit the
   relocation command's result alone, so file history survives the rename.
3. Promote the collection contract and supply it in every job packet. Make
   `retained/` under the old tree excluded from validation, and retire the one
   generated review that pins an old set.
4. Change publication to the stable path per system with the archive move,
   and generate the list of current analyses at site build. Write the
   publication instruction; only the coordinator loads it.
5. Vocabulary: for each registered term the supplied contracts use
   technically, check that the contract states what a worker needs to apply
   it. Fill gaps inline in a few lines. Then state in the worker rules that
   the supplied contracts are the binding copy and the linked definition
   notes are background, and list those notes in the maintenance instruction
   as dependencies to recheck.
6. Establish what the boundary job uses from `opening`. Pass only that, or
   reword it as run metadata. Remove the memory job's mention of publication
   checks if nothing analytical depends on it.
7. Re-measure, verify, write the first decision record and the result record.

**Return to the operator after phase 1** with the result record before
starting phase 2.

### Phase 2: profile job

1. Check the design against ADR 083 and ADR 093 clause by clause. Report any
   conflict before building.
2. Draft the profile type, the profile job instruction and the
   `verify-profile` instruction in the new collection.
3. **Fixed: replay before changing the run.** Rebuild the profile for the two
   retained Dynamic Cheatsheet sets from their members with the profile
   removed, and compare axis by axis as the profile job design describes.
   The operator authorized the replay on 2026-10-03 and directed that its
   model jobs run on Luna. It gates the build because a
   classifier that cannot recover the retained profile from records would
   make every regenerated analysis weaker.
4. Add the two jobs to the run, the sixth member to the set, and move the
   profile checks out of the memory, reconcile and record-verification jobs.
   Point the matrix reader and set validation at the new member.
5. Re-measure the memory, reconcile and verify packets and the two new ones.
   Verify, write the second decision record and complete the result record.

### Tests that start model jobs

The replay is the only planned test before regeneration that starts model
jobs. All other checks in this plan are deterministic. Run the replay's
worker jobs on Luna, by the operator's direction, and record the exact model
ID in the result record. If another test that needs model jobs proves
necessary, run it on Luna too and say why it was needed. If Luna cannot be
selected for a worker, stop and ask; do not substitute another model, because
the replay result is compared across the two retained sets and must come from
one model.

Confirm the model from each worker's own session record, not from the
request. The configured Pi worker omits `model` and inherits the dispatching
session's model, and this KB has a recorded case of workers requested as Luna
that ran as another model:
[harness sub-agent model selection regression](../../reference/harness-sub-agent-model-selection-regression.md).

## Left to the executor

Decide these from the code and the intent, and record the choice: file and
function names; the slug function, if the existing run-ID slug is not usable
as it stands; the form of the generated list page; how the validation
exclusion is expressed; test structure; commit granularity beyond the fixed
points; the wording of contracts and instructions; whether a draft is revised
or rewritten; the order of steps that do not depend on each other.

## Return to the operator

Stop and ask, with the evidence and your recommendation, when:

- the end state cannot be reached inside a boundary;
- a consumer needs old and new paths at once, or a compatibility shim;
- the contract cannot stay near 3 KB without omitting a rule a worker needs;
- a registered term cannot be made sufficient inline in a few lines;
- an analyst packet must keep a publication or comparison rule;
- the replay weakens many axes, or shows the records lack facts the profile
  needs;
- the design conflicts with an accepted ADR other than ADR 099;
- the work would change an analytical definition, add a workflow stage beyond
  the two profile jobs, or touch files another session is editing.

Otherwise proceed without asking.

## Verification

- `uv run pytest -q` and `uv run ruff check .` pass.
- Targeted `commonplace-validate` passes for the new collection, the changed
  contracts and instructions, and the redirect map. The old `reports/` tree
  is skipped and unchanged.
- Site boundary tests show that run state is not published and that retained
  members are.
- Publication tests cover a first publication, a replacement with the archive
  move, an interruption on each side of the move, and refusal of two sets of
  one source or a directory whose name does not match its set.
- A test moves a real retained set to an archive path at the same depth and
  confirms its relative links resolve and its hashes are unchanged. The
  design asserts this without having tested it.
- Packet tests show, for every job, the contract supplied by absolute path
  and included in dependencies, also through `scripts/analyst_trial.py`.
- Re-measurement: per analyst role, bytes of mandatory method input and the
  five complexity measures, against the recorded baseline, with the itemized
  list behind each count. If concerns, references or conflicts did not fall
  for analyst roles, say so plainly; that is the claim this work rests on.

A passing fixture shows interface behavior. It does not show that workers
follow the method or that analyses improve.

## Records

- **Result record:** `result.md` in this workshop, written as work proceeds:
  what was implemented, each executor choice with its reason, the consumer
  inventory, measurements, deviations from the supported route, and what
  remains.
- **Decision records:** two ADRs, numbered when written, after implementation.
  The first revises ADR 099 and is built from the decision draft; keep its
  literal `TODO` revisit markers. The second records the profile job. Each
  names its consumption paths and considered alternatives, as the ADR type
  requires.
- **Commits:** follow the repository's commit rules, with the `Workshop:`,
  `Decision:` and `Model:` trailers where they apply.
