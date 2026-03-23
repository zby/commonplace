=== PROSE REVIEW: learning-is-not-only-about-generality.md ===

Checks applied: 8

WARN:
- [Source residue] The table in "Generality" (lines 17-24) uses exclusively KB-domain examples: "Fix a typo," "Sharpen a description," "Add a connection," "Define structured sections for a type," "Every related-system note gets consistent structure," "The verifiability gradient changes how everything constrains." The title and opening paragraph claim a general insight about learning ("People equate learning with generality..."), but the entire scope table is drawn from knowledge-base operations. A reader arriving from the learning-theory tag would expect domain-neutral or multi-domain illustration. The KB examples are legitimate, but without framing ("In a knowledge base, for instance...") or at least one non-KB example row, the table reads as a KB-specific taxonomy rather than a general learning claim illustrated through a KB.
  Recommendation: Either add a framing sentence before the table acknowledging it uses KB operations as the running example, or add one or two rows from a different domain (e.g., an athlete drilling form, a manufacturing process improvement) to demonstrate the generality the title claims.

- [Source residue] The opening paragraph's example "A system that can now multiply without hallucinating has learned" is an LLM-specific illustration (hallucination is an LLM term) dropped into a paragraph that frames the claim as general. This is mild — most readers in the expected audience will understand it — but it's a domain assumption embedded in what presents as a universal statement.
  Recommendation: Either generalize ("A system that can now multiply without errors has learned") or briefly flag the domain ("An LLM that can now multiply without hallucinating has learned").

INFO:
- [Proportion mismatch] The core claim of the note is that capacity is multi-dimensional (generality plus the reliability/speed/cost compound plus other dimensions). The "Generality" section gets roughly 250 words plus a table; "The compound" gets roughly 100 words; "Other dimensions" gets roughly 50 words. The compound section is the note's distinguishing contribution (the generality axis is well-established; the compound axis is what makes the note's title true), yet it receives less development than the generality section. This may be intentional — the compound is explored in linked notes — but the imbalance means a reader of this note alone gets much more support for "generality matters" than for "but it's not the only thing that matters," which is the title's actual claim.

- [Confidence miscalibration] "These form a compound because they often improve simultaneously" presents the reliability/speed/cost clustering as an empirical regularity, but it is the note's own proposed grouping. The evidence offered is one example (codification) and three brief assertions (conventions, caching, distilled skills). This is plausible but not established. The word "compound" and the claim that these dimensions "tend to move together" assert more covariance than the note demonstrates.

- [Redundant restatement] The last sentence of "The compound" section — "Learning cuts across Argyris's loops — it can be single-loop (codifying one check into a script) or double-loop (deciding that claim notes should use Toulmin-derived sections)" — revisits the Argyris mapping already introduced at the end of the "Generality" section. Both passages map single-loop/double-loop onto the note's framework. The second instance adds the compound-side examples, which is new, but the structural move (invoking Argyris to validate the current section) is repeated.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or variable definitions are used. The note relies on prose, a table, and bold-defined terms. No decorative formalism present.
- [Orphan references] The "23-49% improvement on task completion" (line 28) is attributed to AgeMem with a link to the relevant note. Simon and Argyris are cited in the Sources section with links. All specific claims trace to named sources. Clean.
- [Unbridged cross-domain evidence] Simon's definition (human learning theory) is used to ground a claim about system learning generally. The bridge is implicit but adequate: Simon's definition is stated in domain-neutral terms ("any change in a system"), so no transfer assumption is hidden. Argyris's single-loop/double-loop distinction is mapped onto KB operations with explicit "maps onto this axis as rough regions" language. Clean.
- [Anthropomorphic framing] The note uses "system" as its subject throughout, which is appropriate for the general framing. "A system that can now multiply without hallucinating has learned" uses "learned" deliberately — the note is explicitly arguing that capacity changes constitute learning. No unintended anthropomorphism.

Overall: 2 warnings, 3 info
===
