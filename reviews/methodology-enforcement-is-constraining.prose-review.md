=== PROSE REVIEW: methodology-enforcement-is-constraining.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The opening sentence asserts the mapping as fact: "The ways we enforce methodology in the KB — instructions, skills, hooks, scripts — map directly onto the constraining spectrum." The table and gradient are the note's own construction (an application of constraining theory to a new domain), not a cited finding. The six-layer table with its reliability ordering is a proposed model, but is presented with assertive framing throughout ("The key insight: hooks are not cleanly 'deterministic'"). The maturation trajectory section similarly asserts: "new best practices should start as underspecified natural-language guidance and constrain toward precise, deterministic enforcement as they prove out" — this is a design recommendation presented as a principle.
  Recommendation: Add a brief framing sentence acknowledging the table is a proposed model applying constraining theory to methodology enforcement. The maturation trajectory could be hedged as "a plausible discipline" or "our recommended trajectory" rather than asserted as a requirement.

- [Proportion mismatch] The core claim is in the title: methodology enforcement IS constraining. The table and opening two paragraphs establish this mapping (roughly 350 words). The "Maturation trajectory" section then receives roughly 550 words of development — substantially more than the core mapping it depends on. The "Current state" section (50 words) and "Open questions" (80 words) are thin by comparison. The maturation trajectory is important but secondary to the core mapping claim; it currently dominates the note.
  Recommendation: Either develop the core mapping further (e.g., more on why each layer trades flexibility for reliability, concrete examples of each layer's failure mode) or consider whether the maturation trajectory warrants its own note, linked from here.

INFO:
- [Source residue] The note references "arscontexta" without introduction: "the three-tier model (instruction -> skill -> hook) that arscontexta uses oversimplifies." A reader unfamiliar with arscontexta would not know what this refers to — it reads as residue from a specific system review that leaked into a general note about constraining. The note does not link to the arscontexta related-system review either.
  Recommendation: Either add a brief inline gloss ("arscontexta, a related knowledge-base system, uses a three-tier model...") with a link to the related-system review, or generalize the reference ("a common three-tier model").

- [Redundant restatement] The second paragraph ("Instructions have the lowest *persistent* reliability because both phenomena compound...") partially restates what the table already shows. The first sentence re-explains the compounding of trigger indeterminism and semantic underspecification, which the table's columns already encode. The paragraph does add the useful observation about skills eliminating the trigger problem, but its opening is setup the reader doesn't need after reading the table.
  Recommendation: Trim the restating portion. The paragraph could start from "Skills eliminate the trigger problem..." and the table would carry the preceding argument.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The table uses plain-language columns (Trigger, Response, Reliability) rather than formalism. The description references the ABC paper's "D*=alpha/gamma" in the Relevant Notes section, but this is a citation rather than notation the note itself introduces. Clean.

- [Orphan references] The note cites specific numbers — "50% of AGENTS.md files were never changed," "additions (78 commits) and modifications (59) vastly outnumber removals (23) and section deletions (2)" — and attributes them to "The context engineering study" with a link to the ingest file. The source (context-engineering-ai-agents-oss.ingest.md) confirms these numbers. Clean.

- [Unbridged cross-domain evidence] The note's evidence stays within its own domain (KB methodology enforcement). The context engineering study data is about AGENTS.md files, which are the same kind of artifact the note discusses. ADR-001 is an internal example. No cross-domain transfer is attempted without bridging. Clean.

- [Anthropomorphic framing] The note uses "the LLM interprets," "the LLM remembers," "the LLM decides," and "the LLM follows." These are borderline but contextually appropriate — the note is about what happens at the prompt/agent layer where interpretation-language is the standard vocabulary. "Interprets" and "decides" describe observable behavior (selecting among possible responses) rather than claiming internal mental states. "Remembers" in "the LLM may not remember to apply the practice" is the most anthropomorphic instance, but it appears once and the surrounding context makes clear this means "the instruction may not be present in context or attended to." Clean, though "remembers" could be tightened if the note is revised for other reasons.

Overall: 2 warnings, 2 info
===
