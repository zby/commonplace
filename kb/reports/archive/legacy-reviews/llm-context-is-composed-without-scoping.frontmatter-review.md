<!-- REVIEW-METADATA
note-path: kb/notes/llm-context-is-composed-without-scoping.md
last-full-review-note-sha: cfe3bacee167706de2ebc3c6f54da1bd5913ffff
last-full-review-note-commit: 6d965b8d2001a48306edf43a5c1b199ee11ead0f
last-full-review-at: 2026-03-24T20:55:45+01:00
last-accepted-note-sha: cfe3bacee167706de2ebc3c6f54da1bd5913ffff
last-accepted-note-commit: 6d965b8d2001a48306edf43a5c1b199ee11ead0f
last-accepted-at: 2026-03-24T20:55:45+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: llm-context-is-composed-without-scoping.md ===

Checks applied: 4

INFO:
- [Title-body alignment] The title names the problem ("composed without scoping") but roughly half the body argues the solution: sub-agents as lexically scoped frames, the return value problem, existing implementations, and speculative directions (tail-call optimisation, stack unwinding, recursion with clean frames). The note's central contribution is the scoping discipline proposal, not just the absence-of-scoping observation. A title like "sub-agents recover lexical scoping for LLM context" or "LLM context needs a scoping discipline borrowed from lexical scope" would better match what the body actually establishes. Noted as INFO rather than WARN because the note is `status: seedling` and the breadth is characteristic of exploratory writing that hasn't yet been split.

CLEAN:
- [Description discrimination] The description adds mechanism (flat concatenation), lists the three specific pathologies (spooky action at a distance, name collision, inability to reason locally), draws the dynamic-scoping analogy, and names the mitigation (sub-agents as lexically scoped frames). All four of these go well beyond the title's claim. Strong discrimination in a search result list.
- [Title composability] "since LLM context is composed without scoping, we need sub-agent isolation" reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Claim strength] Contestable: someone could argue that role markers (system/user/assistant) and XML delimiters already provide scoping. The note itself acknowledges these as "weak conventions" and argues they fall short of real scoping -- which is precisely the kind of specific, debatable position a claim title should stake out.

Overall: 0 warnings, 1 info
===
