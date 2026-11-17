---
description: "Quote checking in general: what a wording check, an occurrence check and a source-identity check each establish, which evidence a pass is relative to, and what stays unverified — attribution upstream, contextual support, truth"
type: types/note.md
tags: [document-system, claims-and-grounding, kb-maintenance]
---

# A citation cannot assert more fidelity than its capture preserved

Marking a span as an exact quotation asserts that these words occur in a named source. Unchecked, that assertion rests on the author's word. A quote check makes it falsifiable by testing one relation: given a quoted span, a resolved source text and a normalization rule, does the span occur in that text, once or once inside a stated range? Markers that never claimed exact wording, such as a paraphrase marker, give the check nothing to match.

## Four questions, one answered mechanically

A citation raises four separable questions:

1. Wording: do these words occur in the compared text?
2. Attribution: is the compared text the source the citation names, and did the named author produce it?
3. Context: does the passage, read where it occurs, support the use the citing text makes of it?
4. Truth: is the quoted claim true?

A string check answers only the wording question. An identity check answers part of the second question (below). Context needs a reader of both texts. Wording agreement is deterministic, cheap and binary, so it can run on every pass. Judging support is costlier and noisier, so it cannot simply block the way a wording check does, and how reliably it detects out-of-context use is unmeasured.

For an exact-wording claim, an inexpensive occurrence check can justify treating mismatch as failure rather than warning. This is a choice within the [trade-off between checking cost and reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md), not a universal rule for retained results. Later readers can reuse the check's result, accepting the risk of changes since it ran.

## What makes "exact" meaningful

"Exact" means "equal after this normalization rule", and the rule can err in both directions. Too little normalization fails correct quotes on quote marks or whitespace; [ADR 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) judges such false mismatches worse than no check. Too much would let substantive edits pass. In one casebook corpus the real mismatches were mostly editorial omissions, bracketed substitutions and case changes (ADR 046), which a permissive enough rule would ignore. Typography and emphasis can affect meaning in prose as well as code; a normalization rule must specify which differences it ignores.

Occurrence is not location. A span can occur several times, and a plausible line range can point elsewhere in the same file. Requiring exactly one occurrence, or exactly one complete occurrence inside a checked range, removes ambiguity about which passage the span equals. Forbidding concatenation of disjoint ranges prevents certifying a passage that never existed contiguously (ADR 094). Uniqueness does not establish that the author intended this occurrence. A locator the check does not test supplies context but is not evidence.

## Which evidence a pass is relative to

A pass means "agrees with the evidence this check used". That evidence may be the original, a capture (a retained copy of the source bytes taken at one time), an intermediary's retained extract, or nothing.

Source identity comes first. A checksum against a recorded capture, with explicit name pairing between citation and file, binds the compared bytes to that capture; equal bytes at an arbitrary path do not (ADR 073). A mismatched or unreadable file is a failure, not an invitation to find another copy. The binding stops at the capture: no mechanism here checks that the capture faithfully represents the original or that the named author wrote it. A pin records identity, and change is detected only when a later check compares current bytes with it. Checking current bytes catches a changed or removed passage at the next check, but misses a changed surrounding context when the quoted words survive.

Retained, accessible and used material differ. A capture kept on another machine is not evidence for a check on this one, and neither is text that happens to sit in a model's context. Missing bytes therefore report as unverified, never as passed. A silent fallback to whatever copy is present would make one citation pass or fail with ambient cache state, without declaring that dependency (ADR 073).

A model may need several reads to check a source that exceeds its context budget. Each excerpt can preserve the wording exactly while omitting context needed to judge the quotation’s use. The checker must retrieve that context before judging support; the full source can remain stored outside the model’s context.

Exactness and second-hand provenance are independent. A quote can be exact with respect to an intermediary's extract and second-hand with respect to the original. Each exact check in a chain, such as capture to extract and extract to note, verifies only its own pair. Semantic hops compound instead: checking a paraphrase against a paraphrase adds a judgment at each hop, and rewording at either hop can change the proposition. Checking against verified source extracts avoids judging a paraphrase of a paraphrase.

## Scope

- Covers textual sources with retrievable bytes. Audio, images, oral quotation and sources whose original is gone are out of scope.
- Transfer beyond agent-operated KBs rests on the reasoning above, not on external evidence.
- Marked editorial alterations (ellipsis, brackets) fail a strict wording assertion; whether a segment-wise check could support them is open.
- An "unresolved" outcome covers recognized quote candidates the checker could not pair with a source. Quotations the extractor never recognized appear in no outcome, and their rate is unmeasured.
