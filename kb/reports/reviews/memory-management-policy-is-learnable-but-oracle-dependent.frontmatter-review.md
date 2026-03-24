<!-- REVIEW-METADATA
note-path: kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md
last-full-review-note-sha: 00591dad032232f3de189e8cc5997e43c0c65aa9
last-full-review-note-commit: ac86be3f00c729bc7bff685d1338fcad43c3fb39
last-full-review-at: 2026-03-24T20:55:58+01:00
last-accepted-note-sha: 00591dad032232f3de189e8cc5997e43c0c65aa9
last-accepted-note-commit: ac86be3f00c729bc7bff685d1338fcad43c3fb39
last-accepted-at: 2026-03-24T20:55:58+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: memory-management-policy-is-learnable-but-oracle-dependent.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism (AgeMem stores facts in memory, learns policy in weights), scope (clean subsymbolic case of durable learning), and implication (depends on task-completion oracles the KB lacks). All three dimensions go well beyond the title's abstract claim, giving an agent enough to distinguish this note from related oracle or learning notes in search results.
- [Title composability] "since memory management policy is learnable but oracle-dependent, the KB's automation bottleneck is evaluation, not mechanism" reads naturally. The claim-form title composes as a sentence fragment without forcing awkward grammar.
- [Claim strength] The conjunction is genuinely contestable on both halves. Someone could argue memory management policy is too context-dependent to learn reliably, or that self-supervised signals could remove the oracle dependency. The "but oracle-dependent" qualifier is the specific, non-obvious part — it narrows a positive result (learnable) with a concrete limitation.
- [Title-body alignment] The body delivers on both halves of the title. "What it learns: the policy, not the operations" establishes learnability; "Why it works: the oracle" and "Comparison to KB learning" establish oracle dependency. The body extends into substrate splits and KB implications, but these serve the title's claim rather than drifting from it.

Overall: CLEAN
===
