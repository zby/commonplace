<!-- REVIEW-METADATA
note-path: kb/notes/instructions-are-typed-callables.md
last-full-review-note-sha: 7949fedfdeebc8bc24495d601366202d5cc0f192
last-full-review-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-full-review-at: 2026-03-24T20:55:27+01:00
last-accepted-note-sha: 7949fedfdeebc8bc24495d601366202d5cc0f192
last-accepted-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-accepted-at: 2026-03-24T20:55:27+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: instructions-are-typed-callables.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Skills and tasks are typed callables — they accept document types as input and produce types as output, and should declare their signatures like functions declare parameter types" closely paraphrases the title "Instructions are typed callables with document type signatures." The second clause ("should declare their signatures like functions declare parameter types") restates the title's "typed callables with document type signatures" nearly verbatim. The body's actual discriminating insight is the early-validation benefit: type annotations on instructions enable catching type mismatches before execution ("this document is an `index`, but this workflow operates on `structured-claim` — wrong type"). Leading with that mechanism would separate the description from the title.
  Recommendation: Replace the description with something that adds the mechanism or implication the title cannot carry, e.g.: "Type annotations on skills enable early validation — rejecting a document before execution when its type doesn't match the skill's declared input, the same way a type checker rejects a wrong argument."

CLEAN:
- [Title composability] "since instructions are typed callables with document type signatures, we can validate inputs before execution" reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Claim strength] The claim is specific and contestable — someone could reasonably argue that instructions don't need formal type signatures, that duck-typing or ad-hoc checking is sufficient, or that the overhead of declared signatures isn't justified. The speculative status is appropriate for the claim's maturity.
- [Title-body alignment] The title promises that instructions are typed callables with type signatures; the body establishes this by (a) framing skills/tasks as procedures whose primary affordance is execution, (b) arguing they should declare which document types they accept, and (c) providing a concrete signature table. The body delivers what the title claims.

Overall: 1 warning, 0 info
===
