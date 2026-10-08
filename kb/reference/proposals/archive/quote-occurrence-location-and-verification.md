---
description: "Proposal archive: quote-checker corpus measurements from 2026-09-27 before the shared matching migration"
type: reference/types/design-proposal.md
---

# Quote occurrence location and verification

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 094](../../adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md), which carries the decision and alternatives. The dated pre-migration observations below remain as design texture.

## Current state (as of 2026-09-27)

The [agentic-system analysis skill](../../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md)
requires frozen sources, supporting quotations and a separate judgment that
the passage supports its attached finding. Line ranges are optional navigation.
The [source-check command](https://github.com/zby/commonplace/blob/866ac51a4/kb/reference/commands.md#commonplace-agentic-analysis-publication)
checks reports before publication, and publication repeats source verification.

Three checkers verify quotations. Each has its own citation parser and source
resolver, and each ends in the same test: does the normalized quote occur as a
substring of the normalized source region.

| Contract | Parser and resolver | Normalization | Tracked corpus |
|---|---|---|---|
| General KB `verbatim` citation | [quote_verification.py](../../../../src/commonplace/lib/quote_verification.py): quoted span plus `verbatim` marker plus link in one paragraph; linked Markdown file, restricted to the `## Quotes` section when the target is an ingest ([ADR 082](../../adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)) | NFKC, typography, `**`/`__` emphasis stripped, whitespace collapsed | 50 citations in 13 files; every target is an ingest |
| Ingest `Source extract (verbatim)` | [validation.py](../../../../src/commonplace/lib/validation.py) `validate_ingest_quotes`: list item; name-paired snapshot whose checksum matches `snapshot_sha256`; skipped when the snapshot is absent or differs | same as above | 822 extracts in 158 ingests; 155 snapshots present locally, all matching |
| Agentic-analysis attributed blockquote | [agentic_analysis.py](https://github.com/zby/commonplace/blob/866ac51a4/src/commonplace/lib/agentic_analysis.py) `_verify_quote_anchors`: blockquote plus `> ---` attribution; git blob at the recorded commit, or checksum-pinned capture | whitespace collapsed only | 1,592 quotes in 44 retained results; 1,528 in the local `path @ commit` form, none of those carrying a line range |

Every ingest extract also carries a free-form `Source location` sub-item
written by the [grounding skill](../../../instructions/cp-skill-ground/SKILL.md).
No code reads it. The analysis attribution grammar accepts an optional
`path:start-end` range, and the range checker validates bounds, but nothing
checks that the quote occurs inside the range.

A measurement over the tracked corpus on 2026-09-27 found the ambiguity the
first draft was designed around to be rare:

- Ingest extracts occurring more than once in their snapshot: 6 of 808
  checkable, all repeated table headers or repeated slogans.
- KB citations occurring more than once in the ingest's Quotes section: 2 of
  50, both because the same extract was appended twice.
- Matches that depend on emphasis stripping: 10 ingest extracts, 0 KB
  citations.
- Unresolved verbatim pairings in tracked artifacts: 0. All 112 unresolved
  results live in gitignored state, cache and snapshot directories.

Trace inspection of the three-system replay found two rejected ranges. Mem0's
coordinator read an unnumbered slice requested through line 782 of a 772-line
file, then cited 751–776. Napkin's specialist read an unnumbered README, then
cited 405–411 in its 387-line file. Numbered rereading corrected that citation
and four other README ranges. Both runs recovered before publication. Neither
error reached the quote checker, because it does not use ranges.

Editing a retained analysis result changes bytes that other records pin:
`result.sha256` in the run-state record, `analysis-result-sha256` in the
generated review, the memory-report hash in the result body, and the
`result_sha256` and `review_sha256` columns of the memory-systems comparison
table.

The ingest `Source location` sub-item records a location on all 822 extracts
that nothing validates.

