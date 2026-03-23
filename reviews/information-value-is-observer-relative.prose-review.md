=== PROSE REVIEW: information-value-is-observer-relative.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The Prior work section presents four intellectual traditions as established precedent with confident attributions ("Relevance theory (Sperber & Wilson, 1986)," "Value of information in decision theory (Marschak, Radner)," "Bounded rationality (Simon)," "Bayesian decision theory"), but the note itself flags that "This literature survey is from the agent's training data, not systematic." The confident citation style (named authors, dates, specific claims about what each tradition establishes) projects more authority than the note's own TODO acknowledges it has earned. A reader encountering the TODO after four crisp bullet points may discount the caveat.
  Recommendation: Either move the TODO disclaimer above the bullet list so readers encounter the caveat before the citations, or soften the bullet framing — e.g., "Traditions that appear relevant (not yet verified against primary sources):" — so the confidence level is set before the details land.

- [Proportion mismatch] The core claim is that information value is observer-relative. The "How to present" subsection (roughly 12 lines of body text plus a dense paragraph on distillation) is substantially longer than "What to keep" (5 lines) and "What observer-relativity doesn't help with" (4 lines). "How to present" is really about KB conventions that follow from observer-relativity — useful but secondary to the claim itself. Meanwhile the note's most novel contribution — applying observer-relativity specifically to agent-operated KB design — gets only a brief framing paragraph at the top of "Why this matters for the KB" and the thin "What to keep" subsection.
  Recommendation: Develop "What to keep" to more fully articulate why observer-relativity reshapes inclusion decisions (the core design consequence). Consider whether the four-bullet convention list in "How to present" could be trimmed or spun off, since each convention is already documented in the linked notes.

INFO:
- [Pseudo-formalism] The phrase "In information-theoretic terms this is lossy compression" in the distillation paragraph invokes a formal framework without doing formal work — no rate-distortion tradeoff is specified, no entropy quantities are compared. Deleting the phrase leaves the surrounding argument ("it discards information. But for the target reader, the distillate can be more valuable than the source because it makes previously unreachable structure accessible") equally clear. The phrase is not harmful — it serves as a useful conceptual anchor — but it is decorative rather than load-bearing.

- [Anthropomorphic framing] The note is largely about observers in general, not models specifically, so most of the language is naturally appropriate. One edge case: "the agent can connect it to what it already has in context" attributes a connecting action to the agent. This is borderline — "connect" is more operational than cognitive, and the note is explicitly about agents as readers. Flagging only because the note's own framework (observer-relativity) could be stated more precisely: it is the context arrangement that determines connection opportunity, not an agent intention.

CLEAN:
- [Source residue] The note claims a general principle (observer-relativity of information value) and applies it to a specific domain (agent-operated KBs). Domain-specific terms like "token," "context," "agent," "note," and "index" are all appropriate to the stated application domain. No leaked vocabulary from an unrelated source domain was found. The Prior work section references multiple traditions without importing jargon from any single one.

- [Orphan references] All specific claims are attributed: Sperber & Wilson 1986, Marschak/Radner, Simon, Shannon, Kolmogorov. No unattributed numbers, percentages, or empirical data points appear. The note is careful to stay at the level of named traditions rather than citing specific experimental results, which avoids the orphan-reference failure mode.

- [Unbridged cross-domain evidence] The Prior work section cites traditions from decision theory, cognitive science, and information theory, but uses them to establish that observer-relativity is a known idea — not to make direct empirical claims about agent behavior. The bridge to the KB domain is explicit in the "Why this matters for the KB" section: "What's specific to our context is applying it to the design of an agent-operated knowledge base." No unbridged transfer was found.

- [Redundant restatement] The opening paragraph under "Why this matters for the KB" does briefly restate that observer-relativity is established elsewhere, but it does so to pivot — "What's specific to our context is applying it to..." — which is a transition that earns its space. No section opens by re-explaining a prior section's conclusion without adding new direction.

Overall: 2 warnings, 2 info
===
