---
description: Use during ingest drafting when a source's subject or mechanism is learning or adaptation, to write the Learning Claims section that judges what the source changes in our understanding.
type: kb/types/instruction.md
---

# Assess learning claims during ingest

Write the `Learning Claims (our opinion)` section of an ingest report so a
later reader can judge what the source changes in our understanding of
learning and adaptation: how its mechanism works, what the evidence supports,
and whether it strengthens, limits, or challenges Commonplace's current
account. Preserve surprising mechanisms and distinctions even when our
vocabulary does not yet accommodate them.

Use this instruction within `draft-ingest-report.md` when the source's
subject or mechanism is learning or adaptation, including a conceptual
account with no empirical results. Keep the caller's source boundary, output
contract, and occasion rules. This branch adds exactly one report section,
placed after `Connections Found` under the ingest-report type contract, with
its paired `learning_claims: true` frontmatter field, and does not authorize
further source collection.

Read [Theory builder](../notes/definitions/theory-builder.md) as the
current comparison basis for the source's system. When fine-grained
localization or selective repair matters, also read
[Addressable theory](../notes/definitions/addressable-theory.md). Load these
definitions at execution rather than copying their content into this
instruction. They govern our use of the terms but remain open to challenge
by the source.

Read [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
for the boundary between improvement within an effective update space and
evidence for choices fixed outside it.

Write for a reader already acquainted with Commonplace's vocabulary. Use our
established terms without reteaching them; explain unfamiliar source terms
and consequential differences in meaning.

Procedure:

1. Establish the source's mechanism on its own terms, before mapping it.
2. Relate its important ideas to Commonplace concepts. Make the mapping
   explicit, so the reader can see what the source adds to, supports, or puts
   in question in the current account. Where a mapping is partial or no
   concept fits, explain the difference using the nearest relevant
   distinction without forcing equivalence. Distinguish our interpretation
   from the source's claims.
3. Judge the source's system against the theory-builder definition
   condition by condition: localized content, consumption, content-directed
   criticism, and iteration. Give each condition its own evidence strength
   and do not infer one from another. Iteration counts when the result of
   criticism is kept and shapes the next conjecture, including rounds within
   one run. Record separately how far results persist (within an episode, a
   run, across runs, or across problems); persistence is graded, not a
   condition. Judge learning, meaning improved
   capacity for future action, as a separate claim: meeting the conditions
   does not establish it, and failing one does not rule out other
   improvement. Choose the further analytical distinctions that matter for
   this source and the KB's goals. Where relevant, the current account
   distinguishes using a theory from revising it.
   When they affect the learning judgment, identify the signals and histories
   available to the learner, the operations it can compose, the mappings its
   hypothesis class can express, and the representations or partitions fixed
   outside its effective update space. Separate improvement within that space
   from evidence for the fixed decomposition. Include only distinctions that
   affect interpretation or reuse.
4. Keep each conclusion at the strength of its evidence. A plausible
   mechanism, an observed improvement, and evidence that the mechanism caused
   the improvement support different judgments. Missing evidence leaves a
   question open; it does not establish absence.
5. Write the section and set `learning_claims: true` in frontmatter. It is sufficient when it makes the source's
   contribution, its relation to our concepts, and its evidential limits
   clear, including any reason to revise our concepts. Include only
   distinctions that change that judgment. Leave unresolved mappings explicit
   rather than forcing a classification or repairing the KB's theory during
   ingest.

---

Relevant Notes:

- [Theory builder](../notes/definitions/theory-builder.md) — rests-on: the four conditions judged one by one, with learning as a separate claim
- [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — rests-on: learning assessments distinguish improvements within an effective update space from evidence for choices fixed outside it
