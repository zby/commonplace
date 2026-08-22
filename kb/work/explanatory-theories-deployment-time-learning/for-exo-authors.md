# Exo can rewrite itself. Can retained theory improve the next rewrite?

> **Status:** Exploratory invitation from the Commonplace project. We have not contacted the Exo authors, and no response or endorsement is implied. The proposed treatment is ours; Exo does not claim or test it.

Exo provides a strong substrate for reflective self-improvement. Its agent can inspect and edit the source and self map that shape its behavior. It can also run mechanical checks, rebuild and restart the executor, retain facts, skills, prompts, tools, and code, and preserve the record of attempts across sandbox rewind.

These capabilities make self-change addressable and repeatable. They do not show that Exo maintains an explicit system theory, that a retained self-change improves behavior, or that one improvement helps produce the next. The proposed experiment separates these claims.

## The proposed treatment

In improvement episode `n`, the treatment requires Exo to record a working theory `tau_n` before the decision it will guide. The theory explains a failure or behavior through a mechanism, invariant, or other explanatory relation. It states its premises, scope, expected consequences, and a possible falsifier. Exo must then use those consequences in diagnosis, candidate search or choice, evidence acquisition, or outcome interpretation. A post hoc rationale does not count.

The stronger treatment retains an addressable and revisable `T_n` across episodes. A later episode retrieves an applicable part of `T_n` and uses it to form a working `tau_n`. Later evidence may support a separately judged `T_{n+1}`. Existing facts, skills, update reasons, event history, and code do not automatically constitute `T_n`; they qualify only if they perform this theory role.

Candidate acceptance and theory acceptance remain separate. A rewrite can work for the wrong stated reason, while a failed rewrite can reveal a useful counterexample. Exo's build, test, restart, and registry checks can reject mechanical faults, but they do not by themselves warrant a theory or establish better judgment.

This treatment tests theory-mediated self-improvement because the theory describes Exo and guides change through Exo's self-representation. Deployment time names the setting in which the evidence arises, not the update mechanism.

## One Exo experiment

Keep Exo's existing memory, skills, tools, prompts, edit paths, and raw episode history in every arm. Compare three arms:

1. direct reasoning over the available history with no required theory artifact;
2. a fresh `tau_n` reconstructed from the same history in every episode; and
3. a retained, revisable `T_n` that is retrieved and applied to form `tau_n`.

Hold the base model, observations, editable surface, actions, evaluator, and total resource budget fixed where possible. Use a task stream whose later episodes preserve the theory's mechanism, violate one premise, and invalidate the theory more broadly. Record whether an episode retrieved the theory, which decision the theory changed, and how the result affected a proposed theory revision.

Measure later improvement quality at a fixed total cost, or total cost at a fixed quality and harm bound. The cost account must include construction, retrieval, applicability checking, review, maintenance, stale-theory failures, and repair. The retained-theory arm succeeds only if it improves a later revision after those costs. Improving only the task that produced the theory does not qualify.

A behavioral canary provides one Exo-specific example. Suppose an earlier theory leads to a stronger evaluator. If that evaluator later rejects a judgment-degrading rewrite that the old checks would have admitted, the earlier benefit has helped a later improvement episode. A matched replay without the evaluator can test this dependence. Installing the canary alone establishes neither later use nor compounding.

The proposal loses if current Exo plus just-in-time reconstruction matches or beats retained theory, if the theory is stored but not used, or if stale and overbroad theories erase its gains.

## Questions for the Exo authors

- Which current Exo surface could host a separately addressable theory without confusing evidence, advice, and executable authority?
- Which real improvement episodes have strong enough independent evaluation for this comparison?
- What existing memory, skill, or self-update behavior would make the retained-theory arm redundant?
- How should an evaluator remain independent of the active rewrite while still being revisable in a separate episode?
- Which failure would you test first before allowing one retained theory to guide several self-changes?

## Supporting documents

- [Detailed Exo case](./exo-case.md) — why Exo is a suitable substrate, how `tau_n` differs from `T_n`, and what later-episode result would support compounding.
- [Exo evidence ledger](./exo-evidence.md) — pinned Exo and ExoWorker facts, adjacent positive and adverse evidence, unresolved gaps, and falsifiers.
- [Workshop experiment design](./experiment-design.md) — common controls for direct, deliberation-matched, fresh-theory, and retained-theory comparisons.

We welcome corrections to our reading of Exo and criticism of the proposed contrast, especially if current Exo already supplies the theory lifecycle or if the treatment cannot be isolated from ordinary deliberation.
