=== PROSE REVIEW: unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md ===

Checks applied: 8

WARN:
- [Source residue] The "Architecture" and "What assertions look like" sections use the connect skill as the sole worked example, with specific implementation details ("Bash (qmd commands, grep fallback), MCP semantic search tools, Grep, Glob, Read"; "connect-new is discovery-only"; "Attempted semantic search before falling back to grep"). The note's title and opening paragraph claim generality — unit testing LLM instructions — but the body reads like a design doc for testing the connect skill specifically. The connect skill is never introduced as an illustrative example; it appears as the subject.
  Recommendation: Either frame the connect skill explicitly as one example among possible others ("For instance, testing the connect skill would require mocking...") or generalize the architecture and assertion sections to use a generic skill, then add the connect skill as a concrete case study in a separate subsection.

- [Proportion mismatch] The core claim is that mocking the tool boundary enables unit testing of LLM instructions. The section that carries the most weight for this claim — "Architecture" (the general mechanism) — is roughly equal in length to "What assertions look like," which is entirely connect-skill-specific detail. Meanwhile, "This is constraining tooling" develops a secondary positioning argument (that this is an instance of constraining) at comparable length to the architecture section. The note's unique contribution — what it means to mock the tool boundary for instruction testing — gets thin treatment relative to the connect-skill worked example and the constraining positioning.
  Recommendation: Develop the architecture section with more general treatment of mock fidelity trade-offs, fixture design principles, and the boundary between behavioral and output assertions as general concepts. Consider whether the connect-skill material belongs in a separate note or a clearly demarcated example subsection.

INFO:
- [Confidence miscalibration] The opening paragraph states "This makes the tool layer the natural seam for dependency injection" as if it's established practice, but the note is status: seedling and the technique described is the note's own proposal. The phrasing is assertive ("the natural seam") rather than propositional. Similarly, "A test fixture has three parts" presents the decomposition as settled architecture rather than a proposed design. These are minor — the overall tone is appropriate for a design note — but they slightly overstate the maturity of the idea.

- [Anthropomorphic framing] Minimal concern. The note avoids attributing mental states to models. The phrase "any reasonable execution finds them" in Open Questions anthropomorphizes the execution slightly, but it's clearly informal shorthand in a question context, not a load-bearing claim.

CLEAN:
- [Pseudo-formalism] No formal notation is used. The note uses prose and bulleted lists throughout. No decorative formalism to flag.

- [Orphan references] No specific numbers, percentages, or named studies appear without citation. The "Five to ten notes suffice for most skill tests" in the Architecture section is a rough heuristic, not an empirical claim, and reads appropriately as design guidance.

- [Unbridged cross-domain evidence] The note operates entirely within its own domain (LLM instruction testing). It draws on software testing concepts (dependency injection, mocking, test fixtures, assertions) but these are the native vocabulary of the domain the note addresses, not cross-domain transfers requiring a bridge.

- [Redundant restatement] Each section opens with new content. The second paragraph of the introduction recaps the "doubled testing surface" from the linked programming-practices note, but this is necessary contextualization (establishing where this note fits), not restatement of something the note itself already said.

Overall: 2 warnings, 2 info
===
