=== SEMANTIC REVIEW: needs-testing.md ===

Claims identified: 8

1. [Intro] "Ideas that look promising but haven't been tested enough to confirm." — scope/definition claim for the note
2. [Extract, connect, review cycle] "A three-phase pipeline: extract pulls insights from source material, connect finds relationships to existing notes (the backward pass — updating older notes to reference newer ones), review checks quality." — enumeration of three phases
3. [Extract, connect, review cycle] "The connect phase seems to be where most value is created." — evaluative claim
4. [Extract, connect, review cycle] "Likely needs tweaking." — hedged meta-claim
5. [Extract, connect, review cycle] "This cycle is a primitive version of the aspirational learning loop" — relationship claim to the boiling cauldron
6. [Extract, connect, review cycle] "the boiling cauldron's extract/relink/synthesise mutations run manually through these three phases" — mapping claim: three of seven boiling-cauldron mutations correspond to the three-phase cycle
7. [Input classification before processing] "External sources (papers, articles, blog posts) may need different treatment than domain research or design explorations." — classification claim: input types differ
8. [Input classification before processing] "Classifying input type before processing could prevent applying the wrong extraction strategy." — causal claim

WARN:
- [Completeness] The note claims a "three-phase pipeline" (extract, connect, review) and then maps it to "the boiling cauldron's extract/relink/synthesise mutations." But the boiling cauldron in the linked source defines seven mutations (Extract, Split, Synthesise, Relink, Reformulate, Regroup, Retire), not three. The note selectively names three of those seven ("extract/relink/synthesise") to make the mapping work, but this leaves four mutations (Split, Reformulate, Regroup, Retire) unaccounted for. If the three-phase cycle is genuinely "a primitive version" of the full loop, the mapping should either explain where the other four mutations fall within the three phases or acknowledge that the cycle covers only a subset. As written, a reader could mistake the three-phase cycle as covering the entire boiling cauldron when it covers roughly three-sevenths of it.

- [Completeness] The "review checks quality" phase is asserted but never unpacked. What does quality mean here — structural validity, semantic accuracy, connection strength, all of the above? The linked source distinguishes structural metrics ("PageRank, betweenness centrality, cluster density") from question-answering capacity and from artifact-level quality checks (the text testing framework). The review phase is the most judgment-heavy of the three, yet it receives the least specification in the note.

INFO:
- [Completeness] The input classification section enumerates "external sources (papers, articles, blog posts)" versus "domain research or design explorations" as distinct types, but the boundary between these categories is not defined. A blog post about a design pattern could be either an external source or domain research. The note does not address how to classify inputs that straddle the boundary, or whether the classification is by provenance (external vs. internal) or by content type (survey vs. exploration). This is a natural consequence of the note's "needs testing" status, but worth flagging for when the idea matures.

- [Grounding alignment] The note says the extract/connect/review cycle "is a primitive version of the aspirational learning loop." The linked source (automating-kb-learning-is-an-open-problem.md) reciprocally says at line 85: "needs-testing — the extract/connect/review cycle is a primitive version of the boiling cauldron, already partially operational." The relationship is mutually acknowledged. However, the linked source frames the boiling cauldron as "aspirational" with an emphasis on the unsolved oracle and evaluation problems that block automation. The note here presents the three-phase cycle as something that "likely needs tweaking" — a much milder framing that does not surface the evaluation gap the linked source treats as the central open problem. The link is accurate but the inherited context understates the difficulty.

- [Completeness] The claim "The connect phase seems to be where most value is created" is plausible but untested (which the note acknowledges via "seems"). The linked source's analysis of where untapped value sits ("the link structure is where the most untapped value sits, because it's where understanding is encoded") supports this claim indirectly. However, the source argues this about link structure generally, not about the connect phase of a specific pipeline. The note's claim is narrower (one phase of a three-phase manual cycle), while the source's claim is about the KB's link layer as a whole. The inference is reasonable but not a direct grounding.

PASS:
- [Internal consistency] The note's two sections are independent ideas under a shared "needs testing" umbrella. There is no contradiction or definition drift between them — they do not share terminology or make claims that could conflict. The note's framing as a collection of untested ideas is internally consistent.
- [Grounding alignment] The reciprocal link between this note and automating-kb-learning-is-an-open-problem.md is accurate in both directions. The linked source does describe the boiling cauldron, and the note's characterization of the cycle as "a primitive version" aligns with the source's own description at line 85.
- [Internal consistency] The hedged language throughout ("seems to be," "likely needs tweaking," "may need," "could prevent") is consistent with the note's declared purpose of collecting ideas that "haven't been tested enough to confirm." The note does not overclaim.

Overall: 2 warnings, 3 info
===
