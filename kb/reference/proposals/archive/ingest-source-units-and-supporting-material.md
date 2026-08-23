---
description: "Proposal (adopted): dated pre-migration source-unit contracts and corpus observations behind the ingest authority decision"
type: ../../types/design-proposal.md
---

# Ingest source units and supporting material

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 072](../../adr/072-ingests-own-source-authority-and-snapshots-are-local.md): the live source authority and primary/secondary design now reside in that ADR, the [source collection contract](../../../sources/COLLECTION.md), and the [ingest-report type](../../../sources/types/ingest-report.md). What remains here is the dated pre-migration state and corpus observations that the decision was tested against.

## Current state (as of 2026-08-22)

- The ingest-report type required one repository-relative `source_snapshot`
  string. The paired tracked snapshot supplied the canonical source URL,
  capture metadata, and genre; the ingest carried no primary checksum.
- [ADR 045](../../adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)
  made the snapshot the single genre authority and required ingestion to edit
  that value when closer reading changed the classification.
- The ingest type optionally accepted `code_revisions`, an array of immutable
  GitHub commit URLs. Three ingests used it.
- The [paper-with-code procedure](../../../instructions/ingest-paper-with-code.md)
  treated the version-pinned paper as primary and repositories as
  corroborating implementation evidence. It already allowed several
  repositories when they implemented distinct claim-bearing parts.
- The [directory-ingest procedure](../../../instructions/ingest-directory.md)
  treated one ephemeral, usually ignored directory as a source unit. That
  directory could contain a repository, a paper with supplements, or grouped
  captures, while the durable report recorded only an upstream pin where one
  existed.
- Ordinary tracked snapshots, ignored repository checkouts, and grouped
  working copies therefore used different storage and capture paths while
  producing the same ingest-report type. No general durable relation stated
  why an additional external resource belonged to the primary source or what
  evidential role it played.

## Corpus observations behind adoption

- Ordinary ingests remained single-source in practice, so an empty companion
  structure would have taxed the common case.
- The three code-grounded ingests established a real multi-resource case, and
  the existing procedure's several-repository allowance ruled out a fixed
  document-plus-one-repository pair.
- Repository evidence qualified implementation claims without becoming
  co-authority for the paper's title, genre, reported results, or limitations.
- Directory ingestion could conceal arbitrary member cardinality, but the
  corpus supplied no worked case that required a genuinely co-equal primary
  bundle.
