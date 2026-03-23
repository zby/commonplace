=== SEMANTIC REVIEW: constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md ===

Claims identified: 12

1. "Capacity decomposes into generality and a compound of reliability, speed, and cost" (opening paragraph, attributed to learning-is-not-only-about-generality.md)
2. "The two learning mechanisms -- constraining and distillation -- both operate on this trade-off" (opening paragraph)
3. "The calculator has far more capacity for multiplication" than an LLM (The trade-off in action)
4. "These three dimensions move together because the substrate changes" (The trade-off in action)
5. "Constraining constrains the interpretation space. Each constraint narrows what the system can do (less generality) but makes what it does do more reliable, faster, and cheaper." (How constraining trades)
6. "Codification -- the far end of the constraining spectrum -- is the most dramatic compound gain" (How constraining trades)
7. "Constraining short of codification (storing outputs, writing conventions) also improves reliability and speed, just less dramatically" (How constraining trades)
8. "Distillation extracts from a larger body of reasoning into a focused artifact shaped by a specific use case, context budget, or agent" (How distillation trades)
9. "The extracted artifact is narrower than the source (less generality) but operationally more efficient (compound gain)" (How distillation trades)
10. "A skill distilled from fifteen methodology notes fits in a single context window (speed, cost) and delivers consistent procedure (reliability)" (How distillation trades)
11. The comparison table claims constraining and distillation differ along four axes: operation, what changes, medium transition, compound yield (The mechanisms differ)
12. "The reverse -- relaxing a constrained component, or loading the full source instead of the distillate -- trades compound back for generality" (closing paragraph)

---

WARN:
- [Completeness] The note claims reliability, speed, and cost "move together because the substrate changes" (claim 4), but this causal explanation is specific to the calculator/codification case. The note itself provides a counter-pattern two paragraphs later: "Constraining short of codification (storing outputs, writing conventions) also improves reliability and speed." In that case the substrate does NOT change -- the artifact stays in natural language. The compound gains in those cases must have a different cause (e.g. removing re-interpretation overhead), but the note offers "substrate change" as the general explanation. The foundation note (learning-is-not-only-about-generality.md) is more careful, saying the compound dimensions "often improve simultaneously" and that codification is "the clearest example." The reviewed note promotes the codification-specific causal mechanism to a general principle.

- [Completeness] The note's distillation section claims the distilled artifact is "narrower than the source (less generality)." Boundary case: a distilled artifact that reorganizes and synthesizes multiple sources can sometimes INCREASE generality by revealing patterns invisible in any single source. The distillation note itself acknowledges "Discovery -- positing an abstraction and recognizing particulars as instances of it" elsewhere in the KB. A distillation that discovers a cross-cutting pattern is narrower in volume but potentially wider in applicability. The claim that distillation always trades generality away is a simplification.

- [Grounding] The comparison table states distillation has "Moderate" compound yield vs constraining's "Highest at codification." The distillation source note (distillation.md) does not make this relative comparison. It says distillation makes operations "feasible that raw source material would exceed" -- a feasibility claim, not a moderate-gain claim. The ranking of compound yield across mechanisms is the reviewed note's own inference, not grounded in either source note. Readers could mistake the table as summarizing established framework rather than the note's own judgment.

INFO:
- [Completeness] Boundary case: caching or memoization. Caching an LLM response improves speed and cost without narrowing generality (the system can still handle all the same inputs; the cache just shortcuts repeated ones). The constraining note classifies "storing an LLM output" as constraining because it "commits to one interpretation," but caching a response for a repeated query is a pure compound gain with no generality loss for novel queries. This sits ambiguously between the two mechanisms -- it could be framed as constraining (commitment) or as infrastructure optimization (no generality trade). The note's framing that both mechanisms trade generality for compound may not cover pure efficiency improvements.

- [Completeness] Boundary case: the note's LLM-vs-calculator example is compelling but represents the extreme end. A middle case would sharpen the argument: adding input validation to an LLM workflow. This constrains (rejects some inputs) but the generality loss is arguably zero for well-formed inputs, while reliability increases. The trade-off framing suggests you always lose something; in practice the "generality" lost may be only malformed or adversarial inputs that were never genuinely served.

- [Grounding] The note says distillation "extracts from a larger body of reasoning into a focused artifact" (claim 8). The distillation source note defines it as "compressing knowledge so that a consumer can act on it within bounded context." There is a subtle vocabulary difference: "extracts from reasoning" vs "compresses knowledge." Extraction implies selection; compression implies the whole is preserved at lower resolution. The note's framing slightly over-emphasizes the selection aspect, though both framings are compatible.

- [Internal consistency] The comparison table says distillation's medium transition is "Typically none -- stays in natural language," and constraining's ranges from "none (conventions) to full (codification)." But the body text's distillation section says distillation produces a "focused artifact shaped by a specific use case, context budget, or agent" -- which in practice could be code (e.g. a codified script distilled from methodology). The codification note explicitly says "Codification can also be distillation -- when it draws on accumulated methodology or practice, it's both operations at once." The table's "typically none" for distillation is accurate as a statistical claim but could mislead readers into thinking distillation never crosses media.

PASS:
- [Internal consistency] The note's core structure is internally consistent: it defines one trade-off (generality vs compound), shows two mechanisms operating on it, and uses the comparison table to differentiate them. No section contradicts another on the basic framework.
- [Internal consistency] The term "compound" is used consistently throughout -- always meaning the cluster of reliability, speed, and cost. No definition drift.
- [Grounding] The attribution to learning-is-not-only-about-generality.md for the capacity decomposition (claim 1) checks out. That note explicitly defines "generality" and "the compound -- reliability, speed, cost" as the two clusters, and says "constraining and distillation both trade generality for compound gains."
- [Grounding] The constraining note (constraining.md) confirms the "interpretation space" framing and the constraining spectrum from conventions to codification. The reviewed note accurately represents this.
- [Grounding] The codification note (codification.md) confirms codification as "the far end of the constraining spectrum" and describes the substrate/medium change. The reviewed note's characterization is accurate.
- [Grounding] The bitter-lesson-boundary link is used correctly -- the note references it for determining "when the generality-vs-compound trade-off is permanent vs when relaxing is needed," which matches the source's content about arithmetic vs vision features.
- [Completeness] The LLM-vs-calculator example (claim 3) is a well-chosen concrete instance that maps cleanly to the framework. The three compound dimensions are all clearly illustrated (never wrong = reliability, microseconds = speed, free = cost).

Overall: 3 warnings, 4 info
===
