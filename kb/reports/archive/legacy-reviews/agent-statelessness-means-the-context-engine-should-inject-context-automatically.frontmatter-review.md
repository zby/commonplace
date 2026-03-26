<!-- REVIEW-METADATA
note-path: kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md
last-full-review-note-sha: de8d3a0671b46cd00810fd582098a54eb6de6500
last-full-review-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: de8d3a0671b46cd00810fd582098a54eb6de6500
last-accepted-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agent-statelessness-means-the-context-engine-should-inject-context-automatically.md ===

Checks applied: 4

WARN:
- [Title-body alignment] The title claims the *need* for automatic injection, and the body explicitly states "The claim here is about the *need* for injection, not the mechanism." Yet the body devotes two full sections to a specific mechanism: a proposed `definition` type with concrete structural properties ("has examples, has negative examples, links to sibling definitions, bounded length") and an injection-strategy table covering definitions, area indexes, ADRs, and specs. This is mild scope drift -- the title promises a necessity argument but the body delivers both necessity and a substantial design proposal for how to fulfill it.
  Recommendation: Either broaden the title to acknowledge the design sketch (e.g., "Agent statelessness means the context engine should inject context automatically, starting with definitions") or extract the `definition` type proposal and the injection-strategy table into a separate note that this one links to. The current note tries to carry two claims: (1) injection is needed, and (2) definitions are the right first case with specific type properties.

CLEAN:
- [Description discrimination] The description adds concrete examples ("definitions once per session, ADRs when relevant") and explicitly scopes the claim ("the trigger mechanism is open; the need follows from statelessness"). These are mechanism and scope additions that the title alone cannot carry. An agent seeing this in search results alongside other context-engineering notes would know exactly what this note argues and what it leaves open.
- [Title composability] "since agent statelessness means the context engine should inject context automatically, we designed..." reads naturally as a sentence fragment. The title functions well as a linkable clause.
- [Claim strength] The claim is specific and contestable. A reasonable counterargument is that agents should learn to follow links on demand rather than having context pre-injected, or that the overhead of automatic injection (context budget, staleness) outweighs the cost of explicit loading. The note itself acknowledges these counterarguments in its Caveats section, confirming the claim is non-trivial.

Overall: 1 warning, 0 info
===
