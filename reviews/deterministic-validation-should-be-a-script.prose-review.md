=== PROSE REVIEW: deterministic-validation-should-be-a-script.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The opening sentence states "Our `/validate` skill runs all checks through an LLM (Sonnet), including checks that are purely deterministic." The phrase "purely deterministic" is stated as fact, but whether each listed check is truly deterministic is itself an assumption — e.g., "Required sections per type" may have edge cases (partial matches, variant headings) that push it toward soft oracle territory. Separately, the closing paragraph asserts "The `/validate` skill would then only need to run the judgment-based checks, making it cheaper and faster" as a straightforward consequence, but whether it would actually be faster end-to-end (factoring in script maintenance, false positives, user experience of two separate feedback channels) is not as settled as the phrasing implies.
  Recommendation: Hedge the hard/soft classification as proposed rather than given — e.g., "checks that appear purely deterministic" or "checks we believe are deterministic." For the closing claim, acknowledge that the cost/speed benefit depends on implementation details.

INFO:
- [Source residue] The note references "Thalo's 32 validation rules" as a comparison point. Thalo is a specific external system, and the note uses it as evidence that deterministic scripting works for validation. This is fine as a cited example, but the phrasing "Comparing with Thalo's 32 validation rules — all of which are deterministic scripts — reveals that we're spending LLM tokens on work a Python script could do in milliseconds" treats Thalo's design choice as proof of feasibility for this KB's validation. Thalo's constraints and this KB's constraints may differ. This is borderline — the note does link to the related-system review, which presumably provides the full comparison — but the rhetorical weight given to it ("reveals") is slightly stronger than the evidence warrants.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus present. The note uses plain lists to classify checks, which is appropriate for the content.
- [Proportion mismatch] The core claim (split validation into script vs. skill) gets the bulk of the note through the two classified lists. The framing paragraphs are proportionate — the opening motivates the split, the closing states the payoff. The load-bearing content (the two lists) is the longest section, as it should be.
- [Orphan references] No unsourced data points or empirical claims. The only specific reference (Thalo's 32 rules) is linked to a related-system review. The mention of `sync_topic_links.py` refers to an existing script in the repo.
- [Unbridged cross-domain evidence] The Thalo comparison is same-domain (knowledge-base validation systems). The oracle-strength spectrum link is to an internal note that already establishes the framework. No cross-domain transfer issues.
- [Redundant restatement] The note is short and linear. No section re-explains what a prior section established. Each paragraph advances: motivation, hard-oracle list, soft-oracle list, payoff.
- [Anthropomorphic framing] No anthropomorphic language. The note discusses scripts and skills without attributing agency or mental states to models.

Overall: 1 warning, 1 info
===
