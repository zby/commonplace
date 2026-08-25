---
description: "Proposal (retired): dated corpus measurements behind replacing paraphrased ingest claims with direct checks against retained quotes or snapshots"
type: ../../types/design-proposal.md
tags: []
---

# Deterministic note-to-ingest claim checking

> **Archived** (see [archive README](./README.md)). Retired by the 2026-08-25
> revision of [ADR 073](../../adr/073-untracked-source-snapshots-require-ingest-grounding.md).
> The live design now checks a note directly against retained verbatim quotes
> or a declared checksum-verified snapshot. What remains here is the measured
> pre-migration state.

## Current state (as of 2026-08-24)

- The virtual `source` review lens had recorded 33 `(artifact, ingest)` pairs,
  all with a `pass` outcome. It compared note wording with the ingest's
  paraphrased Claims entries rather than directly with source text.
- The grounding instruction asked writers to prefer the exact normalized
  `Claim (paraphrase)` wording. Only 4 of 65 measured note-to-ingest pairs did
  so. The other 61 paraphrased the paraphrase, leaving no shared string for a
  deterministic check.
- The corpus contained 119 Claims entries with 374 exact source extracts. The
  revision retained the extracts and removed the interpreted Claim, Scope,
  Confidence, and Limitation fields.
- The universal verbatim-citation validator found one use across 1,264 files.
  Fifty-five source-citing notes contained long quotations, but only three
  distinct quoted spans occurred in the ingest they cited. Requiring existing
  note prose to quote its ingest would therefore have been a corpus-wide prose
  convention rather than a mechanical activation of established practice.
- The first grounded cohorts had five false extracts before deterministic
  extract verification was added. Four silently repaired capture artifacts: a
  line-break hyphenation, an inline footnote marker, or a LaTeX arrow. This
  measurement is why quote-to-snapshot verification remains mechanical even
  though note-to-source alignment remains semantic.
