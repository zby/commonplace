# Where quotation validation still disagrees

The quotation matcher accepts some valid citations that structural validation
rejects. Structural validation also calls some unparseable citations
well-formed. Separately, document-wide link and source-anchor scans interpret
quoted source content as citations authored by the report. Sharing the quote
matcher did not remove these competing interpretations.

The agents did use the source-check command. The shipped tools detect invalid
quotes and ranges after drafting; they do not construct citations or derive
their endpoints for the author. The expectation that tooling would prevent
range mistakes during construction is broader than the implemented design.

## Scope and evidence

The operator requested this follow-up on 2026-09-27 after the
[pilot root-cause analysis](./source-check-root-causes.md). Inspection used
implementation at `4a97ad715a4dbdcc6de09dea22417d1f88fbbbdf`, its tests, and
the six worker traces listed in the [rerun record](./quote-rerun-20260927.md).
The specialist instruction and type fixes made during this follow-up change
guidance, not validator behavior.

Small Python probes called the actual parser, structural checker, quote
verifier, link checker and ordinary source-anchor checker from the editable
installation. A temporary Git repository held one committed README and an
existing source-side image. A separate checksum-pinned file exercised capture
attribution. The probes changed no pilot artifacts or producer code. They
isolate component disagreements; the pipeline order below establishes how
those disagreements block publication.

## 1. Two attribution grammars disagree in both directions

[`parse_blockquotes`](../../../src/commonplace/lib/quote_matching.py) recognizes
an HTTP(S) URL or a pinned local path. The structural checker
[`validate_quote_citations`](../../../src/commonplace/lib/validation.py)
then applies its own `_SOURCE_REF_RE`, recognizing Markdown links or code
spans. It does not use successful source parsing as its source-presence test.

For the same unique source passage and full Git commit, the probes found:

| Attribution form | Shared parser | Structural citation check | Frozen-source quote check |
|---|---|---|---|
| Bare full-commit GitHub URL | accepts | warns: names no source | passes |
| Angle-bracket GitHub autolink | accepts | warns: names no source | passes |
| Markdown GitHub link | accepts | passes | passes |
| GitHub URL in a code span | accepts | passes | passes |
| Local path and full commit in code spans | accepts | passes | passes |
| Unpinned local path in a code span | rejects | passes | rejects |
| Relative Markdown source link | rejects | passes | rejects |
| Arbitrary code span naming “documentation” | rejects | passes | rejects |

A bare URL exactly matching the registered capture identity also passes
frozen-source matching but gets the structural “names no source” warning.
The defect is therefore broader than GitHub URLs.

The reverse disagreement has a specific cause: structural validation adds a
parser error only when `citation.source is not None`. When the parser cannot
identify any source, `source` is `None`, its error is suppressed, and a code
span or Markdown link can satisfy the separate regex. The checker then reports
the citation well-formed. The source verifier still rejects it; this is not
evidence that publication admits an unsupported quotation.

Structural checking need not resolve Git objects or validate a capture digest.
That is a legitimate division of responsibility. Calling a parser-rejected
attribution well-formed, or claiming a recognized URL names no source, is a
different problem: the layers disagree about the syntax itself.

The structural helper also serves legacy memory reviews. A repair must decide
the syntax required by each consuming type, without silently imposing the
agentic publication contract on every old artifact or keeping an accidental
regex fallback as the shared rule.

## 2. Quoted links lose their source context

[`find_markdown_links`](../../../src/commonplace/lib/note_parser.py) includes
links inside blockquotes. It returns target strings without their containing
quotation or its source identity. `validate_links_from_document` resolves
relative targets from the report directory.

The probe quoted `![Diagram](figures/diagram.png)` exactly from the pinned
README. The image existed in the source repository. Quote verification passed,
but document link validation warned that the target was missing. Adding an
unrelated file at the report-relative path cleared that warning. The result
depends on the report's local neighborhood, not the quoted source's link.

This reproduces the Dynamic Cheatsheet image failure. The underlying problem
is lost context, not an incorrectly copied image URL. A faithful source quote
can contain relative links without asserting they are report-relative links.

## 3. The ordinary source-anchor scan has the same context problem

[`_verify_source_anchors`](../../../src/commonplace/lib/agentic_analysis.py)
scans the entire document with separate regexes. It does not exclude attributed
quote bodies or distinguish literal source examples from the report's own
evidence anchors.

Two additional probes both passed quotation matching:

- A README quotation containing a GitHub blob link to another repository was
  rejected as using the wrong repository by the ordinary anchor checker.
- A README quotation containing the literal code example `other/file.py:1-2`
  was rejected because that example path did not exist in the reviewed commit.

These are reproduced adjacent defects, not additional failures counted in the
three pilots. They show that repairing only the Markdown image scanner leaves
the same mistake in another validation layer. A source is allowed to discuss
another repository or show a fictional path; exact quotation does not make
those strings the report author's own evidence assertions.

## 4. Pipeline order makes these warnings blocking

[`verify_sources`](../../../src/commonplace/lib/agentic_publication.py) first
runs `_clean_validation`, then quotation matching, then ordinary Git source
anchor verification. `_clean_validation` rejects both warnings and failures.

Thus a bare valid URL or copied relative image can stop the command before the
quote matcher runs. A quoted foreign blob URL can pass quotation matching and
then fail the ordinary anchor scan. The command's failure does not necessarily
mean the quotation matcher found a problem.

Ordinary `commonplace-validate` allows warnings with exit zero. Publication's
stricter acceptance is explicit and useful; changing all warnings to
non-blocking would conceal the underlying classification errors.

## Tool use and the range expectation

All six pilot workers executed `commonplace-agentic-analysis-publication
verify-sources`. The trace locations and failed checks are recorded in the
rerun and root-cause reports. Agents corrected the rejected ranges and quotes
before publication. The evidence does not support attributing these failures
to failure to invoke that tool.

The installed command surface contains checkers, not a quotation constructor:

- `commonplace-agentic-analysis-publication verify-sources` checks the already
  written analysis or specialist report against the frozen source. It does
  not edit the report or return a generated replacement citation.
- `commonplace-verify-quotes` audits the separate `verbatim` prose-citation
  interface. It is not the authoring command for analysis blockquotes.
- The shared `match_quote` returns occurrence count and an error. It validates
  supplied ranges but does not return the matching source span.

[ADR 094](../../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md)
explicitly considered a locator command and selected counts with optional
ranges instead. Construction was left to the author. The eight observed
range diagnostics concerned ordinary source anchors, not quotations lying
outside their attributed ranges. Both kinds are checked, but neither kind is
generated by the shipped checker.

The instruction fix now delivers uniqueness and range rules to specialists,
requires the Source register contract, preserves comment markers, and removes
the conflicting requirement that every ordinary anchor include a range.
Those changes can reduce avoidable mistakes. They do not establish a workflow
in which tools construct valid quotations and locations before insertion.

## Repair boundary and acceptance

The first validator repair should make structural attribution checking honor
the shared parsed citation and surface parser errors consistently. Then retain
quotation context through both link discovery and ordinary source-anchor
discovery. Quotation attributions must still identify and verify their frozen
source; report-authored links and source anchors must still be checked.
Neither weakening literal matching nor skipping all blockquote links is an
adequate substitute for distinguishing source text from author assertions.

Existing tests cover matching, range containment, source identity and the
read-only source-check command. The inspected syntax tests cover Markdown
GitHub links and pinned paths, but not the bare URL crossing both layers.
The shared-matcher agreement test compares matching outcomes, not the whole
artifact acceptance path. It cannot detect the pre-matcher structural veto.

Acceptance should exercise the documented URL and path forms through the
whole source-check path, reject parser-invalid forms consistently, and retain
exact quotations containing relative links, foreign blob URLs and example
paths while still rejecting invalid report-authored references. Include
wrong-commit, missing-source, altered-text, ambiguous-quote and invalid-range
controls so accepting valid forms does not weaken source verification.

No validator repair or citation-generation feature was implemented by this
investigation. The probes establish the disagreements; they do not establish
their frequency across the full corpus.
