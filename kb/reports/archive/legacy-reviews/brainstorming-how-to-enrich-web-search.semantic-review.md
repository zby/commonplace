<!-- REVIEW-METADATA
note-path: kb/notes/brainstorming-how-to-enrich-web-search.md
last-full-review-note-sha: dd5c21e5474763b08f84c52163d31047f4fbeabc
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T00:00:00+00:00
last-accepted-note-sha: dd5c21e5474763b08f84c52163d31047f4fbeabc
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T00:00:00+00:00
last-acceptance-kind: full-review
review-type: semantic-review
-->

=== SEMANTIC REVIEW: brainstorming-how-to-enrich-web-search.md ===

Claims identified: 11

WARN:
- [Completeness] The "Two value propositions" enumeration (connect results to each other; connect results to KB) omits a third value proposition the note itself later surfaces in Open Questions: **contradiction detection** ("search results that *contradict* existing KB content"). The note acknowledges this as a "different operation" but does not revisit the "two value propositions" framing to account for it. If contradiction detection is genuinely a different operation rather than a third value proposition, the note should explain why — otherwise the enumeration undercounts its own content.
- [Completeness] The Phase 3 sub-operations ("Gaps," "Synthesis opportunities," "New queries") are presented as the outputs of the synthesize-and-redirect step, but the note does not account for **prioritization or ranking** among them. With N results generating potentially O(N^2) pairwise connections, the gap/synthesis/query outputs could be numerous. The note flags the cost problem in "Architectural tensions" but treats it as a depth-vs-cost tradeoff rather than as a missing phase operation. The "notes need quality scores to scale curation" link hints at this but the gap between identifying synthesis opportunities and deciding which ones to pursue is unaddressed.
- [Grounding] The note claims the proposed iterative search loop "is the boiling cauldron loop applied to search" (Phase 3, last sentence). The boiling cauldron in the source note (automating-kb-learning-is-an-open-problem.md) defines seven specific mutation types: extract, split, synthesise, relink, reformulate, regroup, retire. The enriched search loop proposes different operations: gap detection, synthesis, and query generation. Only "synthesise" maps directly. The source's boiling cauldron also requires a scoring/evaluation gate ("surfaced for human review only when it scores high enough") which the search loop does not include — Phase 3 has no quality gate, just generation. The analogy is suggestive but overstates the structural correspondence. The note is making its own architectural move and attributing it to the source more strongly than warranted.

INFO:
- [Completeness] The stopping criteria list (diminishing returns, query exhaustion, budget, user checkpoint) is labeled as mapping to oracle types on the oracle-strength spectrum, but the mapping is approximate. "Diminishing returns" and "query exhaustion" are both described as "soft oracles," while the source note's spectrum distinguishes between soft oracle (proxy score), interactive oracle (feedback), and delayed oracle (you only know later). Diminishing returns could arguably be a delayed oracle (you only know whether the graph was complete enough when you try to use it later). The mapping is plausible but looser than the note implies.
- [Completeness] The MVP (five-step chain) claims to validate "whether connection quality on web search results justifies the iteration investment." But the MVP includes no evaluation mechanism — it produces a research report (step 5), but there is no criterion for judging whether the connections in that report are valuable. This is the same oracle gap the automating-kb-learning source identifies for the boiling cauldron, but the note does not flag it for the MVP. The validation claim is aspirational rather than operational.
- [Grounding] The note says the `/connect` skill "already operates at level 2" of the abstraction depth hierarchy (shared structure). The discovery source note describes level 2 as requiring "understanding, not just matching" and calls it "expensive." The note does not cite evidence that `/connect` achieves structural-level connections rather than surface-level ones; this is stated as fact. The claim is plausible given the articulation test described in the note, but the grounding is the note's own assertion rather than a demonstrated property of the skill.
- [Internal consistency] The intro paragraph hedges that "Phase 3 goes beyond pure /connect reuse (it adds synthesis and query generation), so this is connection methodology as a starting point, not a complete design." But the "Two value propositions" section and the "Why this differs from naive search" section both frame the value as coming from `/connect`'s existing capabilities (articulation testing, structural reasoning). The Phase 3 operations — gap detection, synthesis, query redirection — are the parts that would actually reach level 3 (generative model), yet they have no operational specification. The note is internally consistent in acknowledging this gap, but the rhetorical weight falls on the reuse story while the genuinely novel (and unspecified) part is where the highest claimed value lives.

PASS:
- [Completeness] The "Two value propositions" cleanly partition the design space along the corpus boundary: intra-result connections vs. result-to-KB connections. Within each proposition, the note identifies distinct mechanisms (articulation testing for intra-result, `/ingest` for result-to-KB). No boundary case straddles both propositions ambiguously.
- [Grounding] The attribution to the discovery epistemology note for the three abstraction depths (shared feature, shared structure, generative model) is accurate. The source note uses exactly this three-level hierarchy with the same names and the same ordering. The note's characterization of level 1 as "what naive RAG does" is the note's own inference but a reasonable one.
- [Grounding] The reference to the two-kinds-of-navigation note is accurate: the source distinguishes link-following (local, contextual) from search (long-range, title/description-based). The note's claim that enriched search "combines both kinds of navigation" is a legitimate extension of the source's framework to a new context.
- [Grounding] The reference to the claw-learning-loops note accurately reflects its content. The source argues that a Claw's learning loop must target action capacity, not just retrieval. The note's claim that enriched search exemplifies "active research capacity" aligns with the source's framing of action beyond retrieval.
- [Internal consistency] The five-phase architecture (Seed, Snapshot & inter-connect, Synthesize & redirect, Bridge to KB, Report) is internally consistent. Each phase has clear inputs and outputs, and the MVP cleanly maps to phases 1-2 plus 4-5, skipping the iteration loop (phase 3). The architectural tensions section identifies real tradeoffs that correspond to genuine design decisions rather than contradicting the architecture.
- [Internal consistency] The note consistently maintains its "brainstorming" / "seedling" framing throughout. Claims are hedged appropriately. No section asserts certainty that other sections qualify.

Overall: 3 warnings, 4 info
===
