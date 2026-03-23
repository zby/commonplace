=== PROSE REVIEW: distilled-artifacts-need-source-tracking-at-the-source.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that source tracking belongs at the source, not the target. The "Source-side tracking" section (the load-bearing section that explains the mechanism and the practical convention) is roughly equal in length to the opening paragraphs that motivate it. However, the "Two audiences, one link direction" section — a table that restates the same idea in a different format — adds little beyond what "Source-side tracking" already establishes. The note's real weight is in the convention ("Distilled into:" at the source footer) and the maintenance scenario it enables, but proportionally neither gets deeper treatment than the motivating setup.
  Recommendation: Consider whether the table section could be folded into a sentence or two within "Source-side tracking," freeing space to develop the convention further — e.g., what happens when a source feeds many targets, or when the distillation is partial rather than wholesale.

INFO:
- [Redundant restatement] The final sentence of the note ("Staleness detection flows in the direction of change: source changes -> maintainer sees downstream targets -> reviews them") restates the mechanism already described in "Source-side tracking" ("you're editing a methodology note, you see 'Distilled into: WRITING.md', you know to check whether WRITING.md needs updating"). The restatement is compact enough that it functions as a summary rather than dead weight, but it is doing the same work twice.

CLEAN:
- [Source residue] The note claims to be about distillation and source tracking within a knowledge base. All examples — WRITING.md, methodology notes, conventions, instructions — are native to this domain. No leaked framing from an unrelated source domain.
- [Pseudo-formalism] No formal notation or symbolic apparatus is present. The table in "Two audiences, one link direction" is presentational, not pseudo-formal.
- [Confidence miscalibration] The note presents a convention (the "Distilled into:" footer pattern) and a design rationale. Both are framed as design choices, not empirical findings. Assertions like "The dependency link belongs at the source, not the target" are stated directly, which is appropriate since this is a design note arguing for a convention, not reporting external evidence. The claim "The KB is small enough that grep is the query engine" is correctly scoped as a current-state observation.
- [Orphan references] No specific figures, data points, percentages, or named studies appear. All claims are about this KB's design.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. The note stays within its own domain (knowledge-base maintenance).
- [Anthropomorphic framing] The note discusses artifacts and maintainers, not models. Language like "it doesn't know its sources" (in the table) is applied to the distilled artifact, not to an LLM, and reads as shorthand for "contains no record of its sources" — acceptable in context and unlikely to mislead.

Overall: 1 warning, 1 info
===
