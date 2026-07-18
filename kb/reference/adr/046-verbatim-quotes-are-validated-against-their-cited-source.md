---
description: "`commonplace-validate` resolves every `verbatim`-marked quotation against the source it links; a false verbatim claim fails, and `unresolved` warns only where the convention is demonstrably in use"
type: ../types/adr.md
tags: []
status: accepted
---

# 046-Verbatim quotes are validated against their cited source

**Status:** accepted  
**Date:** 2026-07-12

## Context

A `verbatim` citation asserts that a quoted span is copied exactly from a source retained in the KB. The dialectical/evidential profile has mandated the three-part convention — file link, prose locator, and a grounding-layer marker of `verbatim` / `paraphrase layer` / `second-hand` — since [ADR 042](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md). Until now nothing checked it: an author wrote a quote, wrote `verbatim`, and the claim was hand-maintained and trusted.

That is exactly the state [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) forbids. All four of its preconditions hold here: the derivation rule is a strict substring test, the quote names its source via the adjacent markdown link, the source snapshot is a checked-in file present at validation time, and the extraction heuristic is a single centralized artifact amortized across every citation it protects. The check is therefore Level A — deterministic, near-zero cost — not a judgment-based review gate.

The prototype supplied the missing evidence the proposal initially lacked — it did not originate from a felt friction case, and said so in writing. Run over the sibling `epistack-casebooks` corpus it found **63 match, 18 mismatch, 6 unresolved** across 87 candidates, with no false mismatch on manual audit. The mismatches are real failures of the strict assertion, dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary.

## Decision

`commonplace-validate` resolves every `verbatim`-marked quotation against the markdown source it links, as a generic check alongside link health — not a type rule, because the trigger is the citation, not the note's type. A note that asserts a verbatim quote gets checked whatever it is.

Three outcomes, with deliberately asymmetric severity:

- **mismatch → fail.** The note asserts a falsehood. Per the derived-copy rule the false-copy failure mode is silent and unbounded, so it cannot be a warning.
- **unresolved → warn, but only in notes carrying at least one resolvable verbatim quote.** An unpaired verbatim citation is a parser-coverage gap worth surfacing where the convention is in use. Warning on it unconditionally would fire in every KB that merely *writes about* the convention — this repo has ten such candidates and zero real ones — and a check that cries wolf teaches authors to ignore it, which is the failure the check exists to prevent.
- **match → pass**, reported as a count.

`commonplace-verify-quotes` gives the corpus-wide view (match / mismatch / unresolved counts over many files) that an audit or a before/after sweep needs; the validator gives the per-note enforcement.

**Both referential checks share one notion of code.** This is the second check that *dereferences* — that resolves an element of a note against a second artifact — link health being the first, and the two must not disagree about what counts as content. A fenced code block *demonstrating* the citation convention is showing it, not asserting it; scanning one reports a false mismatch against whatever source the example links, which the first cut of this check did. Code fences are therefore neutralized in `note_parser` by a single primitive, `blank_fenced_code_blocks`, which both checks consume. It blanks rather than deletes: a check that only needs the *set* of matches (link health) is indifferent, while a check that pairs elements by proximity and reports line numbers (this one) needs the offsets to survive.

## Consequences

The `verbatim` marker becomes load-bearing rather than decorative: it is now the cheapest of the three grounding-layer markers to assert and the only one that can be mechanically falsified. `paraphrase layer` and `second-hand` remain unchecked by construction — they never claimed exact text, and no derivation rule exists for them, which is precisely why [a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).

Downstream KBs adopting the dialectical/evidential profile inherit the check with no configuration. The 18 live mismatches in the sibling casebooks are not fixed here: those notes are slated for a from-scratch rebuild, and the point of shipping the checker first is that the rebuild's citations land machine-checked rather than hand-trusted.

The extraction heuristic is not complete, and `unresolved` is how it says so rather than passing silently. Normalization (quote-mark folding, whitespace collapse, emphasis stripping, `NFKC`) is load-bearing, not polish: an under-normalized checker would produce false mismatches on correct quotes, which is worse than no check.

**An open architectural question this decision surfaces rather than settles.** The dividing line in validation is *not* frontmatter versus body — the schema already validates the body. `ParsedDocument.to_validation_object()` hands the schema `body`, `headings`, `links`, and `body_dates`, and several type schemas assert required headings. Anything about a note's own text that the parse model exposes is expressible declaratively, and is type-owned.

What the schema **cannot** express is **dereferencing**: it has no way to say *follow this path and look inside the artifact it names*. So the real class is **referential checks** — does this link's target exist (link health), does this quoted span occur in the source it cites (this ADR). Their ground truth lives outside the document, which is precondition 3 of the derived-copy rule, and it is why they are hand-written imperative passes rather than schema constraints.

That class has no design. It has no shared model of a *positioned* element, no shared severity policy, and no owner. Sharing the code-fence primitive removes the immediate divergence without supplying one, and the shared parse remains lossy for it: `ParsedDocument.links` is a tuple of URLs with no positions, which suffices for link health (it needs only the set) but not for proximity pairing, so the quote checker still carries a private link regex. The gap belongs to the kb-graph-loader workshop — and it is the same gap, since a referential check *is* a graph edge being resolved.

Supersedes and retires the verifiable-quotes proposal, whose content has shipped.
