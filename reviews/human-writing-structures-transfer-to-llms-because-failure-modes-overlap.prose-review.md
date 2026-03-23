=== PROSE REVIEW: human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note states "they get distracted by irrelevant context, they conflate evidence with opinion, they skip qualifications when the argument feels strong" as established fact, but these are informal characterizations rather than cited empirical findings. The Lampinen source establishes content effects on reasoning accuracy, not specifically "getting distracted" or "skipping qualifications." The note then uses these asserted failures as load-bearing premises for the transfer argument without grounding each one.
  Recommendation: Either cite specific evidence for each claimed failure mode (distraction, conflation, skipping qualifications) or hedge them as commonly observed behaviors ("LLMs have been observed to..." or "practitioners report that..."). The Lampinen findings are strong evidence for content effects specifically; the other failure characterizations need their own support or softer framing.

- [Unbridged cross-domain evidence] The sentence "Chain-of-thought prompting reduces content bias by improving performance on abstract/unfamiliar conditions without degrading familiar ones" is presented as established, and then the note bridges to "the structured templates in this KB (Toulmin sections, Evidence/Reasoning/Caveats) may work by a similar mechanism." The bridge assumes that structured templates in a knowledge base operate by the same mechanism as chain-of-thought prompting, but these are quite different interventions — CoT adds intermediate reasoning steps at inference time, while Toulmin templates constrain the shape of stored text. The "similar mechanism" claim needs a stronger bridge explaining why constraining written structure would produce the same content-debiasing effect as prompting for step-by-step reasoning.
  Recommendation: Either spell out the shared mechanism more precisely (e.g., "both force explicit decomposition of the reasoning chain, reducing the model's reliance on content-driven heuristics") or weaken the claim to analogy ("may work by an analogous mechanism" or "this parallel is suggestive but the mechanisms may differ").

INFO:
- [Proportion mismatch] The note's title claim is about the transfer methodology — evaluate per-convention whether human failure modes apply to LLMs. The methodology itself gets roughly one paragraph of development (paragraph 3), while the Lampinen evidence gets two paragraphs (paragraphs 4-5). The methodology is the note's distinctive contribution; the empirical evidence is supporting material. The proportions are slightly inverted. This is mild because the evidence paragraphs do circle back to the methodology, but the methodology section could carry more weight — for example, walking through a second convention beyond Toulmin to show the per-convention evaluation in action.

CLEAN:
- [Source residue] The note claims generality over "human writing genres" and uses Toulmin argumentation, scientific paper structure, and legal brief format as named examples. All three are framed explicitly as examples ("for instance," "for Toulmin," "for scientific paper structure"). No leaked domain-specific vocabulary from a narrower origin. The writing-convention domain is consistent throughout.

- [Pseudo-formalism] No formal notation, equations, or symbolic decompositions present. The note argues entirely in prose. Clean.

- [Orphan references] The note cites one empirical source (Lampinen et al. 2024) with a link to the ingest, and references specific findings (syllogisms, Linda problem, Wason selection task, antecedent-false errors, CoT effects). All are traceable to the cited paper. No floating numbers or uncited claims.

- [Redundant restatement] Each paragraph opens with new content. Paragraph 2 introduces the naive-vs-refined transfer argument; paragraph 3 states the methodology; paragraph 4 presents empirical evidence; paragraph 5 discusses CoT; paragraph 6 generalizes. No section re-explains what a prior section already established.

- [Anthropomorphic framing] The note says LLMs "get distracted," "conflate evidence with opinion," and "skip qualifications when the argument feels strong." These sound anthropomorphic, but the note explicitly frames them as "surprisingly human-like failure modes" and flags them as "un-machine-like" — the anthropomorphic quality is deliberate and acknowledged, not accidental. The note is making a specific claim that these behaviors resemble human failures, which is the entire point. This is intentional framing, not careless attribution.

Overall: 2 warnings, 1 info
===
