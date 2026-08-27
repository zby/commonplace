---
description: "Proposal: move the grounding reading limit from the review to the note — a note may cite at most N sources a reviewer must open and search, with validated inline quotes and note links exempt"
type: ../types/design-proposal.md
tags: []
---

# Atomic-step grounding bounds unquoted sources per note

Commonplace currently places its grounding reading limit on the review. The
`semantic/grounding-alignment` criterion lets a pass inspect at most sixteen
distinct linked artifacts, and sixteen was chosen because it is the corpus p90
offer ([ADR 079](../adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md)).
Two costs follow from that placement. The number is calibrated to a corpus, so
it has to be recalibrated whenever the corpus's evidence needs move. And when it
lags, the failure is silent: a reviewer that stops at its limit and returns a
pass is indistinguishable, from the outside, from one that read everything and
returned a pass. Disclosure conventions report where the budget stopped, not
whether a finding was sitting behind it.

The option this proposal describes is the other placement of the same
constraint. **Bound the artifact instead: a note may cite at most N sources that
a reviewer must open and search.** A source quoted inline, where the quotation
is resolved against the linked file by the validator
([ADR 046](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)),
does not count against N, because the finding step has moved into code and what
is left for the reviewer is a bounded judgment over a passage already on the
page. Links to other notes do not count either, because a claim-titled note
arrives with its own grounding already discharged.

Both exemptions are load-bearing and neither is asserted here: they are the
transferable claims this proposal rests on, cited below.

## Current state (as of 2026-08-27)

- ADR 079 is in force. `semantic/grounding-alignment`
  ([gate text](../../instructions/review-gates/semantic/grounding-alignment.md))
  budgets sixteen distinct linked artifacts per pass, counts a repeated target
  once, and treats reaching the limit as disclosure rather than failure.
- `sentence/concept-attribution` and `sentence/misleading-link-text` each read
  at most five distinct target notes per review. Those numbers are inherited
  constants, unchanged by ADR 079.
- `commonplace-validate` resolves a quotation marked as such against the whole
  linked file by normalized substring containment
  (`src/commonplace/lib/quote_verification.py`, `verify_content`), pairing each
  quoted span with the nearest link in its paragraph.
- Tracked ingests hold retained quotes in a `## Quotes` section validated
  against the pinned snapshot; analysis elsewhere in an ingest is not source
  support ([ADR 073](../adr/073-untracked-source-snapshots-require-ingest-grounding.md)).
- Corpus measurement over `kb/notes/`: 344 notes, of which 256 link no ingest at
  all, 18 link more than three, and 8 link more than five (maximum 9). The eight
  are single-claim notes:
  `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` (9),
  `knowledge-storage-does-not-imply-contextual-activation` (8),
  `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` (7),
  `evidence/real-self-improving-systems-occupy-combinations-no-rung-captures` (7),
  `a-proposal-selection-loop-requires-search-evaluation-and-retention` (6),
  `evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces` (6),
  `instantiation-alone-cannot-model-agent-learning-across-sessions` (6),
  `formal-systems-assess-explanatory-reach-through-causal-and-proof` (6).
- The comparable count over distinct linked artifacts of every kind has a median
  of seven across 337 measured targets, which is why the source-counting unit
  and the artifact-counting unit are not interchangeable at any N near five.

## What the bound would count

The unit is the **unquoted source**: an artifact the reviewer must open and
search to find the passage that carries the claim. Three consequences fix the
count.

- A source with a validated inline quotation is discharged. The reviewer still
  judges whether the passage supports the claim, but that judgment reads the
  note's own page.
- A linked note is charged to the representation criteria
  (`sentence/concept-attribution`, `sentence/misleading-link-text`) rather than
  to grounding, so it does not consume N.
- A source used through the `(snapshot required)` route has no bounded passage
  by construction, so nothing about it can be discharged by quoting.

## Candidate mechanism

The binding consumer would be `commonplace-validate`: for each note, count the
distinct `kb/sources/*.ingest.md` targets that carry no accompanying verified
inline quotation, and signal when that count exceeds N.

One tightening is required rather than optional. `verify_content` currently
matches a quoted span against the whole linked file, so a span aimed at an
ingest can satisfy the check against the ingest's analytical prose. ADR 073
holds that an ingest's analysis is not source support, so for ingest targets the
match must be confined to the `## Quotes` section. Without that change the
exemption can be earned by quoting the wrong half of the ingest.

## Forces

**For the artifact-side placement.** A conforming note fits by construction, so
the reviewer's limit never binds on it and the silent-lag failure mode does not
arise. The number stops tracking a corpus statistic. And the verdict becomes
auditable: a grounding result resting on three sources and their quoted passages
can be re-checked from the same page by a second checker, including a person,
whereas one resting on fourteen artifacts costs as much to audit as it cost to
produce.

**Against.** The bound puts work on authors that the review currently absorbs,
and it lands hardest on exactly the notes that are doing the most: the eight
above are single-claim notes whose claim is established by reading six or more
sources together. Whether they can be quoted or split without losing the claim
is not known, and is the evidence this proposal needs.

**The cost the review-side placement avoids.** Some claims rest on the structure
of a whole argument, on what a source does not say, or on material distributed
across a document. Those cannot be carried by a bounded passage. Under an
artifact-side bound they are pushed toward the snapshot route or toward
fragmentation, and the bound offers them no relief.

**Bytes stay unbounded either way.** N counts artifacts, and a single
`(snapshot required)` source can be very large. Nothing here prices bytes.

## Free choices

- **N.** Candidates: five, matching the original grounding cap; three, matching
  the corpus shoulder where 18 notes sit; or a number chosen as a stated
  convention. The theory this rests on fixes the *kind* of number rather than
  the value — N is a convention chosen so a second checker can redo the step,
  not a point at which reviewer performance degrades — so the choice is a
  commitment about auditability, not a measurement.
- **Fail or warn.** Failing makes the bound a hard authoring contract; warning
  makes it a visible pressure that leaves the eight notes publishable while the
  corpus adapts.
- **`(snapshot required)` sources.** They may count as one each against N, or be
  disallowed once N is reached, on the grounds that a note needing several whole
  sources at once is the case the bound exists to catch.
- **Articles.** `kb/articles/` cites many sources by nature and is not reviewed
  by the same gate. Articles may get their own N, or be exempt.
- **The representation criteria's own limits.** The note-link exemption leaves
  the five-target limits in `sentence/concept-attribution` and
  `sentence/misleading-link-text` untouched. Whether those also want an
  artifact-side bound is open and not decided by adopting this one.

## Interactions with existing decisions

**ADR 079 stands.** The review-side budget is not repealed by this option; it
becomes a ceiling that never binds on a conforming note. A non-conforming note —
one written before adoption, or one exempted — still gets a bounded review with
disclosure. The two placements are compatible; what changes is which one
normally decides.

**The joint-support hazard is avoided rather than solved.**
[Exceeding a review budget splits the task](./exceeding-a-review-budget-splits-the-task.md)
identified that partitioning a review by link severs claims whose support spans
several sources, so any partition would have to be by claim. Under an
artifact-side bound the author, who knows which passages jointly carry the
claim, quotes them onto one page and the check reads them together. The
partition problem does not arise because nothing is partitioned; the hazard is
sidestepped, not answered.

**ADR 078 is not contradicted.**
[ADR 078](../adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md)
rejected evidence living in the target artifact and kept the ingest `## Quotes`
pool as the evidence owner. An inline quotation is not a second evidence store:
it is a checked copy of a quote the ingest already retains, admissible exactly
because a validator re-derives it and fails on mismatch — the general rule that
[a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
The ingest remains the owner, and the required `## Quotes` tightening above is
what keeps that true.

## Operativity and warrant

The operativity path is the validator. `commonplace-validate` is the binding
consumer, and its force is a build-time check on the note rather than a judgment
instruction. `cp-skill-write` and `cp-skill-write-multistage` would need to know
the rule at write time so a note is authored inside N rather than repaired after
it; both already invoke `cp-skill-ground` at the point where quotes are
retained (ADR 078), which is the same place. The grounding gate text itself is
unchanged by this option.

What warrants the oracle: the substring test establishes that the words occur in
the linked source, and nothing more. It does not establish that the passage
means there what the note uses it for, or that it is representative of the
source. That semantic half stays with the grounding reviewer, whose limit still
applies. The bound therefore reduces what the reviewer must open; it does not
reduce what the reviewer must judge.

## Adoption criteria

This is the third mechanism candidate for the open review-attention-price
question, alongside the reviewer spending a priced budget and code assembling
the evidence pack to a pass size. Adopt when that question is decided in this
option's favour.

The evidence to gather first is narrow: whether the eight notes above can be
quoted or split without loss of the claim each makes. A bounded trial on those
eight settles the force that most argues against this option, and it can be run
without touching any production criterion.

---

Relevant Notes:

- [A note is an atomic step relative to the check that reads it](../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — rests-on: supplies the artifact-side placement, the unquoted source as the grounding check's unit, and what kind of number N is
- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — rests-on: supplies the note-link exemption without which the bound would put over half the corpus in violation
- [Exceeding a review budget splits the task](./exceeding-a-review-budget-splits-the-task.md) — compares-with: the review-side answer to the same over-budget case, whose joint-support hazard this option sidesteps
- [079-Grounding reviews budget sixteen distinct linked artifacts](../adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — evidenced-by: the interim ceiling and the corpus measurement this option would leave in place as a non-binding ceiling
- [Grounding alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md) — procedure: the criterion that carries the review-side budget today and would be unchanged
