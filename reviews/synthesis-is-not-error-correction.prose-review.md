=== PROSE REVIEW: synthesis-is-not-error-correction.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "There is no mechanism to detect that agent 2 contradicts agents 1 and 3." This asserts a universal property of synthesis as a category. Synthesis implementations vary — some merge strategies do surface contradictions (e.g., an LLM synthesizer could notice disagreement). The note's claim holds for naive concatenation/merge but is stated as a categorical rule. The sentence should hedge: "In naive synthesis, there is typically no mechanism..." or qualify which synthesis operations lack contradiction detection.
  Recommendation: Add a qualifier acknowledging that synthesis is a family of operations, and the no-contradiction-detection property applies to the naive variant Kim et al. tested rather than to all possible synthesis strategies.

- [Confidence miscalibration] "Synthesis propagates errors; voting corrects them." (opening paragraph) and "Synthesis is information aggregation. Voting is error correction." (end of 'The distinction' section). These are presented as categorical facts, but the note itself later introduces adversarial debate as a possible third category that partially corrects errors without voting. The clean binary framing in the opening overstates the sharpness of the distinction the note actually establishes — the note's own Open Questions section softens what the opening asserts.
  Recommendation: The opening could acknowledge the binary is a first approximation. Even a parenthetical — "at their extremes" or "in their pure forms" — would calibrate the claim to what the body actually supports.

INFO:
- [Proportion mismatch] The "What Kim et al. actually tested" section (~150 words) and "What MAKER tested" section (~130 words) are roughly balanced, which is appropriate. However, the "Design rule" section (~100 words) carries the note's prescriptive payload — it is where synthesis vs. voting becomes actionable — and it is the shortest substantive section. The core claim (title) is a negative distinction; the design rule is the positive contribution. A reader looking for the "so what" gets less development than the two evidence sections.
  Recommendation: Consider whether the design rule section deserves expansion — e.g., what happens when the match is wrong (Kim et al. is one case, but are there others?), or what signals tell a designer which aggregation to choose.

- [Source residue] The note references "first-to-ahead-by-k voting" and "red-flagging (discarding responses >700 tokens or with format violations)" — these are MAKER-specific implementation details that may be more granular than the note's level of abstraction requires. The 700-token threshold is a MAKER-specific parameter, not a general property of decorrelation. This is minor since the note is explicitly analyzing MAKER, but the specificity of ">700 tokens" feels like source residue in a note that aims to establish a general synthesis-vs-voting distinction.
  Recommendation: No change strictly necessary since this appears in a section explicitly about MAKER. If the note is later generalized, these details should move to a parenthetical or footnote.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus appears in the note. Numbers cited (17.2x, 4.4x, 7.8x, 5.1x, 515%) are empirical data points from cited sources, not decorative formalism. Clean.

- [Orphan references] All specific numbers trace to cited sources. The 17.2x, 4.4x, 7.8x, 5.1x figures are from Kim et al. (linked). The "3 agents," "3 rounds," and "515% overhead" are from the same source. The "million LLM steps" and ">700 tokens" are from MAKER (linked). No unsourced empirical claims found.

- [Unbridged cross-domain evidence] Both sources (Kim et al. and MAKER) are from the multi-agent LLM systems domain, which is the same domain the note addresses. No cross-domain transfer claims are made. The distinction between synthesis and voting is established within the multi-agent coordination domain throughout. Clean.

- [Redundant restatement] Sections build on each other without restating prior conclusions. "What Kim et al. actually tested" follows from "The distinction" by applying it; "What MAKER tested" follows by contrasting; "The design rule" synthesizes. No section opens by re-explaining what the previous section established. Clean.

- [Anthropomorphic framing] No anthropomorphic language detected. Agents "produce," "run," "solve," "attempt" — all appropriate for software agents. The note does not attribute mental states to models.

Overall: 2 warnings, 2 info
===
