<!-- REVIEW-METADATA
note-path: kb/notes/mcp-bundles-stateless-tools-with-stateful-runtime.md
last-full-review-note-sha: eef3a239ff7d83ba48be0a08bbd51205157df577
last-full-review-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-full-review-at: 2026-03-24T20:55:55+01:00
last-accepted-note-sha: eef3a239ff7d83ba48be0a08bbd51205157df577
last-accepted-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-accepted-at: 2026-03-24T20:55:55+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: mcp-bundles-stateless-tools-with-stateful-runtime.md ===

Checks applied: 4

WARN:
- [Description discrimination] The first clause of the description ("MCP forces stateless tool operations through a persistent server process") closely paraphrases the title ("MCP bundles stateless tools with a stateful runtime") — it restates the same bundling claim with slightly different words. The second clause ("most tools are pure functions that don't need session state, connections, or lifecycle management, but pay the complexity tax anyway") adds scope by naming the specific costs, but the overall description front-loads a restatement before reaching discriminating content.
  Recommendation: Lead with mechanism or implication that the title cannot carry. For example: "Most MCP tool operations are pure functions, but the protocol routes them through a persistent server that imposes lifecycle, connection, and concurrency costs — the files-not-database argument applied to the tool layer." This foregrounds the economic analogy (which is the note's distinctive framing) and drops the title paraphrase.

INFO:

CLEAN:
- [Title composability] "since MCP bundles stateless tools with a stateful runtime, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose clause.
- [Claim strength] The title makes a specific, contestable architectural observation — a defender of MCP could argue the stateful runtime is justified for all tools or that the overhead is negligible. The claim carries real information. No truism risk.
- [Title-body alignment] The body argues exactly what the title claims: most MCP tools are stateless but are forced through a stateful server, and this imposes unnecessary complexity. The body extends into the economic argument (files-not-database analogy) and the stateless-by-default alternative, both of which support the title's framing without drifting from it.

Overall: 1 warning, 0 info
===
