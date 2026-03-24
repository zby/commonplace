<!-- REVIEW-METADATA
note-path: kb/notes/synthesis-is-not-error-correction.md
last-full-review-note-sha: 0b71cd23f8bae70af3ffef8231fa45ff7501a652
last-full-review-note-commit: 6b5b381a4b973131eb8ebd0e202a9057a5f97dd9
last-full-review-at: 2026-03-24T20:57:09+01:00
last-accepted-note-sha: 0b71cd23f8bae70af3ffef8231fa45ff7501a652
last-accepted-note-commit: 6b5b381a4b973131eb8ebd0e202a9057a5f97dd9
last-accepted-at: 2026-03-24T20:57:09+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: synthesis-is-not-error-correction.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds both mechanism and implication beyond the title. It explains HOW synthesis propagates errors ("merging all agent outputs") vs how voting corrects them ("discarding minorities"), then reframes a specific empirical finding (Kim et al.'s 17.2x amplification) as a synthesis failure rather than a general indictment of multi-agent coordination. An agent seeing this among search results would immediately know this note analyzes the synthesis-vs-voting distinction through the lens of specific empirical evidence.
- [Title composability] "since synthesis is not error correction, we need voting for redundant calls" reads naturally as a sentence fragment. The title works as a linkable prose clause.
- [Claim strength] The claim that synthesis and error correction are fundamentally different operations is specific and non-obvious. Someone could reasonably conflate them -- Kim et al.'s paper arguably does, by treating synthesis results as evidence against multi-agent coordination generally. The title names a distinction people actually miss.
- [Title-body alignment] The title claims synthesis is not error correction; the body establishes exactly this by defining synthesis vs voting as distinct operations with opposite failure modes, then demonstrates the distinction through two empirical cases (Kim et al. tested synthesis, MAKER tested voting). The reframing of Kim et al.'s results is an application of the title's claim, not a separate argument -- the scope holds.

Overall: CLEAN
===
