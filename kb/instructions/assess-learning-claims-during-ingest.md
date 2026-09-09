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

Read [Theory refinement](../notes/definitions/theory-refinement.md) as the
current comparison basis. The definition is loaded at execution rather than
frontloaded here because it is new and expected to change often; do not copy
its content into this instruction. The definition governs our use of the term
but remains open to challenge by the source.

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
3. Choose the analytical distinctions that matter for this source and the
   KB's goals. Where relevant, the current account distinguishes using a
   theory from revising it.
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
