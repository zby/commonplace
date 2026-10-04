---
description: Shared quote matching requires one occurrence in the eligible source region, with checked optional ranges and source-kind normalization
type: reference/types/adr.md
status: accepted
---

# 094 — Quotations require a unique occurrence or a containing range

**Status:** accepted
**Date:** 2026-09-27
**Amended by:** [ADR 105](./105-let-analysts-run-their-acceptance-check-before-submission.md) replaces analysis citation construction with an analyst-callable acceptance check and path-only attribution. The constructor clauses below record the earlier decision; normalization and uniqueness remain current.

## Context

A quotation can occur in a source without identifying one occurrence. A
plausible line range can point elsewhere in the same file. Presence and range
bounds alone do not establish that the cited passage occupies the location
an author gives it. Different matching implementations also let the same
quotation receive different treatment without a source-kind reason.

The evidence boundary must remain separate from mechanical matching. Finding
one occurrence cannot establish that its context supports the attached claim.
A note citing an ingest depends on retained source passages, not the ingest's
analysis or its attribution text.

## Decision

Adopt the shared matching core and attributed-ingest form from *Quote
occurrence location and verification*. Parsing produces one citation record
with quoted text, source reference, optional version, optional line ranges,
and the citing line. Prose citations and attributed blockquotes remain two
syntax forms. Source resolution keeps each contract's identity and
availability rules.

Analysis authors use `commonplace-quote` to construct citations from selected
text and the run's frozen source. It returns only the citation for a unique
occurrence, or exact source excerpts, derived ranges and selection metadata for
two to ten occurrences. More than ten asks the author for a longer quote instead
of emitting an unwieldy candidate set. The author chooses
an occurrence and inserts its citation unchanged. Occurrences on the same line
receive additional source context when needed. The generator does not validate
documents; publication invokes regular run-state validation on the assembled
bundle. No separate authoring-time source-check command is required.

Require exactly one occurrence in the eligible source region. If a citation
supplies a range, require exactly one complete occurrence inside it. Slice
original source lines before normalization. Separate extracts and disjoint
ranges remain separate regions; they cannot form a synthetic passage by
concatenation. A repeated quote without a range fails with its occurrence
count. Two occurrences on one line require more quoted context.

Git blobs and analysis captures use whitespace-only normalization. Ordinary KB
Markdown and web or paper snapshots retain typography and Markdown
emphasis normalization. Repository snapshots and citations of their retained
ingest extracts use whitespace-only normalization,
including sources declared as code repositories and recognized repository
hosts. The inspected emphasis-dependent extracts are prose; none requires
weakening the repository rule. The source resolver selects the rule, never a
per-citation switch.

Amend [ADR 073](./073-untracked-source-snapshots-require-ingest-grounding.md)'s populated Quotes contract: each extract is an attributed
blockquote naming the exact name-paired snapshot and its checksum. A path may
carry a checked line range; a trailing locator note supplies context but is
not evidence. Notes citing an ingest search only the blockquote bodies in
its Quotes section. Verification against those bodies does not imply that
the separate snapshot check ran on this machine.

KB prose citations remain unversioned and are checked against current bytes.
An ingest append therefore does not invalidate every existing citation by
hash. A removed or changed supporting passage can still fail its next check.
Snapshots and Git sources retain their existing frozen identities. Missing
source bytes are reported separately from an absent quotation and never count
as verified. Ingest snapshot absence remains conditional and non-blocking.

The authorized migration may remove byte-identical duplicate extracts while
preserving distinct locator information and support for citing notes. This
exception does not change the standing append-only rule or authorize semantic
deduplication. Reviews in the collection scheduled for decommissioning are
outside this migration.

## Considered alternatives

**Guidance alone.** Numbered rereading can prevent some author errors, but
cannot enforce containment or distinguish repeated occurrences.

**Shared matcher with the list-item ingest form.** This fixes occurrence
checks but keeps a third parser and an unchecked location field. Attributed
blocks let the existing analysis syntax carry both identity and optional
checked ranges, including multiline passages.

**Checking author-written citations without a constructor.** This leaves range
calculation and formatting to the author and catches mistakes only after
drafting. Source-derived construction now replaces that authoring step. It
returns all candidates rather than choosing an occurrence for the author.

**Mandatory selected-occurrence syntax.** An occurrence ordinal would add a
new persistent citation form. Generated excerpts with containing ranges use
the existing form; same-line repetition is handled with source context.

**Hash-pin every living KB target.** This detects all target edits but cannot
distinguish relevant changes from unrelated appends. Current-byte quote
verification retains a narrower dependency. It does not detect a changed
interpretive context when the quoted words remain unchanged.

## Consequences

The deterministic validator consumes the matching rules through the shared
core; publication uses that validator. The coordinator and fresh memory
specialist load the generation requirement through their instructions and type
contracts. Structural citation checks use the same parser. Document link and
ordinary source-anchor scans exclude recognized quotation bodies while keeping
their attributions, so source examples are not treated as author assertions.
The ingest and analysis
types define the citation form; grounding and writing instructions teach it;
fresh-project collection templates expose the same form. Existing projects
retain their own content on initialization and must migrate old quote items
before they pass the new checks. Invalid quotations fail at the same checking
boundaries as before; unavailable ingest snapshots remain explicitly
unverified rather than becoming publication-style hard failures.

The checker establishes occurrence, uniqueness, and range containment under
its normalization rule. It does not establish truth, relevance, or semantic
support. The migration's corpus measurements and publication trial bound its
acceptance evidence; they are not a new evaluation of any analysed system.
