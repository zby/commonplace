=== PROSE REVIEW: quality-signals-for-kb-evaluation.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The opening paragraph and frontmatter correctly signal "speculative" / "Brainstorming," but several passages later in the note assert as if established. "If links decrease, the split broke something" (metamorphic relations) and "This is qualitatively different from having too few links — it's worse than no linking infrastructure" (credibility erosion) are stated as facts, not proposals. These are the note's own constructions — no source is cited for the split invariant behavior or the "worse than nothing" claim about credibility erosion. The speculative framing set up front doesn't carry through to these later sections.
  Recommendation: Add hedging consistent with the note's speculative status. E.g., "If links decrease, the split likely broke something" and "This may be qualitatively different from having too few links — potentially worse than no linking infrastructure, because..."

- [Proportion mismatch] The core claim is that many weak signals combined might manufacture a usable soft oracle. The section that directly addresses this — "The 'many weak signals' hypothesis" — is only one short paragraph plus a testability note (roughly 80 words). By contrast, "Neighborhood evaluation" (~250 words), "LLM critique of individual notes" (~250 words), "Agent-centric signals" (~200 words), and "Credibility erosion" (~180 words) each receive substantially more development. The hypothesis that makes the note cohere is the thinnest section.
  Recommendation: Develop the "many weak signals" section — specifically the independence question it raises and what would happen if signals are correlated. Consider whether the later sections (neighborhood evaluation, LLM critique, agent-centric signals, credibility erosion) are doing the work of separate notes rather than supporting this note's core claim.

- [Unbridged cross-domain evidence] "This is the same move as ensemble methods in ML: individual weak learners combined into a strong one." The analogy to ensemble methods is presented as direct equivalence ("the same move") but the bridge is missing. In ML ensembles, the weak learners share a common loss function and the combination has formal guarantees (e.g., boosting reduces bias). Here, the signals don't share a common objective function and there's no formal combination mechanism proposed. The analogy is suggestive but the "same move" framing overstates how much transfers.
  Recommendation: Weaken to analogy: "This parallels ensemble methods in ML" and briefly note what doesn't transfer (no shared loss function, no formal combination guarantees).

INFO:
- [Source residue] The AlphaGo analogy in the opening paragraph ("AlphaGo works because the game has a perfect verifier") comes from game-playing AI but the note is about KB evaluation. The analogy is partially bridged — the note explains what it takes from the comparison (perfect vs imperfect verifiers). However, the verb "works" is doing a lot: AlphaGo "works" in the sense of achieving superhuman play, which is a much stronger claim than "a KB learning loop can run." The residue is mild because the analogy is framed as an analogy, but "works because" imports more certainty from the game domain than the KB domain can support.

- [Redundant restatement] The "What could drive a learning loop" section opens by re-explaining the composite signal concept ("If the composite signal is good enough, the boiling cauldron from [the KB learning loop] could work") before listing its actual contribution (the four-step mutation loop). The restatement is brief enough that it functions as a transition, but the phrase "the boiling cauldron" references terminology from another note without re-explaining it, so the sentence serves neither as standalone setup nor as efficient transition.

- [Pseudo-formalism] The note uses formal-sounding terminology from graph theory (cluster coefficient, betweenness centrality, PageRank, eigenvector centrality) in the "Graph topology" section. These terms are used accurately and do reference real computable measures, so they are not decorative. However, the note doesn't specify how they'd be computed on a KB graph (directed? weighted? what are the nodes and edges exactly?), so the precision is at the vocabulary level rather than the operational level. This is borderline — the terms add meaning but could create a false sense of measurability.

CLEAN:
- [Orphan references] No unsourced specific numbers, percentages, or named studies appear. The description length thresholds ("< 50 chars," "> 200 chars") in the content quality proxies section are clearly framed as heuristic cutoffs ("too short... likely uninformative"), not empirical claims. The note avoids specific empirical assertions throughout.

- [Anthropomorphic framing] The note discusses "agents" extensively but in the context of actual software agents navigating a knowledge base, not as metaphors for LLM cognition. Language like "the agent learns to discount all links" in the credibility erosion section could be read as anthropomorphic, but in context it describes an observable behavioral pattern (reduced link-following rate), not an internal mental state. The LLM-related language ("ask the LLM to critique," "LLM judgment") is appropriately instrumental.

Overall: 3 warnings, 3 info
===
