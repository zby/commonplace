=== PROSE REVIEW: agents-navigate-by-deciding-what-to-read-next.md ===

Checks applied: 8

WARN:
- [Anthropomorphic framing] The note consistently uses "she/her" pronouns and human-like agency language for agents: "An agent has a task and needs information she doesn't yet have," "lets her judge without paying that cost," "the agent knows both what's there and why it matters before deciding." While the note's title uses "agents" generically, the body reads as if describing a human researcher rather than an LLM-based agent. Verbs like "knows," "decides," and "judge" attribute cognitive capacities without qualification.
  Recommendation: If the note intends to cover both human and LLM agents, the anthropomorphic framing is defensible but should be flagged as deliberate ("we use agentive language for readability; the claims apply to any system that selects which documents to load"). If it's specifically about LLM agents, substitute more precise language: "the agent evaluates relevance" rather than "she judges," "the agent has access to" rather than "the agent knows." The pronoun "she" in particular invites human-cognitive readings that may not be intended.

INFO:
- [Source residue] The note appears to have been generalized from this project's own knowledge-base methodology. Terms like "index entries," "skill descriptions," "context phrases," "frontmatter descriptions," and "title as claim" are specific to the commonplace KB design. However, the note's description ("links, index entries, search tools, and skill descriptions are all pointers") signals this scope explicitly, and the note frames these as instances of a general pattern ("The pattern is the same everywhere — what varies is how much context the agent gets"). The domain-specific vocabulary is arguably the intended content rather than residue. Worth checking: is the note meant to apply beyond this specific KB system? If so, the four pointer types are all drawn from one system and may not generalize without examples from other navigation contexts.

- [Confidence miscalibration] The note presents its framework — pointers as the fundamental unit of navigation, the context-cost tradeoff — with direct assertion: "That decision is the fundamental unit of navigation." This is the note's own construction, not cited from any source. The framing reads as established theory rather than a proposed model. The confidence level is high but arguably appropriate for a design note within a KB methodology project, where the author is defining their own terms. Flagging as INFO rather than WARN because the note's type is "note" (not "structured-claim") and the claims are definitional rather than empirical.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, equations, or symbolic apparatus present. The note uses prose throughout and makes its arguments in natural language. Clean.

- [Proportion mismatch] The core claim is that navigation is deciding what to read, and context makes that decision cheaper. The section "How much context different pointers carry" — which is the load-bearing analysis — is the longest section (~4 paragraphs). The "Design implication" section is appropriately shorter, serving as a summary of actionable consequences. The opening section sets up the framing concisely. Proportions match the relative importance of each part.

- [Orphan references] No specific figures, percentages, named studies, or unsourced empirical claims. The note's arguments are conceptual and definitional rather than evidence-driven. The one external reference (Agentic Note-Taking 23) is properly cited and contextualized.

- [Unbridged cross-domain evidence] No cross-domain evidence transfers attempted. The note stays within its own domain (agent navigation in knowledge systems) and cites one source from the same domain. Clean.

- [Redundant restatement] Each section opens with new content. "What makes the decision tractable" moves from the setup (pointers as decisions) to the mechanism (context reduces cost). "How much context different pointers carry" moves to concrete analysis. "Design implication" moves to prescriptions. No section re-explains what the prior section established. Clean.

Overall: 1 warning, 2 info
===
