=== PROSE REVIEW: mcp-bundles-stateless-tools-with-stateful-runtime.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "Most tool operations are pure functions" and "The typical MCP tool surface — read a file, search for content, run a command, fetch a URL — is stateless" as established fact, but these are the note's own empirical claims about the MCP ecosystem without citation or grounding. Whether "most" tools are stateless is an assessable distribution claim that the note treats as obvious. Similarly, "Stateless functions are trivially testable" and "Stateless tools are embarrassingly parallel" are stated as axioms when they are engineering generalizations (stateless functions that call external services, for instance, are not trivially testable).
  Recommendation: Hedge the distributional claim ("In typical usage, most MCP tools appear to be stateless" or ground it with examples/data). The engineering generalizations about testability and parallelism could be softened to "largely" or "in the common case" to acknowledge edge cases.

- [Proportion mismatch] The core claim is in the title: MCP bundles stateless tools with a stateful runtime. The section that carries the most argumentative weight for this claim is "Most tools don't need state" (the empirical case that the bundling is unnecessary for the common case), but it gets only one short paragraph of evidence — a single sentence listing four example operations and then a concession paragraph about legitimate state. Meanwhile, "The state tax" section (the costs of the bundling) gets four developed bullet points plus a concluding sentence. The note over-invests in explaining WHY the bundling is costly and under-invests in establishing THAT the bundling is unnecessary — which is the more contestable premise.
  Recommendation: Develop "Most tools don't need state" with more concrete evidence — e.g., survey a few popular MCP servers and characterize which tools are stateless vs. stateful, or cite the MCP specification's own tool categories.

INFO:
- [Source residue] The note references "Claude Code's native tools" by name ("Read, Write, Grep, Bash are direct function calls") in the economic argument section. This is a concrete product example in a note that otherwise argues at the architectural/pattern level. It is framed as an illustrative example ("This is what Claude Code's native tools already are"), so it functions as intended — but it does anchor the note to a specific product rather than letting the pattern stand on its own.

- [Anthropomorphic framing] The phrase "State genuinely earns its keep" and "A database earns its complexity" and "Files earn their simplicity" use anthropomorphic language (earning, keeping) applied to architectural abstractions. This is conventional metaphorical language in software architecture writing rather than the model-cognition anthropomorphism the check targets, so it reads naturally. Flagging for completeness only.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus appears in the note. The argument is carried entirely in prose and structured lists. Nothing to flag.
- [Orphan references] No specific figures, data points, percentages, or named studies appear without attribution. The note makes architectural arguments rather than empirical claims with specific numbers.
- [Unbridged cross-domain evidence] The note stays within a single domain (software architecture / protocol design). The files-not-database analogy is explicitly framed as an analogy applied within the same domain ("the files-not-database argument applied to the tool layer"), not a cross-domain transfer. No bridging issues.
- [Redundant restatement] Each section opens with its own contribution. "The state tax" opens with costs; "Most tools don't need state" opens with the empirical observation; "The economic argument" opens with the analogy to files-not-database. No section re-explains a previous section's conclusion before proceeding.

Overall: 2 warnings, 2 info
===
