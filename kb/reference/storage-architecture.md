---
description: Authority and lifecycle boundaries among Commonplace's authored files, local source copies, derived artifacts, and operational state
type: types/note.md
tags: []
---

# Storage

This page answers which representation is authoritative and which may be
reconstructed. It does not catalogue the installed directory tree; see
[Commonplace architecture](./architecture.md).

## Storage roles

| Role | Representation | Authority and lifecycle |
|---|---|---|
| Authored KB artifacts | Tracked Markdown | Canonical retained knowledge, contracts, instructions, and decisions; edited and reviewed as source |
| Source reading copies | Ignored files under `.snapshots/` | Reconstructable local materializations; the tracked ingest owns source identity and capture provenance |
| Navigation and publishing views | Generated listings and the static site | Rebuilt from authored artifacts; not a second authority |
| Regenerable reports | Ignored files under `kb/reports/cache/` | Operational views that may be rebuilt from authoritative inputs and current KB state |
| Retained report records | Tracked files under `kb/reports/retained/` | Exact measurements, experiments, or analyses whose record remains useful without becoming a library claim |
| Review results | One file per (note, criterion) pair under `kb/reports/state/review/results/` | The only review and freshness state: judgment text plus the hashes of the inputs it was produced from; machine-local |
| Stateful report packets | One current full-pass packet per note under `kb/reports/state/review/packets/` | Local non-regenerable disposition and resolution state; the pass's run directory keeps its start text |
| Workflow run records | Run directories under `kb/reports/state/review/runs/` | Replay of answered calls within one run; not read across runs and not a format promise |

The role decides whether a missing artifact can be rebuilt; the reports
collection makes that role visible through `cache/`, `state/`, and `retained/`
policy areas. A move between them changes the retention contract rather than
merely organizing files.

## Authored files and version control

Commonplace keeps authored KB content in Markdown under `kb/`; typed artifacts
declare their contracts in YAML frontmatter. The files remain readable and
editable without Commonplace tooling. Their collection and path-valued `type:`
contracts are described in
[collections and types](./collections-and-types.md); the installed surface is
described in [Commonplace architecture](./architecture.md).

Version control is expected for diff review, rollback, attribution, and
reconstruction of change episodes. File visibility and relocation do not
invoke Git ([ADR 039](./adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md)),
and review freshness compares hashes recorded in result files with current
file content rather than repository history
([ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md)).
`commonplace-review` does need a Git working tree: it finds the repository
root and reads `git status` for its checkout guard.
Commits, branches, and merges carry no framework-wide semantic
meaning. Plain-directory and archive installs remain valid. The Commonplace
source checkout is the one exception: there git is the declared change-history
layer, read through instruction-named paths when a decision is revised
([ADR 074](./adr/074-git-is-the-change-history-layer.md)).

## Reconstructable source copies

Captured source content is a local reading copy. Its tracked ingest owns the
external identity, capture metadata, and checksum that says which observation
the copy should reconstruct. A recapture that produces different content does
not silently replace that authority. [ADR 072](./adr/072-ingests-own-source-authority-and-snapshots-are-local.md)
owns this split; the snapshot and ingest skills own its exact file and field
contracts.

Raw captures are neither tracked nor published. The tracked source analyses
that cite them remain ordinary authored artifacts.

### An ingest whose snapshot is on another machine

The checksum travels with the tracked ingest and the snapshot stays where it
was captured. An ingest can therefore arrive on a machine that never held the
pinned bytes. On that machine:

- validation reports the ingest's quotes as unverified, not as failures;
- `commonplace-ingest-handoff prepare` refuses to re-draft the ingest with
  "snapshot not available on this machine";
- `cp-skill-ground` cannot retain new quotes from the source.

Do not recapture to fill the gap. A new capture is a new observation: if its
bytes differ, the pinned checksum names nothing that machine can read. A
snapshot is reconstructable only while its source is unchanged. If the
capturing machine loses the file after the source changed, the pinned bytes
are gone.

The only remedy is to move the exact bytes. The operator's snapshots are kept
in a private repository checked out at `kb/sources/.snapshots/`; it is private
because snapshots are copies of other people's text. A collaborator without
access works in the degraded mode above. A snapshot that a collaborator
captures does not reach that repository unless it is handed over, and no
handover procedure exists yet.

## Derived and stateful local artifacts

Complete directory and tag listings and the ProperDocs site are derived views
over authored Markdown. Agents recover the same navigation facts on demand;
the site generates reader-oriented listings at build time. The exact build and
exclusion rules belong to [documentation site](./documentation-site.md) and
its configuration.

Some generated reports are reconstructable operational views. Connect reports
under `kb/reports/cache/`, for example, may be ignored because their source
artifact and the current KB can replace them
([ADR 007](./adr/007-reports-directory-for-generated-snapshots.md)). Generated
and ignored do not imply disposable: per-pair review result files under
`kb/reports/state/review/results/` hold paid judgments and the hashes that
make them current. Exact report records whose value survives the run live under
`kb/reports/retained/` and are kept with the project.

Full-pass packets are a separate stateful case. A packet owns disposition
and resolution state and records the hashes of the texts it guards; its run
directory keeps the start text. Cleanup must retain the packet while a
pending resolution remains actionable. The packet is still local and
ignored; portability across machines is not promised
([ADR 051](./adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md),
as amended by ADR 127).

## No operational database

Commonplace keeps no database. Review state is the result files and packets
above; each is a file a reader can open, and freshness is a pure function of
them and the current files. [Review architecture](./review-architecture.md)
explains the boundaries.

## Maintenance scope

Review this page when authority or lifecycle moves between these roles: for
example, when a derived view becomes canonical, a regenerable report begins to
own state, or a class of operational state moves out of files.
Directory additions, command names, and build
flags do not by themselves require an edit; their live or focused owners remain
the exact read paths.

## See also

- [Commonplace architecture](./architecture.md) — installed project layout and surface by role
- [Documentation site](./documentation-site.md) — generated publication and listing mechanics
- [Review architecture](./review-architecture.md) — result files, freshness and run state
- [ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) — decided-by: review state as result files instead of a store
