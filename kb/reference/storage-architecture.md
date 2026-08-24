---
description: Authority and lifecycle boundaries among Commonplace's authored files, local source copies, derived artifacts, and operational state
type: kb/types/note.md
tags: []
---

# Storage

This page answers which representation is authoritative and which may be
reconstructed. It does not catalogue the installed directory tree or the
SQLite schema. For those exact surfaces, see [Commonplace architecture](./architecture.md)
and the live [`commonplace.store`](../../src/commonplace/store.py) and
[`store-schema.sql`](../../src/commonplace/store-schema.sql).

## Storage roles

| Role | Representation | Authority and lifecycle |
|---|---|---|
| Authored KB artifacts | Tracked Markdown | Canonical retained knowledge, contracts, instructions, and decisions; edited and reviewed as source |
| Source reading copies | Ignored files under `.snapshots/` | Reconstructable local materializations; the tracked ingest owns source identity and capture provenance |
| Navigation and publishing views | Generated listings and the static site | Rebuilt from authored artifacts; not a second authority |
| Regenerable reports | Ignored local files such as connect reports | Operational views that may be rebuilt from their inputs and current KB state |
| Review evidence | Per-pair review result files | Judgment text not stored in SQLite; retained separately from canonical protocol state |
| Stateful report packets | Full-pass report plus guarded captures | Local non-regenerable disposition state; retained and resolved as one unit |
| Freshness and review state | SQLite operational store | Canonical for accepted input baselines and review execution, not for authored knowledge |

The role, not the file extension or parent directory alone, decides whether a
missing artifact can be rebuilt. `kb/reports/` therefore contains disposable
views, retained evidence, and packets that own actionable state.

## Authored files and version control

Commonplace keeps authored KB content in Markdown under `kb/`; typed artifacts
declare their contracts in YAML frontmatter. The files remain readable and
editable without Commonplace tooling. Their collection and path-valued `type:`
contracts are described in
[collections and types](./collections-and-types.md); the installed surface is
described in [Commonplace architecture](./architecture.md).

Version control is expected for diff review, rollback, attribution, and
reconstruction of change episodes. It is not a correctness dependency.
Commonplace commands do not invoke Git ([ADR 039](./adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md)),
and freshness compares current filesystem content with database-owned snapshots
rather than repository history ([ADR 032](./adr/032-review-freshness-uses-db-snapshots-not-git.md)).
Commits, branches, and merges therefore carry no framework-wide semantic
meaning. Plain-directory and archive installs remain valid.

## Reconstructable source copies

Captured source content is a local reading copy. Its tracked ingest owns the
external identity, capture metadata, and checksum that says which observation
the copy should reconstruct. A recapture that produces different content does
not silently replace that authority. [ADR 072](./adr/072-ingests-own-source-authority-and-snapshots-are-local.md)
owns this split; the snapshot and ingest skills own its exact file and field
contracts.

Raw captures are neither tracked nor published. The tracked source analyses
that cite them remain ordinary authored artifacts.

## Derived and stateful local artifacts

Complete directory and tag listings and the ProperDocs site are derived views
over authored Markdown. Agents recover the same navigation facts on demand;
the site generates reader-oriented listings at build time. The exact build and
exclusion rules belong to [documentation site](./documentation-site.md) and
its configuration.

Some generated reports are reconstructable operational views. Connect reports,
for example, may be ignored because their source artifact and the current KB
can regenerate them ([ADR 007](./adr/007-reports-directory-for-generated-snapshots.md)).
Generated and ignored do not imply disposable: per-pair review result files
retain judgment text that the database does not store. SQLite owns their
protocol and freshness state; the files retain the evidence body.

Full-pass packets are a separate stateful case. A `full-pass-report.md` owns
disposition and resolution state together with immutable start-state captures.
Cleanup must retain and resolve the packet as a unit while that state remains
actionable. The packet is still local and ignored; portability across machines
is not promised ([ADR 051](./adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md)).

## Operational database boundary

The Commonplace SQLite store is canonical for general artifact freshness and
review execution. It retains accepted input snapshots and baselines, plus the
job, pair, and evidence relations needed to execute and finalize reviews.
Review prompts, worker output, manifests, and rendered pair results have the
narrower roles described by [review architecture](./review-architecture.md);
they do not replace store state.

This database is a scoped exception, not a general migration of the KB into
SQLite. Notes, criteria, instructions, tracked source records, and local source
materializations remain file-backed. [Freshness architecture](./freshness-architecture.md)
and [review architecture](./review-architecture.md) explain the cross-component
semantics. The executing store source and SQL resource own exact paths,
environment overrides, migrations, tables, columns, indexes, views, and
integrity checks.

## Maintenance scope

Review this page when authority or lifecycle moves between these roles: for
example, when a derived view becomes canonical, a regenerable report begins to
own state, or another class of operational state moves into the database.
Directory additions, schema objects, store versions, command names, and build
flags do not by themselves require an edit; their live or focused owners remain
the exact read paths.

## See also

- [Commonplace architecture](./architecture.md) — installed project layout and surface by role
- [Documentation site](./documentation-site.md) — generated publication and listing mechanics
- [Freshness architecture](./freshness-architecture.md) — accepted-input state and transitions
- [Review architecture](./review-architecture.md) — canonical review state and artifact roles
- [ADR 052](./adr/052-general-freshness-store-review-first-migration.md) — outcome: the general operational store and first review adapter
