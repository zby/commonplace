# Public state repository

## Goal

Decide whether the local operational state under `kb/reports/state/` should be
kept in a second, public Git repository, and if so prepare and create it.

The operator opened this workshop on 2026-11-11. It started from a question
about the [decision lifecycle](../decision-lifecycle-evidence/README.md)
workshop: that workshop asks what earns admission to the main record, and
storage size is not what limits admission. A second repository could keep
state durably without admitting it.

## The idea

`kb/reports/state/` is ignored by the main repository. Its contract says the
contents are local but not disposable. Today that material lives on one
machine, with no backup, no history and no second reader.

A separate repository, checked out at `kb/reports/state/` and still ignored by
the main repository, would give state a durable home without these costs of
tracking it in the main repository:

- search noise: a failed candidate looks like an ingest to `rg`;
- implied status: presence in the main record reads as endorsed;
- commit load: every run would dirty the main tree;
- mixing with library history.

It would be a class-level default: keep the material without curating it and
without claiming it is useful. Promotion into the main record stays a separate,
deliberate decision.

The operator wants this repository public so collaborators can participate in
running automated reports, including reviews. The operator also wants to
continue that work when switching computers. Sharing operational state, not
only preserving old runs, is the intended use.

## Settled

- **Snapshots are not part of it.** Being publicly readable does not grant a
  right to redistribute, so snapshots went to a private repository,
  `zby/commonplace-sources`, checked out at `kb/sources/.snapshots/`
  (created 2026-11-11). See
  [storage architecture](../../reference/storage-architecture.md#an-ingest-whose-snapshot-is-on-another-machine)
  for what a machine without it can and cannot do.
- **A plain nested checkout, not a submodule**, is the working assumption. An
  ignored directory stays ignored after `git init` inside it, and the validator
  runs its Git calls from the main repository root.
- **Unify the cache and state directories.** This is the chosen design
  direction, not an executed migration. Record differences in deletion
  consequences and cleanup rules without separate storage classes. The
  destination path and migration plan remain open; public inclusion remains
  subject to checks.

## What the directory holds

Measured on 2026-11-11, before archiving retired review state: 964 MB in
24,099 files.

- About 500 MB is abandoned review data: the retired SQLite stores, their
  backups, and directories the [state README](../../reports/state/README.md)
  already permits deleting. These are not the current review state.
- 231 MB was old agentic-system analysis runs under `agentic-system-analysis/`,
  96 runs of the retired method. 210 MB of it was verbatim source extractions
  that three runs' workers had made into their scratch directories under the
  old rule forbidding reads from the worktree (two PageIndex runs with an
  18 MB example PDF per copy, and a 22-repository arsumbris text bundle).
  Those extractions were deleted on 2026-11-11 and the remaining 21 MB of run
  records moved to the archive; see item 1 below.
- 563 files contain `/home/zby` paths.
- 42 files match an API-key pattern. These may only be analyses that discuss
  key handling in other systems; none has been read.
- 2 files carry snapshot frontmatter and may be copied snapshots. 152 files
  mention a snapshot path without copying one.

## Current implementation and initial policy

[ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md)
replaced the SQLite review and freshness system. Commit `3562ca982` deleted
its code, commands and tests without compatibility or data migration;
`61bdb0802` updated the reference pages. The old files remain only as
abandoned local data. Inspection of `src/`, `pyproject.toml` and `uv.lock`
found no SQLite implementation or declared SQLite dependency. The remaining
`sqlite` value in `systems_matrix.py` classifies external systems.

Current review state is files:

- `review/results/`: one result per (note, criterion) pair, holding the
  judgment and input hashes. Deleting a result makes the pair missing and
  eligible for review again. Preserve these results when pruning.
- `review/packets/`: current full-pass disposition and resolution state.
  Preserve packets needed for unresolved work.
- `review/runs/`: replay records and run artifacts. Freshness does not read
  these, but continuation and packet inspection can need them; do not infer
  that all runs are disposable.

See [review architecture](../../reference/review-architecture.md) for the
current ownership and lifetimes. Result note paths are repository-relative;
criterion identities are repository-relative or installed-library identities.
That does not establish portability of run records or packets.

Start simply, as directed by the operator in this discussion:

- Commit and sync manually, inspecting what will become public.
- Do not combine conflicting reviews. Choose one complete result, keeping
  its judgment and hashes together; accept discarded work or a rerun. Keep
  review updates separate from unrelated changes so they can be reverted.
- Add coordination rules when actual conflicts show the need, rather than
  building a merge mechanism now. The existing
  [isolation analysis](../review-on-workjig/isolation-after-the-store.md)
  records the same decision to defer cross-run coordination.
- Initially prune only the explicitly abandoned data above. Broader cleanup
  must preserve review coverage, unresolved findings and runs needed for
  continuation. Once state is tracked, remove obsolete files through ordinary
  commits. Deleted material remains in Git history; repository growth is
  accepted for now. History pruning, its collaborator coordination procedures
  and pruning automation are deferred.

## Storage direction: unify outputs, document cleanup rules

The operator reports that earlier checks found perhaps one pure cache case;
most outputs currently called cache are not deterministically reproducible.
Those findings need locating and verification before changing the storage
contracts. A report being read once does not establish that it is disposable.

Review results and connect reports both retain model-dependent judgments.
Reviews have freshness machinery that checks whether an existing result still
applies. Connect reports could benefit from such machinery, but defining it
sensibly is deferred. That implementation difference does not by itself
justify separate storage classes.

The chosen direction is one operational-output directory tree, organized by
workflow rather than by cache/state class. Preservation does not imply
endorsement. The destination path and migration plan remain open; this
choice does not authorize migrating paths or publishing the current cache
tree.

Instead of a numeric measure of how cache-like an output is, describe what
its deletion would cost:

- **Reproducibility:** can retained inputs reconstruct the same content?
- **Replacement cost:** how expensive is an adequate replacement, even if it
  is not the same output?
- **Operational dependency:** does freshness, continuation or unresolved work
  rely on this particular output?
- **Historical value:** is the output needed to explain a decision or compare
  runs?

A possible minimal policy vocabulary is:

- **Rebuild:** deletion loses no unique information; reconstruct from retained
  inputs.
- **Rerun:** deletion loses this output, but generating a new one is an
  acceptable replacement when needed.
- **Preserve:** deletion loses something currently needed, such as review
  coverage, unresolved work or decision evidence.

These labels are optional, not a required classification scheme or intrinsic
artifact types. Start with a table in the unified directory's README, with
one row per workflow output stating what deletion loses and its cleanup
rule. No numeric score or new per-file metadata is needed. An individual
output may need an exception when its use changes: a connect report used to
justify a decision is no longer merely an unused suggestion.

Initial rules to verify against consumers before migration:

| Output | What deletion loses | Initial cleanup rule |
|---|---|---|
| Review results | Judgments and review coverage | Preserve current results |
| Review packets | Disposition and unresolved findings | Preserve while work remains unresolved |
| Review runs | Replay and continuation context | Check dependencies before removal |
| Connect reports | Previous suggestions and analysis | Remove only when no ongoing work or decision depends on them |
| Confirmed deterministic cache | Only reconstruction time | Safe to rebuild from available inputs |

A genuinely rebuildable, cheap cache could remain ignored. Connect reports
might permit rerunning when no ongoing work or decision depends on them.
Current review results require preservation because removing them loses
coverage. These examples need checking against actual consumers before
assigning policies.

Open design work: locate the earlier cache audit, inventory consumers and
choose the destination path and migration plan. Start with plain
workflow-specific cleanup rules; add classification only if it improves
actual cleanup decisions. Any unified layout must also preserve the main
repository's ownership of retained reports and navigation. Do not treat
`kb/reports/` wholesale as an ignored nested checkout without resolving that
boundary.

## Before anything is published

Publishing cannot be undone, so each of these comes before the first push.

1. Remove the abandoned review data from the publication tree. Done on the
   operator's direction: 15 top-level entries (716 MB reported by `du`) moved
   to `../commonplace-archive/kb/reports/state/`, preserving their names.
   These comprise the old SQLite databases and backups, `review-store-backups/`,
   `review-jobs/`, `reviews/`, `bundle-reviews/` and `full-pass/`. Current
   `review/` and other workflows' state were left untouched. The earlier
   approximate 500 MB inventory above was not a complete size accounting.
   Later the same day, `agentic-system-analysis/` followed: its source
   extractions were deleted and the 21 MB of run records moved to the same
   archive path. After the x-likes relocation and the pilot archive the live tree is
   3.4 MB in 250 files; 18 files mention `/home/zby` and 9 match the loose key
   pattern, all false positives: 8 tag-placement files with note slugs
   containing `sk-`, and one review launch log with the Claude Code
   `apiKeySource` metadata field (both counts with `rg --no-ignore`,
   which any count over this ignored tree needs).
   Items 2 to 6, the links question and the cross-machine question were
   audited on 2026-11-11 over the remaining tree; results, commands and
   verdicts are in [pre-publication checks](./pre-publication-checks.md).
   In short: no real secret; two review run records carry operational
   absolute paths; `x-likes/` held personal data and third-party posts and
   can never be published, so on 2026-11-11 its state, its rendered cache under
   `kb/reports/cache/x-likes/` and the September literature batch moved to
   `x-likes/` in the private snapshots repository and the script now writes there; the meta-analyser pilot traces copied MIT-licensed
   source without its notice and moved to the archive on 2026-11-11; no copied snapshots remain; the state README
   needs rewriting; this checkout holds no review results, only two revision
   runs, and the 37 results on this machine sit in an agent worktree.
2. Read the 42 key-pattern files. Remove or exclude any real secret.
3. Audit paths consumed by commands for cross-machine use. Distinguish
   operational references from historical path mentions; do not globally
   rewrite logs. Check machine-specific paths beyond `/home/zby`.
4. Check what the analysis runs quote from external repositories and under
   which licences. Exclude what cannot be redistributed.
5. Check the 2 files that look like copied snapshots.
6. Decide what a public reader is told about status: unreviewed model output,
   failed candidates and abandoned runs are in there.

The secret and redistribution checks also apply to later pushes. A clean
initial import does not establish that future workflow output is publishable.
Deleting material after publication does not substitute for these checks;
ordinary deletion commits leave it in Git history.

## Open questions

- **Cross-machine operation.** Verify which files a collaborator needs to
  run reports and reuse existing review results. Continuing an unfinished
  run is a separate portability question; it is not established by copying
  the results.
- **Pairing with the main repository.** A state commit does not say which main
  commit it belongs to. Record the main commit hash, or accept the loss.
- **Sync.** Start with manual commits and pushes. Reconsider automation only
  after the publication boundary and actual collaboration needs are clear.
- **Links.** Library files must not depend on state. Does anything tracked
  link into `kb/reports/state/` today?
- **Cleanup beyond abandoned data.** Establish cleanup rules by payload
  class before deleting live state. This concerns the current tree only;
  Git-history pruning is deferred.
- **Effect on retention choices already made.** The
  [ingest working directory case](../decision-lifecycle-evidence/ingest-working-directory.md)
  ends by deleting run records once one decision is made. A durable state
  repository changes that calculation.
- **The fixed boundary it touches.** The decision-lifecycle workshop says not
  to create duplicate primary process records. State files are not session
  traces, but the boundary should be restated if this goes ahead.

## Scope

This workshop permits design work, the measurements and checks listed above,
and deleting the abandoned review data that the state README already permits.
It does not authorize creating or pushing to a public repository; that needs
the operator's explicit go-ahead after the checks.

Coordinate with [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md),
which owns the retention economics, and
[lineage-mechanisms](../lineage-mechanisms/README.md), which owns general
derived-material retention design.

## Completion

Close when one of these holds:

- the repository exists, the pre-publication checks are recorded as done, and
  the state README and storage architecture describe it; or
- the idea is dropped, with the deciding reason recorded where a later reader
  will look, such as the state README.
