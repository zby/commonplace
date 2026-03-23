=== SEMANTIC REVIEW: two-context-boundaries-govern-collection-operations.md ===

Claims identified: 14

1. [Enumeration] Two operations justify areas: orientation and comparative reading (intro, attributed to areas note)
2. [Causal] The two operations have different minimum resolution requirements (intro)
3. [Definition] The full-text boundary is the point where all note bodies can be loaded together (~40 notes per WRITING.md) (section "The two boundaries")
4. [Definition] The index boundary is the point where all titles+descriptions can be loaded together (section "The two boundaries")
5. [Causal] The full-text boundary may not move with growing context windows because complexity costs limit useful simultaneous reasoning (section "The two boundaries")
6. [Scope] The two boundaries create exactly three operational regimes (section "Three operational regimes")
7. [Causal] Below the full-text boundary, both operations work at full power (regime 1)
8. [Causal] Between the two boundaries, orientation works but comparative reading must be partitioned (regime 2)
9. [Causal] Above the index boundary, even the index stops fitting productively (regime 3)
10. [Causal] Descriptions become load-bearing in the middle regime — they are "the only content that participates in index-level operations" (section "Descriptions become load-bearing")
11. [Scope] "the only content that participates in index-level operations" (section "Descriptions become load-bearing")
12. [Causal] Parent areas operate at index resolution; child areas operate at full-text resolution (section "Parent/child area relationships")
13. [Causal] /connect works by reading the full index.md in one pass — built on the index boundary (section "Library/workshop separation")
14. [Causal] Library/workshop separation is an operational necessity to keep the main collection below the index boundary (section "Library/workshop separation")

WARN:
- [Grounding alignment] The note states "WRITING.md sets this at ~40 notes" for the full-text boundary. WRITING.md does not contain a 40-note threshold or any numeric split threshold. The areas note also references "the [split threshold of ~40 notes](../instructions/WRITING.md)" but WRITING.md has no such number. The ~40 figure may have been removed from WRITING.md in a later edit, or it may have been inferred rather than stated. Either way, the attribution is currently inaccurate — the note claims a source that does not contain the claimed content.

- [Completeness] The note claims exactly "three operational regimes" created by the two boundaries. Boundary case: what happens *at* a boundary rather than below, between, or above? A collection of exactly 40 notes (at the full-text boundary itself) is ambiguously in regime 1 or regime 2 — the note treats boundaries as sharp thresholds but also acknowledges they depend on "note length, instruction overhead, and how much reasoning space the operation needs," making them fuzzy zones rather than clean lines. A fuzzy boundary creates a transitional zone that doesn't cleanly map to any of the three regimes. This is INFO-level because the note partially acknowledges the fuzziness ("the actual threshold depends on...") but the three-regime framework treats the boundaries as discrete separators.

- [Grounding alignment / domain coverage] The note cites the context-efficiency note as "foundation: context scarcity is why the boundaries exist; the volume/complexity distinction explains why the full-text boundary may not move with growing windows." The context-efficiency note does discuss volume vs. complexity and argues that growing windows address volume but not complexity. However, the specific claim that "the full-text boundary may not move" is the reviewed note's own inference — the context-efficiency note argues that complexity costs persist despite larger windows, but it doesn't discuss collection-level boundaries or the specific threshold at which multiple note bodies can be loaded together. The inference is plausible but the link text ("the volume/complexity distinction explains why") suggests the source directly addresses this, when it doesn't.

INFO:
- [Completeness] Boundary case: a collection where notes vary wildly in length. Some notes are 100 words, others 3000 words. The full-text boundary isn't a fixed note count — it's a token budget. A collection of 80 short notes might be below the full-text boundary, while a collection of 20 long notes might be above it. The note acknowledges this ("the actual threshold depends on note length") but the three-regime framework is presented in terms of collection membership (all notes in a collection are in one regime), which assumes rough homogeneity of note length. A heterogeneous collection might have some notes that could all be loaded together and others that can't, creating sub-collections in different regimes simultaneously.

- [Completeness] Boundary case: selective loading. The note frames the middle regime as requiring "partitioned sub-passes" for comparative reading. But an agent could also do selective comparative reading — loading, say, 15 of 80 notes based on index-level signals — rather than partitioning into exhaustive sub-passes. This is closer to how the quality-scores note describes filtering: "only the top N candidates get full attention." The note mentions that "the agent can use the index to choose sub-passes intelligently" but frames this as partitioning rather than selective loading, which is a subtly different operation.

- [Internal consistency] The note says descriptions become "the only content that participates in index-level operations" in the middle regime. But the note also says parent areas "operate at index resolution — orientation, routing, candidate discovery." If parent areas have curated editorial structure (as the areas note describes — "synthesis and editorial structure"), then the editorial prose in an index is also content that participates in index-level operations, not just descriptions. The claim "only content" may be slightly too strong.

- [Grounding alignment] The note attributes to ADR 003: "/connect works by reading the full index.md in one pass." ADR 003 does say "read kb/notes/index.md first" and "scanning the full list catches cross-domain connections." However, ADR 003 frames index-first scanning as a vocabulary-bias fix (conceptual overlap vs. keyword overlap), not primarily as a context-boundary phenomenon. The reviewed note reframes the ADR's design choice as "built on the index boundary," which is the reviewed note's own interpretive layer. The reframing is reasonable but the attribution implies ADR 003 was motivated by the boundary concept, when it was motivated by discovery quality.

- [Completeness] Boundary case: multi-modal operations. The note identifies two operations (orientation and comparative reading) and maps them to resolution requirements. But there is a third plausible operation: targeted investigation — loading a specific note plus its linked neighbors to understand one thread in depth. This operation doesn't require loading the whole collection and so isn't governed by either boundary. It falls outside the framework, but since the framework claims to govern "collection operations" (title), and targeted investigation is arguably not a collection operation, this may be intentional scoping rather than a gap.

PASS:
- [Internal consistency] The three regimes are internally consistent with each other — regime 1 is strictly more capable than regime 2, which is strictly more capable than regime 3. No section contradicts another on what each regime enables or prevents.
- [Internal consistency] The consequences section follows logically from the regime framework. Each consequence (descriptions becoming load-bearing, parent/child operational layers, library/workshop necessity) maps cleanly to the regime model without introducing claims that contradict the framework.
- [Grounding alignment] The attribution to the areas note is accurate — that note does identify orientation and comparative reading as the two justifying operations, does treat context as the shared constraint, and does identify the tension between synthesis and flat lists in index design. The reviewed note's extension (separating them by resolution) is clearly flagged as the note's own contribution.
- [Grounding alignment] The attribution to the quality-scores note is accurate — that note does discuss /connect scaling and candidate filtering. The reviewed note's claim that quality scores are "a response to the index boundary" is a reasonable inference, though the quality-scores note frames the problem as candidate volume rather than context boundaries specifically.
- [Grounding alignment] The attribution to the workshop note is accurate — the library/workshop separation is described there, and the reviewed note adds the operational argument (keeping the index scannable) as a new dimension.

Overall: 3 warnings, 5 info
===
