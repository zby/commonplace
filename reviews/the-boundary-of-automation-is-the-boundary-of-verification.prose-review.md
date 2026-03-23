=== PROSE REVIEW: the-boundary-of-automation-is-the-boundary-of-verification.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The title asserts "the boundary" (definite article, singular) as though verification is the sole structural boundary of automation. The caveats section itself acknowledges this: "The title uses 'the' boundary as a claim title, but the argument defends verification as *the primary structural* boundary, not the only one." The body text also uses assertive framing: "generation without verification produces output, not automation" and "Where automation stalls, the bottleneck is typically oracle construction, not generation." These are presented as established structural claims, but the note's own evidence base is three sources — one internal theory, one investor-oriented essay, and one interview — none of which are empirical studies directly testing the boundary claim. The note is aware of this (the convergence section is well-hedged), but the opening paragraph and title read as established principle rather than proposed synthesis.
  Recommendation: Soften the opening paragraph to match the epistemic status the note actually defends. The title can remain strong as a claim-title convention, but the first paragraph should signal synthesis rather than settled law. For example, "generation without verification produces output, not automation" could become "generation without verification produces output, not reliable automation" or be explicitly flagged as the note's central proposal.

- [Proportion mismatch] The core claim is that verification cost is the primary structural determinant of automation. The section that most directly supports this — "Why convergence matters" — is 4 sentences (~90 words). By contrast, "The evidence" section is ~270 words and "Caveats" is ~220 words. The convergence argument is the load-bearing section that distinguishes this note from a mere literature summary, yet it receives the thinnest treatment. Why does convergence across reasoning paths matter more than convergence across, say, citation networks? What would disconfirm the convergence? These questions go unaddressed.
  Recommendation: Expand "Why convergence matters" to articulate more precisely what makes the convergence evidentially strong (distinct reasoning paths, distinct domains) and what would weaken it (shared assumptions, citation overlap — which is mentioned but only briefly). The section currently reads as a transition between evidence and implications rather than as the argumentative core it actually is.

INFO:
- [Source residue] The note is framed at a high level of generality — "tasks become automatable when..." — but draws its three evidence sources from AI/ML, labor economics, and AI leadership commentary. All three domains concern AI-driven automation specifically, not automation in general. The claim could in principle apply to pre-AI automation (e.g., industrial automation, where verification via quality control is also load-bearing), but no such examples appear. This may be intentional scoping rather than residue, but a reader encountering the title might expect broader coverage.

- [Anthropomorphic framing] The phrase "no reliance on model self-knowledge" in the oracle-theory paragraph attributes "self-knowledge" to the model. This is mild — the note uses "self-assessment" elsewhere, which is more neutral — but "self-knowledge" carries stronger cognitive connotations.
  Recommendation: Consider replacing "model self-knowledge" with "model self-assessment" for consistency with the note's own preferred vocabulary.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or variable decompositions appear. The note argues entirely in prose. No issue.

- [Orphan references] Specific claims are sourced: "$600k for research taste" is attributed to Tam et al., the Karpathy autoresearch example is contextualized, Rabanser et al.'s calibration/discrimination finding is cited, MAKER's "zero errors over a million steps" is linked to its ingest. No unsourced empirical claims found.

- [Unbridged cross-domain evidence] The note is explicit about cross-domain transfer. It frames Tam's labor-economics argument in oracle vocabulary ("hard oracles in our vocabulary, though Tam doesn't use that term") and flags Amodei's interview as "our interpretive frame." These are genuine bridge sentences. The Rabanser et al. finding is applied within its native domain (model evaluation). No unbridged transfers detected.

- [Redundant restatement] Sections are distinct. "Why convergence matters" does not re-explain the evidence; it argues for its collective weight. "The practical implication" does not restate the convergence argument; it draws consequences. "Caveats" introduces genuinely new qualifications (error-cost tolerance, oracle gaming) rather than restating prior limits. No redundancy found.

Overall: 2 warnings, 2 info
===
