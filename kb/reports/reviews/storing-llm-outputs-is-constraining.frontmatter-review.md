<!-- REVIEW-METADATA
note-path: kb/notes/storing-llm-outputs-is-constraining.md
last-full-review-note-sha: d6185194fbba4c6719cb59e060df2a16f3656233
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:57:00+01:00
last-accepted-note-sha: d6185194fbba4c6719cb59e060df2a16f3656233
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:57:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: storing-llm-outputs-is-constraining.md ===

Checks applied: 4

WARN:
- [title-body alignment] The title "Storing LLM outputs is constraining" scopes to a single insight — that saving an LLM artifact is a constraining decision. The body establishes this in the first two paragraphs and the "applies broadly" list, but then extends into three additional sections ("Testing implications," "Generator/verifier: an alternative to constraining prompts," "Verbatim risk: the hardest verification failure") that argue distinct points about testing strategy, the generator/verifier tradeoff, and a specific verification failure mode. These sections use the core claim as a premise but each develops its own argument well beyond the title's scope.
  Recommendation: Either (a) tighten the body to the constraining-as-storing insight and spin the testing/generator-verifier/verbatim-risk material into their own notes, or (b) broaden the title to reflect what the body actually covers — something like "storing LLM outputs is constraining and that shapes how you test them" — though this may be too broad for a single claim title. Option (a) is probably cleaner: the generator/verifier section and the verbatim-risk section each carry enough weight for standalone notes.

CLEAN:
- [description discrimination] The description adds mechanism ("resolves semantic underspecification to one interpretation and freezes it against execution indeterminism") and context ("the same constraining move the parent note describes for code, applied to artifacts"). It explains why storing is constraining, not just that it is. Strong discriminator against other constraining-related notes.
- [title composability] "since storing LLM outputs is constraining, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose phrase.
- [claim strength] The claim reframes a mundane action (saving a file) as a specific theoretical operation (constraining in the KB's technical sense). Someone could reasonably view storing outputs as caching or saving work rather than as a constraining decision. The claim is non-obvious and contestable. Note status is "speculative," which is appropriate for the claim's maturity.

Overall: 1 warning, 0 info
===
