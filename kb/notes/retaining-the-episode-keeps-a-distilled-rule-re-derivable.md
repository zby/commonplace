---
description: "Keeping relevant episode evidence and its relation to a distilled rule preserves a route for re-examining that rule; reconstruction, comparative value, and correct generalization still require testing"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [agent-memory, learning-theory, context-engineering]
---

# Retaining episode evidence keeps a distilled rule open to re-examination

An **episode** records the situation from which a lesson was drawn: a session,
execution trace, or worked case. A **rule** states the resulting generalization.
Keeping the relevant episode evidence and its connection to the rule preserves
a route for checking what supported the generalization and what it omitted.
It does not guarantee that another reading will reproduce the same rule or
that the original rule was correct.

This is one useful relation between retained forms, not a requirement to keep
every transcript. The question is whether the surviving record preserves the
premises needed to re-examine the lesson. A selected evidence packet may do so;
a complete-looking transcript may still omit a decisive observation or human
judgment.

## Evidence for reconstruction is not the reconstruction itself

A challenged rule can lead the house back to its recorded cases. The house may
then recover the original inference, revise its scope, or reject it. The result
is interpretation of evidence, not deterministic recomputation. A link to an
episode identifies a possible support path; the consumer must still inspect it
and judge what follows.

The analogy to a [two-layer execution
system](./theory-and-methodology-form-a-two-layer-execution-system.md) has a
limit. A rule may be the fast path, while episode evidence informs fallback
reasoning. The episode is not itself the reasoning process or a complete theory.
The model and other available knowledge also contribute.

Losing the episode removes this particular route of re-examination. It does not
make the rule immune to testing or leave trust and deletion as the only options.
New observations, independent evidence, and retained tests can still challenge
it. [Lineage records](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md)
help identify which earlier evidence a revision calls into question; they do
not replace that evidence.

## Distillation and acceptance are separate

A rule can be proposed after one episode. [The discovery
lifecycle](./definitions/discovery-lifecycle.md) distinguishes forming a
conjecture from accepting it; early distillation need not skip testing when its
status and scope remain explicit.

Recurrence can reveal that deriving the same lesson repeatedly is costly and
can motivate a retained fast path. Repetition alone does not establish the
rule's explanation or range. A single informative failure can also expose an
assumption and motivate a useful revision. Test consequences and alternative
accounts rather than making a fixed number of episodes the acceptance rule.

## Different forms preserve different things

A distilled rule can make an assumption easy to find, compare, and revise.
It can also omit context or retain a mistaken abstraction. An episode may
preserve details not selected by the original rule, but those details need not
be relevant or correctly interpreted later.

A fixed model can infer an explanation from cases, not merely imitate similar
ones. Conversely, it can follow a written theory mechanically. Storage form
alone therefore does not establish the reasoning mechanism or determine which
treatment transfers better. [Explicit
retention](./only-explicit-retention-is-durable-writable-and-addressable.md)
provides edit targets, not a guarantee that the target captures the useful
lesson.

Governance is possible at both levels. Rules can be versioned and retired;
episodes can be annotated, excluded from retrieval, or retained as evidence of
a rejected interpretation. Contradictory examples may require analysis, just as
contradictory rules may remain unnoticed or be applied inconsistently. Neither
form supplies its own reliable consumer.

## Comparing the retention choices

Compare cases alone, a distilled rule alone, and a linked combination using
the same source observations and comparable access and resource limits. Test
new cases both within the original account and after one of its assumptions
breaks. Count initial mistakes, recovery, collateral changes, and total cost,
including distillation, retrieval, and re-examination.

The combination earns its added storage and retrieval cost when the retained
evidence enables useful corrections that the rule alone cannot support
adequately. Cases alone may win when the model reconstructs the needed account
cheaply; a rule alone may suffice when the omitted details do not matter to the
assessed work. These are competing outcomes, not defects of the comparison.

## Scope

[Persistence and loading are separate
choices](./session-history-should-not-be-the-default-next-context.md).
Keeping an episode does not require loading it on every decision. A rule may
provide a cheaper default and linked evidence a targeted fallback, but the
routing must be evaluated too.

Both rules and episodes depend on their consumer. Pinning a model makes one
comparison more interpretable; it does not ensure exact replay or complete
recovery of the original understanding. This note concerns a retained route to
re-examination, not preservation of an entire prior mental or model state.

---

Relevant Notes:

- [Explicit retention provides direct targets for selective revision](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: explains why different records provide different revision targets without ranking their inference capacity
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: an episode can inform fallback but is not itself the generator
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: separates conjecture formation from acceptance
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — grounds: preserves the relation between a lesson and its evidence
- [Preserve evidence without making history the next context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) — extends: separates evidence capture from routine loading
- [Open-domain memory retention needs a declared output spec](./open-domain-memory-retention-needs-a-declared-output-spec.md) — contrasts: concerns which material to retain, rather than only its form
