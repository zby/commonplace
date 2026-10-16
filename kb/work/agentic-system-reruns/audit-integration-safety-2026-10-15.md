# Next-61 integration safety after namespace migration

## Decision and review boundary

**The 55 coordinator-cleared results have a supported serial integration route,
but origin is currently dirty and integration must wait.** For each GitHub result,
the route is its unchanged pinned integration, immediately followed by an
origin-only namespace migration, exact-byte verification, validation and a
separate migration commit. Finish that cycle before the next integration.
The two cleared document captures keep their names and do not need a namespace
move. This is a safety review, not integration authorization or permission to
bypass a pinned guard.

The operator commissioned this bounded review on 2026-10-15 for the resumed
audit/integration task. Parent retains integration and scheduling. This review
writes only this report. It does not reassess the 61 semantic audits, release
holds, acquire sources, inspect/advance/recover runs, copy publications, change
Git state or edit frozen worktrees. Batch 18 is actively operator-run: no batch
18 worktrees or jobs were inspected or touched. Older documents saying it has
not launched are not live scheduling evidence.

## Evidence and current namespace eligibility

The governing inputs are the [next-61 commission](./audit-next-61-commission.md),
[reviewed inventory](./next-publication-audit-inventory.md),
[operational holds](./audit-next-61-operational-holds.md),
[namespace migration record](./publication-namespace-migration.md), and current
[publication instruction](../../agentic-system-analyses/instructions/publish-analysis.md).
The workshop and root contracts were read. The inventory was read completely,
including all 61 exact-run records.

Read-only checks at origin commit
`300954cbcaf9afb4a1c44aba12a376f72afa2748`, on `refs/heads/main`, established:

- Exactly **55** inventory rows are coordinator-reviewed with disposition
  `integrate with recorded limits`; six are held. The selected set comprises
  **53 GitHub repositories and two captures**.
- All 70 origin publication identities were read from retained `memory.md`
  frontmatter. None matches a selected identity after case normalization. None
  occupies a selected GitHub canonical destination. The supplied identities
  have ordinary repository URL spelling; this is not an equivalence decision
  about moved repositories or different URLs.
- No selected legacy publication directory is present in origin. No selected
  legacy slug collides with an origin source's project-only slug, including the
  old punctuation-to-hyphen normalization. Thus **no different-owner legacy-name
  collision was found among these 55**.
- Each selected legacy path is absent at its own method commit. For all 55,
  `git diff --no-renames --name-only <method> HEAD -- <legacy-path>` returned
  no changed files. These are namespace/path preflight checks, not a call to
  the integration guard.
- All three method revisions are ancestors of `main`. No
  `analysis/<selected-run-id>` branch exists at this checkpoint.

Selected method distribution:

| Method revision | Cleared results | Implementation sampling |
|---|---:|---|
| `a568c6dc489ad546374536b642c3889ce23149a8` | 46 | Mem0 preparation and integration implementation |
| `8414ddbd35da24645c020789bd824cb9749fa677` | 8 | ai-modules preparation and integration implementation |
| `ff452f2f7cf4b88c40b33747df7b987fb5be2f1f` | 1 | Meta-n; ancestry/path checks only |

Exactly two representative preparations/worktrees were inspected:
`.commonplace/worktrees/ai-modules-a7044d5627d2` and
`.commonplace/worktrees/mem0-5b642a1731b4`, with their adjacent preparation JSON.
Both preparations are ready, name this origin and their own command directories,
and have matching worktree HEADs. Their recorded `origin-dirty: true` describes
preparation time; it does not waive integration's current clean-origin check.
The sampled analysis integration code agrees with the current implementation;
the sampled shared integration functions have the guards described below.
No third pinned implementation/preparation was inspected.

This review did **not** renew all 715 selected member hashes, source pins,
receipts, run completion or every worktree's cleanliness. The inventory retains
the coordinator's earlier 793-file verification across all 61. Execution still
requires fresh per-result checks and the unchanged pinned integration guards.
Meta-n's exact pinned implementation remains an execution-time check, not a
third sample silently assumed certified here.

## Technical findings

### F1. Source identity and old directory names are separate checks

A canonical incumbent means a current publication of the **same source**, not
merely the same repository basename. A different owner's canonical publication
is not permission to replace it, and its existence alone does not prove a path
conflict for a new source.

The implementation at
`src/commonplace/lib/agentic_analysis/worktree.py::_integration_publication`
uses the receipt's old destination. It compares the incumbent at that path in
the method commit and requires its exact archive if one existed. It does not
establish replacement/archive correctness at a newly owner-qualified path.
Therefore **any source-matched canonical incumbent remains on hold**, even if
an old-path integration could otherwise pass. Recheck before each transfer;
this checkpoint's absence is not a reservation.

The separate guard in
`src/commonplace/artifactrun/worktree.py::merge_paths` rejects changed origin
paths since the method commit, with rename detection explicitly disabled. If
`retained/project/` existed in the method for another owner and migration moved
it to `retained/other-owner--project/`, the old-path deletion is an origin change.
An old integration can therefore refuse with
`origin paths changed since the method commit`, although its new canonical
source path has no incumbent. A clean filesystem and a vacant canonical target
do not override that refusal. The old frozen publisher may also have archived
the wrong-owner old-path incumbent; this requires a separately planned transfer,
not acceptance by basename.

No such collision was observed for these 55: their old paths are absent in both
the method trees and current origin. The important rule is **same-source absence
plus unchanged old transfer paths**, not same-source absence alone.

### F2. Integration commits and merges automatically

In the sampled implementations, `prepared_origin` requires origin on clean
`main`, worktree HEAD equal to the preparation's method, unchanged startup
instructions, and method ancestry. `merge_paths` additionally refuses an
existing result branch, staged worktree changes and tracked changes outside the
allowed publication/archive paths. It creates `analysis/<run-id>`, stages those
paths, commits, then executes `git merge --no-ff --no-edit` in origin.

There is **no commit-only pause** for renaming the publication before the merge.
A successful call has already merged the legacy-name result into `main`.
Git's merge is not a source-identity decision or a namespace migration. A merge
conflict is aborted when a merge is in progress, and the result branch is kept.
Other failures can also leave a created branch or commit. Stop and preserve
state; do not retry blindly, copy files, choose a conflict side or alter pins.

The current and sampled `_integration_publication` docstring explicitly says
the effect journal is not read there. The code verifies current outputs,
receipt pins, retained hashes and method-incumbent/archive evidence. Do not
interpret the publication instruction's broader journal language as proof of a
new direct journal audit by this function, or as fresh worker-compliance review.

### F3. Migration is a separate, origin-wide mutation

`scripts/migrate_analysis_publications.py` checks all retained manifests, file
maps, source identities and destinations. Apply precomputes Markdown rewrites,
refuses any required retained-member edits, rechecks input hashes, moves paths,
updates outside backlinks and verifies output hashes. It preserves accepted
bytes and run IDs; it does not commit or integrate anything.

Its dry run returns after planning destinations. **A successful dry run does
not prove apply's later backlink/member-edit preflight will pass.** Apply can
still refuse because moving a publication would require changing accepted
bytes. It can also fail after filesystem mutation; no transactional rollback
is implemented in this script. Preserve partial state and evidence for
separately authorized recovery rather than improvising a repair.

The script has no shared publication-lock context. Exclusive origin mutation
ownership must cover the whole integrate–migrate–verify–commit cycle, not just
the integration command. Its Markdown finder excludes hidden directories and
nested Git repositories (`src/commonplace/lib/project_paths.py`), so origin's
`.commonplace` worktrees are not backlink rewrite targets. External worktrees
are outside origin. This does not authorize interfering with batch 18 or any
non-cooperating origin writer.

## Supported execution sequence for the parent

Intent: transfer only the authorized exact accepted bytes, leave all existing
canonical sources intact, and finish each result at its canonical path with
validated, committed evidence before proceeding. The sequence below is
conditional advice for separately authorized execution; none was run here.

1. **Resolve ownership and obtain a clean origin first.** Coordinate with the
   owners of every uncommitted origin file, including this report. Commit their
   complete artifacts only with authority; do not delete, stash, stage or
   silently absorb someone else's work to satisfy the guard. Confirm clean
   `main` and serialize origin mutation. Batch 18 may continue its independently
   owned worktree jobs; do not stop, inspect, patch or duplicate them. If origin
   mutation ownership cannot be established, wait.
2. Select only a coordinator-cleared exact next-61 row and its audit limits
   (including ai-modules' reviewed supplement). Recheck source identity against
   origin's current canonical corpus, canonical destination absence, old-path
   method/current comparison and any required archive paths. **Hold on a
   source-matched canonical incumbent or any collision/changed-path guard.**
   Confirm the recorded preparation/token/method, code binding and publication
   hash map, and validate with the prepared worktree's validator. Failure stops
   that result; do not patch frozen outputs or invoke recovery.
3. With explicit integration authority, use that row's own command directory
   and cwd, not origin's editable command. The command shape is:
   `<recorded-command-prefix>/commonplace-analysis integrate <exact-run-id> --model <executing-model-id>`.
   Leave all pinned guards intact. Record the returned merge commit, command
   result and exact run/method/source identity. On failure, stop for disposition
   of preserved branch/worktree evidence.
4. For a **GitHub** result, immediately switch operational attention to origin
   (not the frozen worktree). Review
   `uv run python scripts/migrate_analysis_publications.py` there. With no
   concurrent origin writer, expect exactly one move for this result and all
   other sets unchanged. Unexpected moves or a duplicate/destination refusal
   stop the cycle. With separate migration authority, apply using
   `uv run python scripts/migrate_analysis_publications.py --apply --record <new-record-path>`.
   Choose a fresh ledger path and retain the result's before/after commits;
   the helper's ledger does not itself record Git commit IDs. Never reuse the
   original migration ledger or rewrite the frozen worktree's receipts.
5. Compare the canonical result's complete filename/hash map, including
   `ARTIFACT.yaml`, with the commissioned map; check the legacy directory is
   gone. Compare pre-existing publications with their pre-cycle maps to detect
   collateral changes. Validate the origin retained corpus using current
   `commonplace-validate kb/agentic-system-analyses/retained`, plus explicit
   changed Markdown/backlink and ledger checks. Review all failures, warnings
   and notices. Source-unavailable notices do not freshly verify quotations.
   Re-run migration dry run: expect zero moves. Review status and the complete
   diff, including outside backlinks; no repinning or member-byte edits.
6. Commit the **complete migration result separately**: relocation, its full
   backlink edits and new ledger, with explicit file paths and no unrelated
   changes. This preserves the publication integration commit and the migration
   as distinct evidence. Finish any authorized acceptance bookkeeping in its
   own complete artifact commit before the next integration. Require clean
   origin after the cycle; an uncommitted ledger/report/checklist would block
   the next pinned integration.
7. The two cleared captures are
   `AAS-2026-10-14-2603-10600v1-a956324c9a82-01` and
   `AAS-2026-10-15-2608-27454-65116a9d0de7-01`. Their paths stay
   `retained/2603-10600v1/` and `retained/2608-27454/`. Verify exact bytes and
   current origin validation after their integrations; no empty migration
   commit is necessary. Resume only after clean-origin checks.

Do not push, build/publish the site, or expose the intermediate GitHub legacy
result to current-analysis readers between integration and migration. Current
readers reject names inconsistent with source identity. The route necessarily
creates an intermediate `main` commit at the old path. If readers cannot be
excluded during that interval, or policy requires every intermediate `main`
commit to be canonically valid, **this route is not suitable**: request a
separately designed transfer rather than a commit-only flag or guard bypass
that the pinned command does not provide.

## Exact blockers and operator decisions

- **Observed immediate blocker:** origin was dirty. Initial status showed
  untracked `kb/sources/defense-of-not-understanding-your-codebase.ingest.md`;
  a later status also showed untracked
  `kb/work/agentic-system-reruns/audit-integration-current.md`. This report adds
  another untracked file. The parent must coordinate disposition with their
  owners, not treat this review as authority over them. Status is live and
  must be checked again.
- **Authority/coordination:** explicit authority must cover both pinned
  integration and each follow-on migration, including outside backlink edits
  and a fresh ledger. Decide whether a controlled temporary legacy-name
  `main` commit is acceptable and readers can be excluded. If not, stop for a
  separate transfer plan. No other consequential source-selection choice was
  found for these 55 at this checkpoint.
- **Retained exclusions:** keep ModularRSI, JAZ and Supermemory on semantic
  hold; NAMS, LLM-Wiki-v3 and llmwiki-marimo on operational hold under the
  coordinator's dispositions. Preserve the earlier 13 semantic holds and all
  source-matched canonical-incumbent holds. Validator success does not resolve
  ownership, public-qualification or replacement/archive blockers.
- **Execution-time blockers, not observed failures here:** changed bytes or
  inputs, incomplete current coverage, dirty/mismatched worktree, existing
  result branch, changed origin transfer paths, migration preflight/apply
  refusal, validation failures or inability to restore clean origin. Stop at
  the first failed invariant; this report commissions no recovery.

## Verification of this review

Only the owned report was written. All operational probes were read-only Git,
file or inventory checks; no integration, migration command, run-state command,
source acquisition, staging/commit, delegation or batch 18 operation was run.
`commonplace-validate kb/work/agentic-system-reruns/audit-integration-safety-2026-10-15.md`
returned **VALIDATION SUCCESS**: one file analysed, one text file, zero failures
and zero warnings. `git diff --check` passed. This implicit-text report is
operational reasoning, not semantic certification by the validator.
