<!-- REVIEW-METADATA
note-path: kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md
last-full-review-note-sha: 921002ef005a63091632fcb8c8db157d66bbe680
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 921002ef005a63091632fcb8c8db157d66bbe680
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description "Practitioner runtime taxonomies converge on three separable components — scheduler, context engine, and execution substrate — because each solves a different class of model limitation" adds mechanism (each component addresses a distinct model limitation) and context (convergence across independent practitioner sources) beyond what the title carries. An agent seeing this among search results for "agent runtime architecture" would know this note specifically argues a three-part decomposition grounded in model limitations, not a general survey or a single-vendor architecture.
- [Title composability] "since agent runtimes decompose into scheduler context engine and execution substrate, we designed each component independently" reads naturally as a sentence fragment. The title functions as a linkable prose clause.
- [Claim strength] The decomposition into specifically these three components is contestable — someone could argue for two components (control vs. environment), four (splitting the context engine into retrieval and framing), or entirely different cut lines. The note acknowledges this in its "Scope limits" section, which strengthens the claim by being explicit about boundaries. Note status is `seedling`, but the claim is already specific enough to be non-trivial.
- [Title-body alignment] The title promises a three-part decomposition; the body delivers exactly that. It defines the three components, maps a practitioner taxonomy onto them (the six-component table), connects each to existing KB theory, explains why independent sources converge on the same split, and scopes the claim's limits. No drift detected — the body neither undershoots nor overshoots the title's promise.

Overall: CLEAN
===
