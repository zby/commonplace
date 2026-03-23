=== PROSE REVIEW: session-history-should-not-be-the-default-next-context.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that session history should not be the default next context — the separation between storage and loading. The section "The right split: storage vs next-context loading" carries the most weight for that claim, but it arrives after three setup sections ("Where the problem actually appears," "Why chat sessions and tool loops default to trace-preserving state," "Why transcript inheritance breaks down") that collectively consume comparable space. More notably, "Execution-boundary compression is a recurring design move" and "Conversation vs refinement is one instance of the general problem" are supporting/derivative sections that together take significant space while doing less load-bearing work than the core split section. The note is not severely imbalanced — the setup sections do earn their length — but the two downstream sections could be tightened given that the core split section is where the note's distinctive contribution lives.
  Recommendation: Consider whether "Execution-boundary compression is a recurring design move" and "Conversation vs refinement is one instance of the general problem" could each be trimmed to a single paragraph or folded into the relevant notes section, since both mostly point outward to other notes rather than developing new argument.

- [Confidence miscalibration] The three-part trace taxonomy ("Conversation transcripts," "Tool/action traces," "Reasoning traces") in "The right split" is presented with assertive framing: "History conflates at least three trace types with different loading profiles." The taxonomy is the note's own construction — it is not cited from a source — but reads as established classification rather than a proposed decomposition. The graduated strength claim ("sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces") further gives it the feel of a settled result.
  Recommendation: Add a brief hedge acknowledging this is a proposed decomposition, e.g., "one useful decomposition" or "at least three trace types worth distinguishing." The graduated-strength sentence could be framed as "in our analysis" or similar.

INFO:
- [Source residue] The note references Slate's "episodes" and Spacebot's "scrubbed conclusions" as exemplifying systems. These are properly framed as examples and the Slate tension is handled explicitly in its own section. However, the phrase "phatic turns" in the conversation-transcripts bullet is a linguistics/pragmatics term that may be unfamiliar in the note's primary audience (agent/orchestration designers). It is not source residue in the strict sense — the note is not generalized from linguistics — but it is domain-imported vocabulary used without definition.
- [Redundant restatement] The opening of "Execution-boundary compression is a recurring design move" begins with "Across these systems, the shared move is compression at the execution boundary" — which restates the conclusion already developed in "The right split." This is mild; it functions as a transition sentence rather than a full restating paragraph, but the overlap is noticeable.

CLEAN:
- [Pseudo-formalism] The note uses `K`, `select(K)`, and `P` as notation inherited from the bounded-context orchestration model note. These are not introduced here as new formalism — they reference an established vocabulary from a linked foundation note. They do real work: `select(K)` compactly names the control point that distinguishes deliberate loading from automatic inheritance. No decorative notation found.
- [Orphan references] No unattributed specific numbers, percentages, or named studies appear. Empirical claims are tied to named systems (Slate, Spacebot) with links to their source material.
- [Unbridged cross-domain evidence] The note stays within agent orchestration and LLM system design throughout. The Slate and Spacebot references are same-domain (agent systems). No human-cognition findings are cited as if they directly apply to LLMs without bridging.
- [Anthropomorphic framing] The note consistently uses mechanistic language: "stores," "loads," "inherits," "surfaces." No anthropomorphic verbs ("knows," "understands," "believes") found. The phrase "how the agent thought" in the reasoning-traces bullet is borderline but appears in a descriptive gloss explaining what reasoning traces reveal, not as a claim about cognitive status.

Overall: 2 warnings, 2 info
===
