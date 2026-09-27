---
description: "Proposal: share one quote-matching core across the three quotation checkers, require each quote to be unique in its eligible source region or carry a checked range, and migrate existing quotations by verification sweep rather than rewrite"
type: reference/types/design-proposal.md
---

# Quote occurrence location and verification

The operator requested this proposal on 2026-09-27 after inspecting citation
errors in agentic-system analysis runs. The scope covers the three quotation
contracts the KB verifies: general KB `verbatim` citations, retained ingest
extracts and agentic-analysis quotations. The first draft proposed an
authoring-time locator tool, a selected-occurrence citation syntax and a
version binding for KB targets. A same-day review with corpus measurements
replaced that with a smaller design: one shared matching core consumed by the
three existing checkers, a uniqueness rule, and a containment rule for ranges
that authors choose to supply, together with moving ingest extracts into the
blockquote form the analysis results already use. This is a proposed design;
nothing here has shipped.

## Current state (as of 2026-09-27)

The [agentic-system analysis skill](../../instructions/analyse-agentic-system/SKILL.md)
requires frozen sources, supporting quotations and a separate judgment that
the passage supports its attached finding. Line ranges are optional navigation.
The [source-check command](../commands.md#commonplace-agentic-analysis-publication)
checks reports before publication, and publication repeats source verification.

Three checkers verify quotations. Each has its own citation parser and source
resolver, and each ends in the same test: does the normalized quote occur as a
substring of the normalized source region.

| Contract | Parser and resolver | Normalization | Tracked corpus |
|---|---|---|---|
| General KB `verbatim` citation | [quote_verification.py](../../../src/commonplace/lib/quote_verification.py): quoted span plus `verbatim` marker plus link in one paragraph; linked Markdown file, restricted to the `## Quotes` section when the target is an ingest ([ADR 082](../adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md)) | NFKC, typography, `**`/`__` emphasis stripped, whitespace collapsed | 50 citations in 13 files; every target is an ingest |
| Ingest `Source extract (verbatim)` | [validation.py](../../../src/commonplace/lib/validation.py) `validate_ingest_quotes`: list item; name-paired snapshot whose checksum matches `snapshot_sha256`; skipped when the snapshot is absent or differs | same as above | 822 extracts in 158 ingests; 155 snapshots present locally, all matching |
| Agentic-analysis attributed blockquote | [agentic_analysis.py](../../../src/commonplace/lib/agentic_analysis.py) `_verify_quote_anchors`: blockquote plus `> ---` attribution; git blob at the recorded commit, or checksum-pinned capture | whitespace collapsed only | 1,592 quotes in 44 retained results; 1,528 in the local `path @ commit` form, none of those carrying a line range |

Every ingest extract also carries a free-form `Source location` sub-item
written by the [grounding skill](../../instructions/cp-skill-ground/SKILL.md).
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

Two quotation populations sit outside the three contracts. The legacy reviews
under `kb/agent-memory-systems/` hold 29 `> ---` quotes that receive only the
shape check in `validate_quote_citations`. The ingest `Source location`
sub-item records a location on all 822 extracts that nothing validates.

## Problem and forces

Presence-only matching accepts a quote found anywhere in the source region.
When the quote repeats, the citation does not identify which occurrence the
author read, and a range the author supplies is never tested against the
quote. The observed failures were miscounted line numbers, which the checker
would not have caught had they been in bounds, and which it did not need in
order to verify the quote.

The separation to preserve is between mechanical matching and evidential
selection. Code can establish where a string occurs in a fixed source version.
The authoring agent must read the context and decide whether that occurrence
supports the claim. A unique match does not settle that decision.

The three checkers differ legitimately in citation syntax, source identity
and policy when source bytes are unavailable. They do not differ legitimately
in how a quote is matched, yet they hold three matching implementations with
two normalization rules. Emphasis stripping is safe for prose and can erase
meaningful characters in code, and Markdown sources can quote code, so the
source kind rather than the file extension has to choose the rule.

Version binding pulls in two directions. Git commits and capture checksums
already freeze the analysis and ingest sources. KB documents are living files,
and a note that cites an ingest points only at a path. Pinning the ingest's
bytes would detect every edit, but an edit changes a citation's meaning only
sometimes, so the pin would force a recheck on every grounding append to catch
the rare case. Validation already re-resolves each citation against current
bytes on every run, so a removed or altered quote fails without a pin.

## Options

### Guidance only

Strengthen authoring instructions to read numbered source text and copy
locations with excerpts. Writers, grounding agents, coordinators and
specialists consume this through their instructions. No code changes. This
does not close the containment gap for ranges that are supplied, does not
detect repeated occurrences, and leaves three matchers in place. Adoption
would require evidence that guidance alone reduces the observed failures.

### Shared matching core with uniqueness and containment rules

Extract one matching function that the three checkers call: normalize by
source kind, count occurrences of the quote in the eligible region, return the
count and positions. Add two rules to that core. A quote must occur exactly
once in its eligible region, or its citation must carry a range within which
it occurs exactly once. A range that is supplied is checked for containment,
not only for bounds. Ranges stay optional; the quote is the primary locator,
and an author resolves a repeat by quoting more context or by adding a range.

Operativity: the three verifiers consume the core through `commonplace-validate`
and the analysis source-check and publication commands, with the same force
each check carries today. The writing, grounding and analysis instructions
gain one sentence: quote enough that the passage is unique in its source, and
if you give a range, the quote must fall inside it. No new command surface.

On its own this fixes the containment gap, exposes the repeated-occurrence
cases the measurement found, and removes two of the three matchers, without
changing any citation syntax. It leaves three parsers, an unread location
field on every ingest extract, and the legacy review quotes unverified. The
recommended candidate is this core together with the next option.

### Shared core plus ingest extracts in the analysis blockquote form

This is the recommended candidate: the shared core above, and a rewrite of
ingest extracts from the `Source extract (verbatim)` list item into the
blockquote form the analysis results already use for checksummed captures:

```markdown
> quoted text
> --- `kb/sources/.snapshots/<slug>.md` @ `sha256:<checksum>`
```

The free-form `Source location` sub-item becomes an optional range in the
attribution, which the containment rule then checks. The analysis parser reads
ingest quotes, so the shared core has two callers instead of three, and the 29
legacy `> ---` quotes under `kb/agent-memory-systems/` fall under the same
parser. Multi-line and code extracts render as blocks instead of wrapped list
items.

Operativity: the ingest checker in `commonplace-validate` and the grounding
skill's append step consume the new form; ADR 073, the ingest type template
and the grounding skill name the list-item form and would be amended. The
note checker must strip blockquote markers and attribution lines from the
Quotes section before matching, or a note's multi-line quote stops matching
its own extract.

Cost: a scripted rewrite of 822 extracts across 158 ingests. Nothing pins
ingest bytes by hash, so no integrity records cascade, though review baselines
on edited ingests go stale as after any edit. The core can land first and the
rewrite follow, since the core fixes the observed problem by itself; but the
proposal recommends both, because the rewrite is what reduces the parsers to
two, gives ingests a location the checker reads, and brings the legacy review
quotes under verification.

### Locator with enforced selected-occurrence citations

Add a shared read-only operation that receives an identified source version,
an eligible region and a quotation, and returns every occurrence with context,
with bounded delivery for large match sets. Extend all three citation
contracts so the selected occurrence is identifiable in every retained
quotation, bind KB targets to a source version, and migrate every existing
quotation to the new representation.

This was the first draft's recommendation. The review set it aside. Its
location output answers a question the quote already answers whenever the
quote is unique, which the measurement found to be the case for over 99% of
the corpus. Its citation-contract change would rewrite 1,592 retained analysis
quotes and cascade through the pinned hashes listed above, for artifacts whose
existing representation already carries version and path. Its KB version
binding would invalidate every citing note on each grounding append. It
remains recorded here as the option to return to if repeated occurrences turn
out to be common in some future source class.

## Shared mechanism and workflow boundaries

The mechanism has three layers, and only the innermost is fully shared.

- **Citation parsing** has two forms: the prose paragraph a note uses, and
  the attributed blockquote that ingests, analysis results and the legacy
  reviews use. Each parser yields the same record: quote text, a source
  reference, an optional version binding, an optional range, and the line in
  the citing artifact. The source reference varies by kind (KB path, snapshot,
  git path). The version binding is a commit for git sources and a checksum
  for snapshots; prose citations leave it empty today, and the slot stays in
  the record so a KB citation can carry one if a case for it arises. Prose
  citations also carry no range. Today the two do not yield the
  same record: the blockquote parser returns the quote and a raw attribution
  string that a second step interprets, and the prose checker fuses parsing,
  source resolution and matching in one function. Splitting that function is
  part of the refactor.
- **Source resolution** stays per contract: a KB path with its eligible
  region, a name-paired snapshot with its checksum, a git blob or capture at
  its pinned revision. Each resolver yields source text or a source error, and
  keeps its own policy for unavailable bytes.
- **Matching** is shared: one function applies the normalization the source
  kind permits, counts occurrences in the eligible region, and applies the
  uniqueness and containment rules.

Normalization is chosen by source kind, not declared per citation. Git blobs
and captures get whitespace collapsing only, as the analysis checker does
today. Markdown KB targets and web-captured snapshots get the typography and
emphasis normalization the KB checker uses today. The 10 ingest extracts whose
match depends on emphasis stripping are the cases to inspect when deciding
whether snapshots of code sources should use the code rule.

Ranges and normalization interact in one fixed order: slice by lines first,
normalize second. Line numbers belong to the original source, so the checker
takes the cited lines from the original text, joins them, normalizes that
slice, and counts the normalized quote inside it. No position is ever mapped
from normalized text back to a line, so whitespace collapsing cannot shift a
range. The consequences follow without extra rules: a quote spanning lines
inside the range matches, because the joined slice collapses the same line
breaks the quote does; a quote straddling the range boundary does not match,
because part of it lies outside the slice; a wrong range fails even when the
quote occurs elsewhere in the file; two occurrences inside the range return a
count of two. The one case a range cannot separate is two occurrences on the
same line, since the line is the range's smallest unit; there the author
quotes more surrounding text.

The eligible region remains part of the evidence contract. A quotation citing
an ingest resolves within its Quotes section, as ADR 082 requires. The extract
it matches resolves separately against the pinned snapshot. These are two
checks; matching the note's quote in an ingest does not establish that the
extract was checked against the original source.

KB citations do not fill the version binding today. The ingest's
`snapshot_sha256` is the frozen identity the chain reaches through the
extract, and the extract's neighbours in a Quotes section are other extracts,
not running prose, so an append rarely changes what an existing extract says.
No tracked citation targets a mutable note today. The slot is optional in the
shared record rather than absent, so that a citation class which does need a
pin, such as a note quoting another note, can fill it without changing the
record or the checkers; the resolver for that kind would then have to reject a
binding that no longer matches the target's bytes.

## Proposed occurrence behavior

| Occurrences in eligible region | Checker result |
|---|---|
| None | Fail: quote does not occur in the identified source region. Distinct from a source error such as a missing snapshot or a checksum mismatch. |
| One | Pass. If a range is supplied, pass only if the occurrence lies inside it. |
| Several, no range | Fail with the count. The author quotes more context or adds a range. |
| Several, range supplied | Pass only if exactly one occurrence lies inside the range. |

A very short quote with many occurrences fails with its count. That is the
signal that the quote is too short to be evidence; the checker does not page
through matches. Missing files, inaccessible sources and identity mismatches
are source errors, reported separately from a completed search with no match.

## Verification warrant and limits

The automated oracle is the identified source version plus deterministic
matching under a declared normalization. It can establish that the quoted
string occurs in the eligible region of the current source, exactly once or
exactly once within the cited range. It cannot establish the source's truth,
the passage's relevance, or the claim's validity. Semantic support stays with
the authoring agent.

Presence in the current source also does not establish that the surrounding
text still supports the reading the citing artifact gives it. An edit to a
living KB file can change a quote's meaning without touching the quoted
string. The KB accepts this gap for KB targets rather than pinning versions of
living files, because a pin would detect every edit and could not tell which
edits mattered. For frozen analysis and ingest sources the gap does not arise:
the source cannot change under the citation.

## Free choices and adoption criteria

The exact shape of the shared function, the position representation it
returns, and where in the analysis attribution grammar a range is written
remain open. Whether web-captured snapshots of code repositories should use
the code normalization rule is open and should be decided from the 10 measured
cases.

### Migration

Migration has two parts. For notes and analysis results it is a verification
sweep, not a rewrite. The new core runs over every existing quotation under
the existing citation syntax. Quotes that are unique in their eligible region
pass unchanged, so their artifacts and the hashes that pin them stay as they
are. The sweep lists the quotes that fail the new rules: the 8 measured
repeats, any range that does not contain its quote, and anything the sweep
finds beyond the measurement. Only those citations are edited, by extending
the quote or adding a range in the original artifact, and only those artifacts
have their dependent hashes refreshed. The record of each such edit says
whether it changed the citation alone or also the claim.

For ingests it is a scripted rewrite of the Quotes section: each extract
becomes a blockquote, its `Source location` text moves into the attribution
as a range where it names one and is otherwise kept as a trailing note, and
the attribution names the snapshot path and `snapshot_sha256`. The script
changes no quoted bytes. The ingest checker then runs over the rewritten
ingests and the note checker over every note that cites them, and both must
report the same matches as before the rewrite, apart from the measured
repeats.

Superseded runs and untracked state under `kb/reports/state/` are swept and
reported but not edited unless the operator asks. The three ingests without a
local snapshot stay in the conditional state ADR 073 already defines for them:
their extracts are unverified on this machine, which the sweep reports
and does not treat as a blocker.

### Acceptance evidence

Adoption of the recommended option requires tests showing: a unique quote
passes; a repeated quote without a range fails with its count; a repeated
quote with a range containing exactly one occurrence passes; a range that
excludes the quote fails even when the quote occurs elsewhere; a range
containing two occurrences fails; multiline and whitespace-normalized quotes
match; the code rule does not strip emphasis markers; an ingest's analysis
prose cannot satisfy a note's quotation; and unavailable source bytes are
reported as a source error, not as a pass. The three verifiers must return the
same result for the same quote and region. For the ingest rewrite: the
blockquote parser reads an ingest extract and its attribution resolves to the
name-paired snapshot; a note's quote matches inside a Quotes section that now
holds blockquote markers and attribution lines; and an attribution line cannot
itself satisfy a note's quotation.

The sweep over the tracked corpus must complete with its failure list
reviewed, the listed citations fixed, and every affected hash record
consistent. One analysis run after the change must show that quotes without
ranges publish, and that a specialist who supplies a wrong range is stopped by
the containment check rather than by manual review.

### Scope gaps

The recommended candidate closes two gaps the shared core alone leaves open.
The 29 legacy `> ---` quotes under `kb/agent-memory-systems/` receive only a
shape check today; under the blockquote parser they are verified like analysis
quotes, and the sweep will report which of them resolve against their pinned
GitHub blobs. The ingest `Source location` sub-item is unread today; the
rewrite replaces it with a checked attribution. If the core ships without the
rewrite, both gaps stay open and need their own decision.
