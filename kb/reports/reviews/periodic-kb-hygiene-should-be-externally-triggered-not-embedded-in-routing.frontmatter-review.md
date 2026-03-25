<!-- REVIEW-METADATA
note-path: kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md
last-full-review-note-sha: 039fa1424c08a751170c697c56987c9fc5d62fd4
last-full-review-note-commit: 09d91abac8ab71a82447d352a0fe42f760f1a853
last-full-review-at: 2026-03-24T22:35:15+01:00
last-accepted-note-sha: 039fa1424c08a751170c697c56987c9fc5d62fd4
last-accepted-note-commit: 09d91abac8ab71a82447d352a0fe42f760f1a853
last-accepted-at: 2026-03-24T22:35:15+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("Routing instructions load every session for high-frequency decisions") and implication ("periodic hygiene adds noise on every session while helping only occasionally, blurring routing and operations"). This goes well beyond restating the title -- it explains why the separation matters and names the cost of violating it.
- [Title composability] "since periodic KB hygiene should be externally triggered, not embedded in routing, we keep the default path lightweight" reads naturally as a sentence fragment.
- [Claim strength] The claim is specific and contestable -- someone could argue that embedding hygiene reminders in always-loaded routing is fine because the overhead is negligible, or that agents can skip irrelevant instructions without meaningful cost. This is a genuine architectural opinion, not a truism.
- [Title-body alignment] The body directly supports the title: it explains why routing instructions should optimize for high-frequency decisions, identifies periodic hygiene as low-frequency operational maintenance, names the two blurred responsibilities (routing vs operations), and points to the maintenance operations catalogue as the correct home.

Overall: CLEAN
===
