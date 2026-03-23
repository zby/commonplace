=== PROSE REVIEW: directory-scoped-types-are-cheaper-than-global-types.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The "Current implementation" section states "The CLAUDE.md routing table and content workflow now implement this proposal" — presenting the note's own design proposal as an accomplished fact. The note is tagged `status: seedling`, yet this section uses language of completion ("now implement," "This is progressive disclosure applied to the type system"). If the implementation genuinely exists, the seedling status is wrong; if the status is accurate, this section overstates delivery. Similarly, the "What this would change" section uses future tense ("gets thinner," "become type definitions"), which is appropriately propositional — but the "Current implementation" section contradicts that tentativeness.
  Recommendation: Reconcile the two framings. If the implementation is real, update the status and rewrite "What this would change" as "What changed." If the note is still propositional, reframe "Current implementation" as "Proposed implementation path" or "Partial implementation" and soften the language.

- [Proportion mismatch] The core claim is that directory-scoped types are cheaper than global types because the resolution mechanism differs between LLM contexts and programming contexts. The section that carries the most weight for this claim — "Why this doesn't happen in programming" — is the one that explains the cost mechanism (no import, no compiler, everything must be pre-loaded). It gets roughly equal treatment to the "What this would change" section and the "Current implementation" section, both of which are consequences rather than the core argument. Meanwhile, "The economic argument" section, which should be the load-bearing bridge between the mechanism insight and the proposal, is relatively thin — it mostly re-delegates to the linked note on loading frequency rather than developing the economics in its own right.
  Recommendation: Develop "The economic argument" section to do more of its own work: quantify or illustrate what "context tax" looks like in practice (how many tokens? how often loaded?), rather than relying primarily on a link to another note for the foundational argument.

INFO:
- [Source residue] The note references seven specific global base types from a "document classification spec" and mentions specific directory conventions (tasks/README.md, related-systems/README.md). These are internal to this KB, so they are legitimate concrete referents rather than leaked residue from an external domain. However, the note's claimed generality is ambiguous — is it about type systems for LLM-operated knowledge bases in general, or specifically about this KB's type system? The title suggests the general principle; the body is almost entirely about this KB's specific implementation. This is not strictly source residue but worth noting: a reader expecting a general design principle will find a project-specific design document.

- [Redundant restatement] The opening of "The economic argument" recaps the resolution mechanism insight from "Why this doesn't happen in programming" ("Given that we don't have automatic resolution...") before moving to its own contribution. This is a single sentence rather than a full paragraph, so it is mild — but it is doing recap work that a forward reference would handle more efficiently.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic decompositions are used. The tables are genuinely informative (mapping structural expectations to their actual locations). No decorative formalism detected.

- [Orphan references] No specific numbers, percentages, or named studies appear without context. The "~80% of writes" figure in the "Current implementation" section is an estimate rather than an empirical claim, and reads as an approximation rather than a precise finding. No unsupported empirical claims detected.

- [Unbridged cross-domain evidence] The note explicitly addresses the programming-to-LLM domain transfer in its "Why this doesn't happen in programming" section, and the bridge is the central argument of the note (different resolution mechanisms). The cross-domain move is well-bridged rather than assumed.

- [Anthropomorphic framing] The note uses "the agent needs to know," "the agent needs to reason about," and "the agent either knows what structured-claim means." These attribute knowledge and reasoning to the agent, but in the context of this KB — where "agent" refers to an LLM operating in a tool loop — "knows" and "needs to reason about" are reasonable shorthand for "has in context" and "must process." The note itself clarifies this: "must be in the context window." No misleading anthropomorphism detected.

Overall: 2 warnings, 2 info
===
