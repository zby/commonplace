=== PROSE REVIEW: types-give-agents-structural-hints-before-opening-documents.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The opening paragraph asserts "Agents are stateless — they start fresh every session with no memory of what they've read before" as an established fact. This is true for some agent architectures but not all — many agent frameworks support persistent memory across sessions. The note's own KB vocabulary (CLAUDE.md) does not define "agent" this narrowly. Since this is the note's own framing rather than a cited finding, it should be flagged as an architectural assumption, not a universal truth.
  Recommendation: Qualify the claim — e.g., "In this architecture, agents are effectively stateless..." or "Agents that lack persistent memory start fresh every session..." — to signal this is a design premise, not a universal property.

- [Proportion mismatch] The core claim is that types give agents structural hints before opening documents. The note's most load-bearing idea — how types and descriptions combine to enable routing — gets one paragraph (paragraph 2, ~75 words). The verifiability criterion and enforcement sections that follow are essentially pointers to other notes, each also about one paragraph. The result is that the note's own central contribution (the two-level filtering: type narrows by kind, description narrows by instance) is stated but never developed. For example, the note never illustrates what a routing decision looks like in practice, how much context this saves, or what happens when an agent faces a choice between two documents of the same type.
  Recommendation: Develop paragraph 2 with a concrete walkthrough or example showing the routing decision in action. This would give the core claim weight proportional to its importance.

INFO:
- [Source residue] The note is written at a general level about agent-operated knowledge bases. The examples used ("A `spec` tells an agent it can implement from this," "A `structured-claim` tells it there's a developed argument with evidence," "An `index` tells it this is a navigation hub") are all drawn from this KB's own type system. This is appropriate since the note is about this KB's design, but worth noting: if the note is meant to be a general claim about agent-KB design (as the title suggests), the examples are narrowly drawn from one system. Currently they work because the note doesn't claim generality beyond this KB.

- [Anthropomorphic framing] The phrase "agents make routing decisions" and "the agent reads a type and description, then decides whether to load the full document" attributes decision-making to the agent. In this KB's framework, agents are tool loops that execute instructions, so "decides" is a reasonable shorthand — the agent's LLM component does perform something functionally like deciding. This is borderline but acceptable given the KB's vocabulary conventions.

CLEAN:
- [Source residue] No domain-specific vocabulary from an external source leaks into the note. All examples are drawn from the KB's own type system, which is the note's subject matter.
- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The note argues entirely in prose.
- [Orphan references] No specific numbers, percentages, named studies, or empirical claims appear without sourcing. All references are to other notes in the KB.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. The note's arguments are internal to the KB's design.
- [Redundant restatement] Each paragraph advances a distinct point: (1) the problem, (2) how types solve it, (3) the verifiability criterion, (4) the enforcement dependency. No section restates a prior section's conclusion.

Overall: 2 warnings, 2 info
===
