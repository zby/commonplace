---
description: "Ingest reports own durable primary and implementation-source identity, capture provenance, genre, and exact snapshot checksums; ignored snapshots are local reading copies"
type: ../types/adr.md
tags: []
status: accepted
---

# 072-Ingest reports own source authority and snapshots are local materializations

**Status:** accepted

**Date:** 2026-08-23

## Context

Tracked source snapshots split one source record across two authorities. The
snapshot held the canonical URL, capture provenance, and genre, while the
ingest held the analysis and pointed back through `source_snapshot`. A fresh
checkout therefore carried source bodies but could not identify an ingest
without a repository-relative path. Code-grounded ingests added a second
special representation, `code_revisions`, without saying why those resources
belonged to the primary source.

[ADR 045](./045-source-genre-is-a-single-open-field-on-the-snapshot.md) also
made the snapshot's `genre` authoritative and allowed ingestion to correct that
field in place. That exception conflicted with the source collection's
immutable-capture contract. It became untenable once snapshots moved to an
ignored local cache: a local file that may be absent cannot be durable
authority, and editing any of its bytes changes the checksum of the observation
the ingest used.

The adopted proposal was “Ingest source units and supporting material.” It
established the option space and the primary-versus-supporting distinction. The
implementation workshop then fixed the smallest version that could migrate the
existing corpus without redesigning ingest prose.

## Decision

One tracked ingest report represents exactly one URL-backed primary source. Its
frontmatter owns the canonical `source` URL, `captured` observation time,
`capture` mechanism, flat adapter metadata, primary-source `genre`, and
`snapshot_sha256`. The checksum is lowercase SHA-256 over the exact bytes of
the primary Markdown reading copy, including frontmatter, line endings, and
final-newline state. Capture companions are outside that hash. The removed
`source_snapshot` and `code_revisions` fields are rejected rather than aliased.

An ingest may additionally carry `secondary_sources`. V1 accepts only
`role: implementation`, paired with an immutable GitHub commit URL containing
a full 40-character SHA. Several implementation repositories may support one
primary. The primary still determines the ingest's identity, title,
classification, summary, and source-level limitations. The corresponding
`Code Grounding` prose states what was inspected and which claims remain
primary-source-only; the field alone does not warrant that the repository is
official, faithful, executed, or outcome-reproducing.

Primary Markdown snapshots and capture companions live under ignored
`kb/sources/.snapshots/`. They are local materializations, not tracked
identities or link targets. Resolution is checksum-first: use the sole exact
local match; reject duplicate exact copies; and, when no match exists, attempt
recapture from the ingest's canonical URL. Install and use a recapture only
when its bytes match. A different checksum is an explicit mismatch, and an
adapter failure is explicit unavailability. Neither state rewrites the ingest
or silently substitutes the current source for the historical observation.

A snapshot may retain an optional capture-time `genre` hint so that a local
copy is self-describing. The tracked ingest's value is authoritative and may
differ after closer reading. Ingestion writes that judgment to the ingest and
does not edit the snapshot. This decision supersedes ADR 045's field placement
and mutation exception while retaining its open-vocabulary warning behavior,
fixed value meanings, removal of `source_type`, and return of snapshot `tags`
to optional topical use.

The migration applied these rules to 275 existing ingest units. A 942-row
recovery ledger completed 275 unit transformations, 338 local-asset
dispositions, and 329 durable-library link dispositions. It retired 325
tracked source bodies or companions only after preserving their local copies,
converted all three code-grounded ingests to implementation secondaries, and
left the five analytical sections unchanged except for links and lines that
only duplicated moved metadata. Directory primaries were not admitted.

## Considered alternatives

**Keep one snapshot pointer plus specialized companion fields.** This minimized
schema change, but retained split authority and made every new companion kind a
new special case. `code_revisions` already demonstrated that drift.

**Require exactly one document and one implementation repository.** This was
simple but narrower than the existing paper-with-code workflow, which can need
several repositories for distinct claim-bearing components.

**Treat all resources as a co-equal bundle.** This represented arbitrary
cardinality but erased the rule for title, genre, summary, limitations, and
claim attribution. It also blurred one-source ingestion into multi-source
synthesis.

**Create one ingest per external resource and connect them.** This gave each
resource independent identity and refresh, but charged full ingest overhead to
implementation material used only to qualify one paper and split one grounding
judgment across several reports.

**Keep source bodies tracked.** Git would preserve historical bytes directly,
but repository weight and durable path coupling would continue, and capture
companions would remain mixed with analysis. The selected local-cache design
keeps a stable external handle plus exact checksum while making the possibility
of failed reconstruction visible.

**Retain snapshot genre authority with a one-field mutation exception.** This
preserved ADR 045's placement, but an ignored cache cannot serve as authority
in a fresh checkout and a genre edit changes the very bytes the ingest hashes.
Putting the closer-reading judgment on the tracked ingest restores whole-file
snapshot immutability.

The deciding forces were unambiguous primary identity, resource-specific claim
attribution, economy for ordinary single-source ingestion, support for several
current implementation repositories, and honest reconstruction from absent
local material. V1 resolves the structural choices with one primary, a closed
implementation-only secondary role, an exact-file hash, no compatibility
fields, no directory primary, and no broader ingest-body rewrite.

## Consequences

The operativity path is direct. The ingest and snapshot schemas enforce the
field shapes; the ingest, snapshot, paper-with-code, and re-ingest instructions
govern agent writes; the GitHub and X commands materialize ignored captures;
`commonplace.lib.snapshot` performs checksum-first resolution; source URL
extraction reads the ingest's top-level `source`; and scaffold, package, and
documentation surfaces distribute those contracts. These consumers make the
ADR binding on subsequent source work rather than leaving it as descriptive
history.

A fresh checkout can identify every primary observation without its local
file and can attempt reconstruction. Exact bytes remain usable regardless of
local filename. Mutable or unavailable upstreams may make a historical
observation unreconstructible; the checksum detects that loss but cannot
prevent it. Local snapshots are not backed up or published by Git, so retaining
irreplaceable source material requires an external retention choice rather
than accidental repository storage.

The durable graph points to ingests or external source URLs, never into the
cache. Snapshot files regain whole-file immutability after capture. Capture
tools may still offer a provisional genre, while ingestion can classify the
same source differently without changing the captured evidence.

## Postponed

- Supporting roles beyond `implementation`, including datasets, supplements,
  evaluation artifacts, and critiques, until a worked case defines their
  identity, materialization, effect on analysis, and validation boundary.
- Genuinely co-equal or directory-backed primaries.
- Non-GitHub or mutable secondary identities and member-specific re-ingestion
  or invalidation.
- Checksums or manifests for capture companions and secondary checkouts.
- An operative installed-KB extension mechanism that adds recurring ingest
  genres and their Limitations lenses beyond the current warned off-list floor.

---

Relevant Notes:

- [ADR 045: source genre is a single open field on the snapshot](./045-source-genre-is-a-single-open-field-on-the-snapshot.md) — supersedes: replaces snapshot genre authority and its mutation exception while retaining the open vocabulary
- [Ingest-report type](../../sources/types/ingest-report.md) — implemented-by: durable primary, capture, genre, checksum, and secondary-source contract
- [Snapshot type](../../sources/types/snapshot.md) — implemented-by: ignored local reading-copy boundary and provisional capture metadata
- [Source collection contract](../../sources/COLLECTION.md) — implemented-by: tracked-ingest versus local-snapshot ownership and link boundary
