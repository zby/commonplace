=== PROSE REVIEW: agent-statelessness-means-the-context-engine-should-inject-context-automatically.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note's frontmatter says `status: speculative`, but several passages use assertive language that doesn't match that status. "The remedy is automatic context injection" (paragraph 2) presents the design as the singular correct solution rather than a proposed one. "Vocabulary must be present for correct reasoning" (table row) asserts a necessity claim without evidence. The four-tier hierarchy in Reasoning ("The hierarchy becomes: 1. Always... 2. On reference... 3. On invoke... 4. On demand") is presented as a definitive rewrite of the loading model, not a speculative proposal. The speculative status and the prose register are in tension.
  Recommendation: Soften the assertive framing to match the speculative status. "One remedy is..." or "A natural candidate is automatic context injection." The hierarchy could be introduced with "Under this model, the hierarchy would become:" rather than "The hierarchy becomes:".

- [Proportion mismatch] The core claim is that statelessness creates a need for automatic injection. The Evidence section is heavily weighted toward the `definition` type — two subsections ("Definitions as the first case" and "The `definition` type") totaling roughly 250 words, compared to the "Beyond definitions" table which handles all other injection candidates in about 80 words. The note risks reading as "we should create a definition type" rather than its actual broader claim about automatic context injection in general. The definition type design (structural properties, title conventions, bounded length) is detailed enough to be its own note.
  Recommendation: Consider extracting the `definition` type design into a separate note. The current note's evidence section should give proportional treatment to the general injection need — perhaps with a worked example for ADRs or indexes, not just definitions.

INFO:
- [Source residue] The analogy "This would make definitions behave like imported constants in a programming language: declared once, available everywhere in scope" uses a programming-language framing. Given that the note's audience likely includes people reasoning about agent systems and programming, this is apt and explicitly framed as an analogy. However, the "ADRs | When modifying related code" row in the table introduces "code" as the context without hedging — ADRs in this KB relate to knowledge-system design decisions, not necessarily code. This is minor but could mislead about the KB's scope.

- [Anthropomorphic framing] "The agent doesn't need to know the definition exists" attributes a mental state ("know") to the agent. This is borderline — the note is about agent architecture, and "know" here is shorthand for "have in context." The note generally uses precise language ("the knowledge is in the KB but not in the context window"), so this one instance is a small inconsistency rather than a pattern.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus is present. The four-tier numbered list in Reasoning is a verbal hierarchy, not a pseudo-formal decomposition. The table in "Beyond definitions" uses prose descriptions, not notation. Clean.

- [Orphan references] The note references three specific definitional notes (codification, constraining, distillation) — all linked. The "Under 200 characters" claim about description length is a design aspiration stated in context, not an empirical measurement presented as fact. The "4-5K tokens" estimate in Caveats is explicitly framed as a rough calculation ("With 20 technical terms... might cost 4-5K tokens"), adequately hedged. No unsourced empirical claims found.

- [Unbridged cross-domain evidence] The note does not cite studies or empirical findings from external domains. All evidence is internal to the KB's own design context. The programming-language analogy (imported constants) is explicitly framed as analogy, not evidence transfer. Clean.

- [Redundant restatement] The opening paragraph establishes the statelessness problem. The Evidence section moves directly to the definition case without re-explaining statelessness. The Reasoning section introduces the loading hierarchy without restating the evidence. Each section advances the argument. Clean.

Overall: 2 warnings, 2 info
===
