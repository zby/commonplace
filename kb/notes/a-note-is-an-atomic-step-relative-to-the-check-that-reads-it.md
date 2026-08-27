---
description: "Two independent bounds on a note: one claim sized to the reader's bounded context, and one checkable inference sized to the checker's single pass — for the grounding check the unit is the unquoted source"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [kb-maintenance, evaluation]
---

# A note is an atomic step relative to the check that reads it

A knowledge base written and reviewed by agents bounds note size twice, for two
reasons that have nothing to do with each other.

The first bound is co-loading. [Short composable notes maximize combinatorial
discovery](./short-composable-notes-maximize-combinatorial-discovery.md)
because a model's context is finite, so the number of notes that fit in it
together sets the surface area for recognizing shared structure. One claim per
note, sized to the reader's context.

The second bound is checking. A note is an **atomic step** when the claim, the
material it cites, and the inference from that material to the claim can be
checked in one pass by the check that will be applied to it. One checkable
inference, sized to the checker's pass.

These are different quantities set by different mechanisms, and a note can
satisfy one and fail the other. "Fits one pass" also has no content until the
pass is named: a step is atomic relative to a particular check, which is an
instance of the general rule that [warranted autonomy is bounded by oracle
domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — a checker's
domain is the range of candidates it can assess with the required confidence,
and [the boundary of automation is the boundary of
verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).
The same note may be one step for a check that judges whether quoted passages
support a claim and several steps for a check that judges whether an inference
across all of them holds. This note states the rule for one check, Commonplace's
grounding check, because that is where the unit of cost is clear; the same
argument would need its own unit for any other check.

## Placing the bound on the artifact rather than the review

The alternative placement is a reading budget on the review: let notes be as
large as they are, and calibrate how much the reviewer may open. The two
placements differ in their failure mode, not in the constraint they express.

A review-side budget has to be recalibrated whenever the corpus's evidence needs
move, and its failure when it lags is silent. A reviewer that stops at its limit
and returns a pass is indistinguishable, from the outside, from one that read
everything and returned a pass. Disclosure conventions reduce this — a reviewer
can name what it left unread — but disclosure reports the budget's boundary, not
whether a finding was sitting behind it.

An artifact-side bound does not have that failure mode, because a conforming
artifact fits by construction: the bound is held by a validator that fails the
note, not by a reviewer that stops reading. The reviewer's limit still exists;
on a conforming note it never binds.

## Mechanism: for the grounding check, the unit is the unquoted source

The grounding check asks whether the material a note cites supports the claim it
is cited for. Its cost is not links, and not bytes: it is the number of
artifacts in which the reviewer must *find* the passage that carries the claim
and then judge whether it does. A source that has been quoted verbatim is not
one of them.

The reason is that Commonplace has moved that finding step into code. A
quotation marked `verbatim` is resolved by substring match against the file it
links, and a mismatch fails the note before any reviewer opens anything ([ADR
046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md));
the source-side material is itself held as retained quotes validated against the
captured source ([ADR
073](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)).
This is the general rule that [a derived copy of recomputable truth must be
checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
applied to citation: the quote is a copy of something held elsewhere, and it is
admissible because a validator re-derives it and fails on mismatch. A paraphrase
has no such derivation rule, and [a citation cannot assert more fidelity than
its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)
— a passage never captured word for word cannot be quoted into this route
without returning to the source.

What is left for the reviewer after the quote is a bounded judgment: does *this
passage* support *this claim*. It costs attention, and nine quoted passages cost
more than one, but the cost is set by the author's choice of passage length and
requires opening nothing.

Two limits follow, and both are prices already paid elsewhere in the system.
Occurrence is not representativeness: the validator establishes that the words
appear in the source, not that they mean there what the note uses them for, and
a reader who suspects a passage was lifted out of a qualifying context has to
open the source after all. And some claims cannot be carried by a bounded
passage — claims resting on the structure of a whole argument, on what a source
does not say, or on material distributed across a document. Commonplace marks
those uses `(snapshot required)`; such a source has no bounded passage and
counts fully against the step.

A consequence worth stating, because it answers the obvious objection to
bounding the artifact: a claim supported *jointly* by several sources, none
sufficient alone, should be quoted rather than split. Splitting it across notes
severs the support, so each fragment fails a check the whole would pass — the
hazard a review-side [proposal to split an over-budget review into covering
passes](../reference/proposals/exceeding-a-review-budget-splits-the-task.md)
identified when it concluded that any partition would have to be by claim rather
than by link. Under an artifact-side bound the author, who knows which passages
jointly carry the claim, puts them on the page together and the check reads them
together. This is where the two bounds meet: every quoted passage lengthens the
note, so quoting spends against the co-loading bound. The bounds are independent
as constraints but coupled through this remedy. A claim whose joint support
cannot be quoted within a note the reader can still co-load has only the
snapshot route or a split left, and the split has to be by claim, so that each
fragment states what it establishes. Links to other notes are also not sources in this sense, because a
linked note carries its own claim title and its own grounding review; [a
linked note discharges its own grounding, so a citing note owes it
representation, not re-grounding](./a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md).

## The two bounds come apart in the corpus

Across 344 notes in `kb/notes/` as of 2026-08-27, eight cite more than five
distinct sources, the largest citing nine. All eight are single-claim notes: one
proposition, established or bounded by reading six or more sources together.
They satisfy the co-loading bound on any reading of it. They are not atomic
steps for the grounding check, because checking one means opening six to nine
artifacts and finding the claimed support in each. The converse case is
available in principle — two independent claims, each grounded in one quoted
passage, is one step for the grounding check and two notes under the co-loading
bound.

The strongest evidence Commonplace holds about grounding-review reading limits
reads differently under this placement. A paired experiment reviewed the same
twelve notes under a five-link instruction and an uncapped one; [four findings
appeared only in the uncapped
arm](./evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md),
after the reviewer had opened six, eleven, fourteen and sixteen artifacts. Read
as a fact about reviewers, this says five is too few. Read as a fact about
notes, it says the reviewer honoured its cap and the notes had put their support
beyond it — which is the behaviour an artifact-side bound depends on, and under
such a bound the four notes would have had to split or quote before review. Two
of the four findings sharpen the reading: one was missing retained support for
details attributed to a source, and one was an ingest's analytical prose treated
as evidence beyond its retained quotes. Both are absences of a retained passage,
and an absence of that kind is a validator's result rather than a reviewer's
finding. Had the details been quoted, either the quote would match or the note
would have failed validation before review began.

## What kind of number a step size is

The bound does not fix its own N, but it does fix what kind of number N is,
because three candidates are available and they justify different values.

N is not the point at which reviewer performance degrades. In the same
experiment, uncapped reviewers read up to twenty-two artifacts and 322 kilobytes
in one pass with no observed loss, and the three notes offering the most
material all passed. Whatever a small step protects, on this evidence it is not
a reviewer capacity exhausted at current corpus sizes. Nor is N the smallest
count at which no miss happened to be observed; that number moves with every
experiment and inherits its sample.

N is a convention, chosen so that a second checker — including a person — can
redo the step. This is what a small step buys that a well-calibrated reviewer
budget does not. A verdict resting on fourteen artifacts costs as much to audit
as it cost to produce, so in practice it is trusted rather than audited; a
verdict resting on three sources and six quoted passages can be re-checked from
the same page. What the page re-checks is the support judgment — that these
passages carry this claim; whether a passage was lifted out of a qualifying
context still costs a trip to the source, so the audit the bound buys is of the
step the validator did not do, not of the one it cannot. The value is not that
the reviewer copes, but that the review
becomes auditable — and Commonplace's own measurement that language-model
verdicts disagree with themselves on unchanged input is the reason auditability
is worth paying for.

Sizing a step to its checker rather than to the material is old. Descartes'
second precept of method was "to divide each of the difficulties under
examination into as many parts as possible, and as might be necessary for its
adequate solution" ([*Discourse on the Method*, Part
II](../sources/descartes-discourse-on-the-method.ingest.md), verbatim, Veitch's
translation). What he claimed for such division was the reliability of long
chains: "The long chains of simple and easy reasonings by means of which
geometers are accustomed to reach the conclusions of their most difficult
demonstrations" ([Part
II](../sources/descartes-discourse-on-the-method.ingest.md), verbatim) had
persuaded him that anything within reach of knowledge could be reached that way.
The parts are sized to the solution, and the chain is trusted because each link
is simple enough to be evident.

Lamport makes the checker explicit. Asked how much detail a proof step needs, he
answers that when the proof is written to convince someone else "the answer
depends on the sophistication of the reader" ([*How to Write a 21st Century
Proof*, section
3](../sources/lamport-how-to-write-a-21st-century-proof.ingest.md), verbatim).
Written for oneself, the test is different: "if the truth of a statement is not
completely obvious, or if you suspect that there may be just the slightest
possibility that it is not correct, then more detail is needed" ([section
3](../sources/lamport-how-to-write-a-21st-century-proof.ingest.md), verbatim).
That is step size stated relative to whoever checks the step. His assessment of
what the structure delivers is measured: "Structured proofs make it possible,
not inevitable" ([section
5](../sources/lamport-how-to-write-a-21st-century-proof.ingest.md), verbatim).
The same modesty applies here — a bounded check does not catch every error, but
an unbounded one cannot be redone. Both precedents concern human checkers
reading mathematical arguments, so the transfer to agent-reviewed notes is an
analogy about checker-relative sizing, not evidence that any particular N
carries over. What the knowledge-base case adds is a validator that turns the
commonest kind of step — *this passage says this* — into a check that costs the
reviewer nothing.

## Scope

- Stated for Commonplace's grounding check. The relativity claim is general;
  the unit — the unquoted source — is derived from that check's cost structure
  and would have to be re-derived for any other check.
- Depends on a system where verbatim quotations are mechanically validated
  against their cited source. Without that validator, quoting moves work around
  rather than discharging it.
- Does not decide N, a validator rule that would enforce it, or the fate of the
  review-side budget currently in force. Those are operational decisions with
  their own evidence requirements.
- The corpus counts and the paired experiment are bounded local reports about
  one knowledge base at one time; they show the two bounds are independent
  here, not how often they diverge elsewhere.

## Open Questions

- Is the check that a citing note represents a linked note's claim faithfully
  itself well bounded, or is it where the same problem reappears in smaller
  form? One of the four findings was a broader mechanism attributed to a link
  that disclaims it, which no count would catch.
- Does the artifact-side bound have a cost the review-side one avoids — claims
  that are genuinely one inference over many sources and cannot be quoted into
  bounded passages, which would be pushed toward the snapshot route or toward
  fragmentation?

---

Relevant Notes:

- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](./a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — grounds: the premise that links to other notes are not sources for the grounding step, which the source-counting unit relies on
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — contrasts: the co-loading bound sized to the reader's context, against the checking bound sized to the checker's pass
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the premise that a check's domain is what makes "atomic relative to a check" a real restriction
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the general form of the dependence between what can run unattended and what can be checked
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: why a validated quote may be trusted as a copy while a paraphrase may not
- [A citation cannot assert more fidelity than its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — grounds: the capture-time bound that decides which sources can take the quoting route at all
- [Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — enables: the convention that lets a chain of notes read as a chain of checked steps
- [A five-link cap missed four grounding findings in twelve reviews](./evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidenced-by: the paired outcomes this note rereads as evidence about note size rather than reviewer capacity
- [ADR 079 — Grounding reviews budget sixteen distinct linked artifacts](../reference/adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — see-also: the review-side placement of the same constraint, currently in force
- [Exceeding a review budget splits the task](../reference/proposals/exceeding-a-review-budget-splits-the-task.md) — see-also: the splitting hazard for jointly supported claims, which quoting answers
- [Descartes, *Discourse on the Method*](../sources/descartes-discourse-on-the-method.ingest.md) — evidenced-by: the second precept sizes the parts to the solution and rests long chains on simple links
- [Lamport, *How to Write a 21st Century Proof*](../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) — evidenced-by: proof-step detail is set by the reader who checks it, and structured proofs make error-finding possible rather than inevitable
