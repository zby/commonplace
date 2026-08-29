---
description: "Accepted decision that a note may cite at most five distinct tracked sources without a paired verified quotation, enforced as a FAIL validator rule on notes and articles, while the three link-following review criteria drop their reader-side caps"
type: ../types/adr.md
tags: []
status: accepted
---

# 082-Grounding is bounded on the artifact by unquoted sources per note

**Status:** accepted
**Date:** 2026-08-27

## Context

Commonplace placed its grounding reading limit on the review.
`semantic/grounding-alignment` budgeted sixteen distinct linked artifacts per
pass, and `sentence/misleading-link-text` and `sentence/concept-attribution`
each read at most five distinct targets. Every one of those numbers tracks a
corpus statistic, so it has to be recalibrated whenever the corpus's evidence
needs move. When it lags, the failure is silent: a reviewer that stops at its
limit and passes is indistinguishable from one that read everything and passed.

The two representation caps had a sharper problem. Under the note-link
exemption those criteria are what makes the exemption sound, and 55% of
`kb/notes/` links more than five distinct notes. The cap bound on the majority
of the corpus, so the exemption's precondition — that the representation check
actually runs — was false for most notes.

A third force is auditability. A verdict resting on fourteen opened artifacts
costs as much to audit as it cost to produce, so it is trusted rather than
re-checked, and Commonplace's own measurement of verdict instability on
unchanged input is why re-checking is worth paying for.

Quote verification carried a related gap. A span marked verbatim was resolved
against the whole linked file, so a quotation aimed at a tracked ingest could
be satisfied by that ingest's analytical prose, which ADR 073 holds is not
source support.

## Decision

This adopts the proposal *Atomic-step grounding bounds unquoted sources per
note*.

1. **Grounding is bounded on the artifact, not the review.** A note may cite at
   most **five** distinct tracked sources (`kb/sources/*.ingest.md`) without a
   verified verbatim quotation paired to each. A source the note quotes
   verbatim is discharged and does not count. A source linked with `(snapshot
   required)` anywhere in the note always counts: the marker attaches per
   source rather than per link, because one such use already forces the
   reviewer to open the snapshot. Links to other notes and to other library
   artifacts never count. A linked note has passed its own grounding review,
   and the citing note owes it representation, not re-grounding.
2. **Enforcement is a `commonplace-validate` type rule on notes, severity
   FAIL.** It shipped as WARN while the eight notes then over the bound were
   conformed and the two authoring conventions named below were written into
   the notes collection contract; both were done the same day, and the rule
   fails from then on.
3. **Quote verification is confined for ingest targets.** A verbatim quotation
   aimed at an `*.ingest.md` must occur in that ingest's `## Quotes` section,
   not anywhere in the file. Otherwise the exemption could be earned by quoting
   the half of the ingest that is not source support. A quotation that wraps
   across source lines inside one paragraph is now recognised; before this
   decision such spans were never verified at all, and an unverified span does
   not discharge a source.
4. **The three link-following criteria lose their reader-side caps.**
   `semantic/grounding-alignment` drops the sixteen-artifact budget and its
   disclosure clause. It reads a linked library artifact head-first for
   representation — title and opening paragraph, and the target's own treatment
   of a concept only when the invoked claim is an interior concept the note
   does not quote. It judges quoted sources on the note's page and keeps the
   two existing routes for unquoted sources. `sentence/misleading-link-text`
   checks every link and `sentence/concept-attribution` every identity claim,
   under that same head-first rule. A head check needs no N, because
   auditability — the reason N exists — is trivially satisfied when a second
   checker can redo the step from the same heads. The paraphrased-interior case
   in concept attribution remains a finding-step outside the artifact-side
   bound. It is tolerated because the sentence shape is rare, no note carrying
   more than four such claims, with quote-or-title as the author-side remedy if
   it stops being rare.
5. **Five is a convention chosen for auditability, not a measured degradation
   point.** What a small step buys is that a second checker, including a
   person, can redo the grounding step from the note's own page; the uncapped
   arm of the paired experiment read twenty-two artifacts with no observed
   loss, so the number is not a reviewer capacity. Five was selected because
   the eight-note trial reached it from already-retained quotes in every case,
   at 2–3% word growth, with no split, no snapshot escape, and no new grounding
   run. Three would put eighteen notes over.

The operativity path has two channels. `commonplace-validate` consumes the
count deterministically on every validation run, with warn force that does not
fail the process. The three hashed criteria consume the reading rules as
binding judgment instruction inside review prompts; changing them stales their
populations once through ordinary criterion freshness.

## Considered alternatives

**Keep the sixteen-artifact budget.** It is calibrated to a corpus statistic,
carries the silent-lag failure mode, and leaves a passing verdict unauditable
because redoing it costs what producing it cost.

**Price reviewer attention by count and bytes, computed by a sizing command.**
The proposal *Review link budget prices reviewer attention* restates the
inherited-number problem in a more elaborate form, since nothing identifies the
exchange rate between artifact-switching and bytes read. The assay that would
calibrate it becomes unnecessary once the artifact fits by construction.

**Assemble the evidence pack in code and split the review.** The proposal
*Exceeding a review budget splits the task* and the review-attention-price
workshop's Mechanism B both partition an over-budget review. Partitioning
severs joint support, so a claim carried by several sources together fails in
fragments a whole pass would pass, and the routes need partial-coverage and
combination semantics the review model does not have.

**N = 3.** Rejected: it would put eighteen notes over the bound, against eight
at five, without a corresponding gain in what a second checker can redo.

**WARN indefinitely.** Rejected: a bound that only warns is a visible
pressure, not a contract, and the trial showed conformance is cheap. WARN was
kept only until the eight over-bound notes were conformed, because two of them
cited sources only from a trailer or a table cell, where there was no hosting
sentence for a quotation.

**Per-link `(snapshot required)` semantics.** Rejected because a source could
then be both discharged by a quotation at one link and snapshot-required at
another, which contradicts the cost the bound counts — artifacts the reviewer
must open.

**A `synthesis`-trait exemption for casebook notes.** Deferred rather than
rejected. The two joint casebooks are the strongest candidates, but both
conform numerically, so nothing yet forces the exemption.

**Keep the two representation caps.** Rejected because they bind on 55% of
notes, leaving the majority of the corpus only partly checked and making the
note-link exemption's precondition false.

Free choices resolved: the two authoring conventions — that a source cited as
evidence is cited in the body rather than only in the trailer, and that a
casebook table hosts its retained evidence in an accompanying prose block —
live in the notes collection contract. `kb/articles/` shares the same N
(resolved 2026-08-29): both live articles sat at two and three unquoted
sources, so the rule bound on nothing, and the articles contract admits the
`verbatim` marker inside a citation parenthesis so an article has the same
discharge route as a note. Nothing is left open.

## Consequences

Grounding verdicts become auditable from the note's page: the passages that
carry a claim are on it, and a second checker can redo the support judgment
without opening the sources. The reviewer caps no longer need recalibration as
the corpus grows, and the note-link exemption makes note-dense notes cheap to
review rather than expensive.

Authors pay what the review used to absorb. A note over the bound must quote or
split, and every quoted passage lengthens the note, so the remedy spends
against the co-loading bound. The eight notes over the bound at adoption were
conformed from already-retained quotes at 2–10% word growth.

Two risks stay. Occurrence is not representativeness: a validated quotation
establishes that the words appear in the source, not that they mean there what
the note uses them for, so a passage that reads as lifted from a qualifying
context still costs a trip to the source. And an ingest whose retained quotes
are paraphrase would discharge the bound falsely; one such ingest has been
found and needs a fresh grounding run.

A review-side budget is no longer available as the mechanism that protects
reviewer attention. ADR 079 is superseded. The review-attention-price workshop
closes; link and usage telemetry remains a measurement of review cost, not a
cap.

Where the decision stops applying: it covers `kb/notes/` under Commonplace's
grounding gate, in a system where verbatim quotations are mechanically
validated against their cited source. Another check would have to re-derive its
own unit of cost before any count transferred to it. Five is not a capacity
claim about other corpora, gates, or models, and the conformance trial that
selected it measured eight notes on one date.

---

Relevant Notes:

- [A note is an atomic step relative to the check that reads it](../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — rests-on: supplies the artifact-side placement, the unquoted source as the grounding check's unit, and what kind of number N is
- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — rests-on: supplies the note-link exemption and the preconditions the uncapped representation criteria make true
- [A five-link cap missed four grounding findings in twelve reviews](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidenced-by: the paired outcomes, the uncapped arm's twenty-two-artifact reading, and the misattribution FAIL no count catches
- [Grounding alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md) — procedure: carries the three reading routes and the removal of the artifact budget
- [Misleading link text gate](../../instructions/review-gates/sentence/misleading-link-text.md) — procedure: carries the every-link head check
- [Concept attribution gate](../../instructions/review-gates/sentence/concept-attribution.md) — procedure: carries the every-identity-claim head-first ladder and the tolerated paraphrased-interior case
- [079-Grounding reviews budget sixteen distinct linked artifacts](./079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — supersedes: the review-side ceiling this decision replaces
- [046-Verbatim quotes are validated against their cited source](./046-verbatim-quotes-are-validated-against-their-cited-source.md) — see-also: the validator that moves the finding step into code and lets a quoted source be discharged
- [073-Untracked source snapshots require ingest grounding](./073-untracked-source-snapshots-require-ingest-grounding.md) — see-also: the rule that an ingest's analysis is not source support, which the `## Quotes` confinement enforces
