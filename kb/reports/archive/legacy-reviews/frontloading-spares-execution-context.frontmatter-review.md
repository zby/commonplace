<!-- REVIEW-METADATA
note-path: kb/notes/frontloading-spares-execution-context.md
last-full-review-note-sha: 33a98602f115f927e65e6e589ceaee7bc5e0fce9
last-full-review-note-commit: cc365676b30ed9f3d77958177ab9107a32e2f046
last-full-review-at: 2026-03-24T20:55:09+01:00
last-accepted-note-sha: 33a98602f115f927e65e6e589ceaee7bc5e0fce9
last-accepted-note-commit: cc365676b30ed9f3d77958177ab9107a32e2f046
last-accepted-at: 2026-03-24T20:55:09+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: frontloading-spares-execution-context.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("partial evaluation applied to instructions with underspecified semantics") and scope ("pre-computing static parts of LLM instructions") beyond what the title carries. An agent seeing five results for "frontloading" or "execution context" could pick this note from the description alone -- it specifies both what kind of frontloading and the theoretical framing.
- [Title composability] "since frontloading spares execution context, we pre-compute file listings at build time" reads as a natural sentence fragment. No awkward grammar when linked.
- [Claim strength] The claim is specific and contestable. Someone could argue that execution context is not the primary bottleneck, that frontloading trades away freshness and flexibility for marginal savings, or that runtime derivation is preferable because it adapts to changing state. The claim takes a definite position.
- [Title-body alignment] The title promises that frontloading spares execution context, and the body delivers on this: the opening paragraph states the claim, "The context saving" section explains the mechanism, "What qualifies for frontloading" defines scope, and the PE section elaborates the theoretical framing. The PE material is substantial but is presented as explaining *why* frontloading works (mechanism behind the claim), not as a separate claim drifting from the title.

Overall: CLEAN
===
