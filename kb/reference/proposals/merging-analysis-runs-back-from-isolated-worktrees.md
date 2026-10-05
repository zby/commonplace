---
type: reference/types/design-proposal.md
description: "Proposal: bring a completed analysis run's published set from its isolated worktree into main by a git merge, give runs IDs unique across worktrees, and say when a worktree may be removed"
---

# Merging analysis runs back from isolated worktrees

An `analyse-agentic-system` run executes in its own detached worktree so that
it can pin its method commit. Publication happens inside that worktree. How a
published set then reaches `main`, how a run is cited once several worktrees
exist, and when a worktree may go are not specified. This proposal makes the
operator's chosen direction precise: merge the published set with git, make
run IDs unique, keep raw runs out of git, and record extracted evidence with
the audit that extracts it.

## Current state (as of 2026-10-05)

- **Isolation.** `commonplace-workflow prepare-analysis --name <label>`
  creates a detached worktree at `.commonplace/worktrees/<label>-<12 hex>`
  (the hex is `uuid4().hex[:12]`; `--worktree <path>` replaces the whole
  path). It writes a sibling `<worktree>.preparation.json` record with the
  commit and command prefix (`src/commonplace/lib/analysis_worktree.py`).
  Opening records the worktree `HEAD` as the run's `inputs-commit`.
- **Publication inside the worktree.** Publication checks the incumbent at
  `kb/agentic-system-analyses/retained/<slug>/` against the digest recorded
  at opening. It then moves the incumbent unchanged to
  `retained-archive/<incumbent run ID>/` and writes the accepted set
  (`src/commonplace/lib/agentic_publication.py`). Both directories are
  tracked. The digest guard reads only the worktree's copy, which is the
  method commit's copy. `require_publishable_worktree` admits local changes
  only under `retained/` and `retained-archive/`. Run directories under
  `state/`, frozen checkouts under `related-systems/`, and the worktrees are
  ignored.
- **Transfer back.** The skill says only: "transfer the retained set back
  when the operator authorizes merging the results"
  ([isolated run setup](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup)).
  The one published set on `main`, Dynamic Cheatsheet, entered as commit
  `c59d2b8a4`, whose parent is its method commit `bb3126f84`.
- **Run IDs.** `AnalyseAgenticSystem.run_location` returns the stem
  `AAS-<date>-<slug>`; `Orchestrator.start` appends the first free `-nn` in
  the worktree's own `state/`. Three Dynamic Cheatsheet runs in three
  worktrees each received `AAS-2026-10-04-dynamic-cheatsheet-01`. The first
  is the incumbent on `main`. The third reached publication and was refused
  with "replacement requires a new run ID". Run-ID collisions therefore block
  publication as well as making citation ambiguous. The archive directory
  name is also a run ID, so two archived sets could collide.
- **Consumers of the ID form.** `RUN_ID` in `src/commonplace/lib/agentic_set.py`
  (`AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}`) is used by
  `AnalyseAgenticSystem.repo_root` and `retained_overview_path`. The latter
  parses the slug by dropping one final segment; only tests call it. Every
  member, overview, run-state and generated-review schema under
  `kb/agentic-system-analyses/types/` repeats the pattern. Type prose writes
  the placeholder `AAS-YYYY-MM-DD-system-slug-nn`. `commonplace-workflow
  start --run <dir>` lets a caller name the run directory instead of
  allocating it.
- **Worktree retention.** The skill says "Do not remove the worktree: its run
  state is the evidence of the run." The first Dynamic Cheatsheet worktree no
  longer exists. Under the [reports contract](../../reports/COLLECTION.md),
  the owning workflow decides when its ignored state may be removed. Tracked
  artifacts must not depend on ignored state; they summarize the evidence or
  promote an exact report to `kb/reports/retained/`.
- **Evidence records.** The three reliability audits in
  `kb/work/analysis-collection-split/reliability/` keep `*-evidence.json`
  files. Each names `run`, `worktree`, a method commit and a source revision,
  under inconsistent keys (`method-commit` and `method_commit`). All three
  name the same run ID; only the worktree path tells them apart.

## Problem

A file copy of `retained/<slug>/` from the worktree into `main` would bypass
the only staleness check publication has. If `main` published a newer set for
the slug after the method commit, the copy would overwrite it silently and
archive the wrong incumbent. Without a unique run ID, a published set, an
archive directory and an audit can each name a run that several worktrees
hold. Without a removal rule, worktrees either accumulate indefinitely or are
deleted before their evidence is extracted.

## Design

The four parts below are the candidate selection. Parts 1 and 2 change
behavior-determining organization; parts 3 and 4 change rules for operators
and auditors.

### 1. Run IDs unique across worktrees

**Selected form:** `AAS-<date>-<slug>-<token>-<nn>`, where `<token>` is the
12-hex worktree token and `<nn>` the existing per-worktree counter. Example:
`AAS-2026-10-04-dynamic-cheatsheet-b0dc01a84b3c-01`.

- The token makes IDs from different worktrees, and from other clones,
  distinct with 48 random bits.
- The counter stays because one worktree can hold more than one run: a failed
  run is never resumed, and its replacement may start in the same worktree.
  Keeping it also leaves `Orchestrator.start` unchanged: `run_location`
  returns the stem `AAS-<date>-<slug>-<token>`.
- The token in the ID names the worktree that holds the run directory while
  that worktree exists.
- The existing `RUN_ID` pattern and the schema patterns already match the new
  form, because the token is one `[a-z0-9]+` segment. Legacy IDs on `main`
  and in archives still match.

**Token channel.** Preparation records the token as its own field in the
preparation record, including when `--worktree` overrides the path (it then
generates a token without putting it in the path). `run_location` reads the
record at `<repo root>.preparation.json` and refuses to allocate without a
ready record. Opening also refuses a run whose ID token differs from the
record. That check covers `start --run <dir>`, which bypasses allocation.

Rejected channels: parsing the worktree directory name fails under
`--worktree`; a `--param run-token` relies on the coordinator copying a value
correctly. Rejected forms: a fresh per-run random token loses the
ID-to-worktree lookup; the token without a counter needs a new rule
forbidding a second run per worktree.

Consequences to implement with the form:

- Slug derivation must not parse the ID. `retained_overview_path` either takes
  the slug from the source identity, as publication already does, or is
  removed with its test uses.
- Type prose placeholders and the `repo_root` error message change to the new
  form. Tightening the schema patterns to require the token for new runs is a
  free choice. It would add a second, alternated pattern for legacy IDs,
  which must keep validating because retained and archived sets are frozen.
- Runs that already hold a colliding legacy ID cannot publish under it. The
  blocked Sol run is recovered by marking it failed and starting a new run;
  this proposal adds no ID rewrite for a live run.

**Operativity.** Code consumes the change at `start` and at opening, with
refusal force. Publication's existing "new run ID" and archive-collision
checks then fire only on genuine reuse.

### 2. Merge the published set back with git

After the run is `complete` and the handoff has run, a separate operator
authorization permits integration. Invocation of the skill does not grant it.
Integration has two steps.

1. **Publication commit, in the worktree.** Create branch
   `analysis/<run-id>` at the worktree `HEAD`, which is the method commit.
   Stage exactly the paths publication changed: `retained/<slug>/` and, when
   an incumbent was replaced, `retained-archive/<incumbent run ID>/`. Refuse
   if anything else is staged or if tracked files outside those paths differ
   from `HEAD`. Commit with a message naming the run ID, method commit and
   source revision.
2. **Merge, in the origin checkout on `main`.** Before merging, require the
   method commit to be an ancestor of `main`. Then `git merge analysis/<run-id>`.

Why a merge rather than a copy:

- The merge base is the method commit, so the merge is clean unless `main`
  changed this slug's paths since then.
- The publication commit's parent records which method commit produced the
  result, in history as well as in `inputs-commit`.
- Every stale case conflicts. A newer set on `main` changes the same member
  files: every member carries its `run-id`, and `ARTIFACT.yaml` pins the
  member hashes, so two runs' sets cannot share those bytes. A
  retirement on `main` is a modify/delete conflict. A first set on both sides
  is an add/add conflict. Identical archive moves on both sides merge cleanly,
  which is correct.

**On conflict:** abort the merge, keep the branch and the worktree, and stop
for the operator. The operator chooses a new run at the current method or a
manual resolution under separate authority. No step resolves a conflict by
preferring either side automatically.

**Ancestry precondition.** A run prepared with `--revision` may pin a commit
that `main` does not contain. Merging its branch would bring unmerged method
commits into `main`. The precondition stops that case for the operator.

**Older-method results are accepted.** A set produced under method M0 may
merge into a `main` whose method has moved to M1. The set pins what produced
it: `inputs-commit` records the method commit and `reviewed-boundary` the
source revision. Reproducing the result means checking out those pins, not
the current method. Integration therefore adds no check on method changes
since the method commit.

**The merge runs in the shared origin checkout.** Other sessions commit there
concurrently and may leave uncommitted changes. A merge in a dirty checkout
succeeds when those changes do not touch the merged paths; git refuses it
otherwise. A separate clean integration checkout is not added until this
causes a problem in practice.

**Free choices.**

- Fast-forward or `--no-ff`. Both keep the method commit as the publication
  commit's parent. `--no-ff` adds one integration commit on `main`'s
  first-parent line; the precedent `c59d2b8a4` is linear.
- Delete the branch after a successful merge, or keep it. The merged history
  retains the commit either way.
- Who performs the steps: documented git commands run by the operator or an
  authorized agent, or a command beside `prepare-analysis` that performs step 1
  and its refusals and prints or performs step 2. The staged-path rule and
  the refusals are exact, so a command enforces them more reliably than
  prose.

**Rejected:** copying `retained/<slug>/` into the origin checkout. It
bypasses the staleness check, as stated under Problem.

**Operativity.** The skill's isolated-run-setup text and the publication
instruction consume the rule; their "transfer back" and "stage and commit"
sentences become this procedure. With a command, code enforces it with
refusal force. With prose only, the coordinator or operator follows it with
instruction force. No consumer exists yet.

### 3. Raw runs stay ignored; when a worktree may be removed

Run directories (about 1 MB each), worktrees, `.venv` environments and frozen
checkouts stay ignored local state. Nothing in this design tracks them.

**Selected rule**, replacing "Do not remove the worktree": a worktree and its
preparation record may be removed by the operator, or by an agent the operator
authorizes, when all of these hold.

- Every run in it is terminal: `complete` and merged into `main`, or `failed`.
  A run that is `running`, blocked, stopped or uncertain keeps its worktree,
  because its state is needed to resume or recover.
- No integration branch from it awaits a merge or a conflict decision.
- Every audit that uses the run has extracted its evidence record (part 4),
  or the operator has stated that no audit needs it.

Removal uses `git worktree remove`, then deletes the preparation record and
any merged `analysis/<run-id>` branch. Removal is never automatic. Ignore
status does not license deletion; the rule above does.

What removal loses: job outputs, rejected attempts and workflow records not
copied into an evidence record, and the frozen checkout. The checkout is
recoverable from the recorded source revision. Harness traces live outside
the worktree, so their retention is outside this rule. A run's `run-state.md`
holds the worktree's absolute source path; after removal that path dangles,
which is acceptable because the source revision identifies the source.

### 4. Extracted evidence identifies its run

No new location. Evidence stays with the audit that extracts it: in its
workshop while in flight, and in `kb/reports/retained/<study>-<date>/` once
the workshop closes, as the reports contract already requires. The one new
convention: every evidence record carries `run-id` (the unique form),
`method-commit` and `source-revision`, under those keys. The worktree path
may appear as local context; it is not an identifier. Existing records keep
their legacy IDs and keys; their worktree path and method commit already
distinguish them.

**Operativity.** Auditors consume this convention with instruction force. No
instruction states it yet; the natural home is wherever audit evidence files
are specified, or the analysis collection's method maintenance instruction.

## Adoption criteria

- A run started after adoption carries a token-bearing ID, and `start
  --run` with a mismatched token is refused at opening.
- One end-to-end integration is exercised: a replacing publication merged
  cleanly into `main`, and a second publication for the same slug from an
  older method commit stops with a conflict that leaves `main` unchanged.
- The skill and publication instruction state the integration procedure and
  the removal rule, and the "Do not remove the worktree" sentence is gone.
- Adopting part 4 needs one new evidence record written with the three keys.

---

- [Isolated run setup](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup) — procedure: the current preparation and transfer-back text this proposal would replace
- [Publish an accepted analysis](../../agentic-system-analyses/instructions/publish-analysis.md) — procedure: archive move and replacement committed together
- [ADR 102](../adr/102-separate-the-analysis-collection-and-publish-stable-system-paths.md) — decided-by: stable `retained/<slug>/` paths and `retained-archive/<run-id>/` archives
- [Reports collection](../../reports/COLLECTION.md) — see-also: ignored state ownership and the rule that tracked artifacts carry their own evidence
- [Operative change](../../notes/definitions/operative-change.md) — defined-in: the operativity paths stated for each part
