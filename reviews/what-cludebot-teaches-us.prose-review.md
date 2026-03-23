=== PROSE REVIEW: what-cludebot-teaches-us.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The "Worth adopting now" section uses assertive framing for proposals that have not been tested. "Active contradiction surfacing" is presented with "A KB that only surfaces agreement becomes quietly overconfident" — this states a consequence as fact without evidence. Similarly, "Consolidation passes" asserts "As the KB grows past 300-400 notes, this becomes important to prevent fragmentation" — a specific threshold presented as established when it is a guess. These are the note's own proposals, not findings from cludebot, but the language does not flag them as proposed.
  Recommendation: Hedge the assertions that go beyond what the cludebot source establishes. "A KB that only surfaces agreement *risks becoming* overconfident" and "past 300-400 notes, fragmentation *may* become a concern" would better match the epistemic status.

- [Proportion mismatch] The note's title is "What cludebot teaches us," implying the core value is what to borrow. The "Worth adopting now" section (~180 words) carries the most actionable weight, yet "What we already have" (~200 words) and "Watch for as the KB grows" (~200 words) are at least as long, and "What to skip" (~130 words) is substantial too. The "already have" section adds no new capability — it is confirmation, not instruction. Meanwhile "active contradiction surfacing," the most concrete and implementable recommendation, gets only ~70 words of development (less than the "molecular metaphor" dismissal in "What to skip").
  Recommendation: Develop the "Worth adopting now" items more fully — especially "active contradiction surfacing," which is described just enough to be tantalizing but not enough to act on (what would the prompt change look like? what would the agent do with a found contradiction?). Consider whether "What we already have" can be compressed; it serves confidence-building but occupies prime note real estate.

INFO:
- [Source residue] The note is explicitly a review of cludebot, so cludebot-specific terminology ("recallSummaries() → hydrate()", "atoms, bonds, molecules, stability scores", "Supabase/pgvector/Solana") is expected. However, the description says "Techniques from cludebot worth borrowing" — framing the note as about techniques, not about cludebot. The body then spends roughly half its length on things *not* worth borrowing ("What we already have," "What to skip"), which is useful for a system review but is not "techniques worth borrowing." The description undersells the note's actual scope.

- [Anthropomorphic framing] The phrase "the human decides what's worth writing down" in the "Automated importance scoring" dismissal implicitly contrasts human judgment against LLM judgment. This is fine in context (the note is about a human-operated KB), but worth noting that if the KB moves toward more autonomous agent operation, this assumption would need revisiting. No action needed now.

CLEAN:
- [Pseudo-formalism] The note uses one formal-looking expression: "O(k) where k ≈ 3-5 hops" and "O(n)" in the graph-based retrieval section. These are standard algorithmic complexity notations used correctly to distinguish traversal from scanning. They add precision the surrounding prose does not capture alone. Clean.

- [Orphan references] No unsourced specific figures, data points, or named studies appear. The "7%/day," "2%/day," "1%/day" decay rates are attributed to cludebot. The "300-400 notes" threshold is the note's own estimate (flagged under confidence miscalibration, not here). The "200 notes" and "1000+ notes" are approximate characterizations of current and future scale. Clean.

- [Unbridged cross-domain evidence] All evidence and examples come from the same domain (agent memory systems and knowledge-base design). Cludebot is a directly comparable system. No cross-domain transfer requiring a bridge was detected. Clean.

- [Redundant restatement] Each section opens with its own contribution. "Worth adopting now" does not re-explain "What we already have." "Watch for as the KB grows" does not restate "Worth adopting now." The sections are cleanly partitioned by adoption timeline. Clean.

Overall: 2 warnings, 2 info
===
