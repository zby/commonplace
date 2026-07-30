---
description: Running a decomposition confirms only that it sufficed here; because many force-sets fit the same split, rationale retained at design time is what gives a transfer claim an antecedent to test
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning]
---

# Use tests a decomposition locally; retained rationale is what makes transfer testable

A decomposition — a split of a system, task, or corpus into parts with boundaries between them — gets validated by being used. The modules compose, the sub-agents finish the task, each piece fits its context window. That is real evidence for exactly one proposition: this split sufficed in the context that produced it. It is [an outcome check, and an outcome check licenses replay rather than a rule](./an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md). What a designer usually wants from a working decomposition is a rule — *split on this seam* — and that is a transfer claim about other contexts, which use never touched.

That note leaves open where the process evidence would come from. For a runtime trace the intermediate steps happened and can be inspected. A decomposition's process is the design reasoning, and it leaves no residue in the product: the boundaries are visible, the forces they answer are not. Many different force-sets are consistent with the same split, so inspecting the artifact cannot recover which one was operative — design-rationale methods exist for precisely this gap, IDEF6 capturing rationale where constraints do not determine a unique decision ([how Commonplace distributes rationale records](../reference/design-rationale-management.md)). Hence *retained*: the rationale is written at design time or it is gone, not merely inconvenient to find later.

## Local success barely discriminates

Use exercises a conjunction — these boundaries *and* this context — and reports one bit about the whole. The set of decompositions that pass is therefore large: a boundary that answers nothing, an over-split, a seam imported by habit from another system, all survive as long as they are not actively harmful. So local success fails to separate load-bearing boundaries from inert ones, and that separation is the whole of transfer. What carries to a new context is a boundary answering a force that is also present there.

Parnas's KWIC example is the clean demonstration: two modularizations of the same small indexing program, both working, both producing the same output, differing in whether module boundaries hide the decisions likely to change. Running either discriminates them not at all. The difference appears only under change and reuse — the transfer cases — and what predicts it is the criterion, not the module list the criterion produced.

## What a rationale must contain for the transfer claim to have an antecedent

A transfer claim is conditional: this split works where such-and-such holds. A conditional is testable only through its antecedent, and rationale supplies it by recording, per boundary, which of three things the boundary answers:

- an **inherited constraint** — what the substrate or consumer forced (an effective context bound, a tool surface, a review budget);
- a **local requirement** — what this problem needed and another might not;
- a **free choice** — what was underdetermined and settled by convenience.

With that split recorded, a new context is checkable before anything is rebuilt: do the constraints still bind, are the local requirements present, and which parts were never load-bearing at all. Without it the only available move is to rebuild and see — another local test, not a test of the transfer claim. The effect of retention is not that transfer succeeds more often; it is that "this transfers" moves from untestable to testable. This is the condition clause that [abstracting an experience into a lesson requires](./abstract-an-experience-only-when-you-can-state-the-boundary.md), supplied for the case where the episode is a design act rather than a trace, and it is why [the why is the part that carries past the original case](./first-principles-reasoning-selects-for-explanatory-reach-over.md).

## Retained-but-unfaithful is worse than absent

Post-hoc rationalization is the standing failure, and the asymmetry that makes [an unfaithful rationale worse than none for repair](./selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) reappears here unchanged. With no rationale, the transfer claim is untestable and visibly so; with a plausible but wrong one, the check runs against the stated force, passes, and the force that actually carried the local success is never examined. Retention makes the transfer claim testable; it does not make the test sound. What separates the two is intervention rather than reading — vary the stated force and see whether the decomposition's fit actually degrades.

## The claim's force scales with underdetermination

Change the premise and the conclusion moves. Where the problem determines the split — a protocol boundary, a hard data dependency, a transaction the external system will not let you straddle — the rationale is recoverable from the problem statement, retention buys little, and use approximates a test of the seam because there was nothing to choose. The gap this note names is proportional to how many alternative splits would also have worked locally, which is why it bites hardest on architecture and agent-team decomposition and barely at all on forced seams.

Repeated use across *varied* contexts is the other route, and it genuinely tests transfer — extensionally. Each new context that works narrows the region empirically. But it costs one full rebuild per sample and yields a list of contexts where the split held, never a statement of which feature carried, so it cannot answer the counterfactual (would this still hold if the review budget tripled?). Retained rationale is the intensional substitute for a sample nobody can afford.

## Nothing here is specific to splitting

The argument used three things: use exercises the whole configuration at once, the product underdetermines the reasons behind it, and a conditional needs its antecedent to be testable. Those hold for any design decision whose alternatives are discarded at design time — naming schemes, schema shapes, retrieval strategies, where a review gate sits. Decomposition is the sharpest instance because its discarded alternatives are maximally invisible: a working system displays its boundaries and never its rejected ones, so the artifact positively looks like its own justification.

## Scope

- The claim is about testability, not success. A complete and faithful rationale can describe a decomposition that transfers badly; it buys a test, not a result.
- Retention is required because the reasoning has to cross a boundary — another person, another session, a later self. Within the session that produced the split the rationale is still in context, and the requirement is invisible there, which is part of why it gets skipped. The default-off rate is measurable: auditing this repository's own architecture decision records before requiring an alternatives section found 4 of 56 carrying alternatives prose, and none carrying it as a heading ([ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)).
- The maintenance cost is unmeasured: rationale drifts as the decomposition is refactored, and drifted rationale is unfaithful rationale. Whether faithful retention stays cheaper than the extensional route at library scale is open.

## Sources

- [Parnas (1972), "On the Criteria To Be Used in Decomposing Systems into Modules", *CACM* 15(12)](../sources/parnas-1972-criteria-decomposing-systems-modules.md) — evidenced-by: two working modularizations of one KWIC program, distinguished by the information-hiding criterion rather than by anything observable in running them.

---

Relevant Notes:

- [An outcome check licenses replay; a rule needs the process verified](./an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md) — extends: names where the process evidence comes from when the thing verified is a design act, whose steps leave no inspectable residue in the product
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: transfer needs a statable condition clause, and retained rationale is what supplies one for a decomposition
- [Selective revision needs a faithful rationale, not just a legible one](./selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — grounds: the worse-than-none asymmetry for unfaithful rationale, which this note inherits for transfer testing rather than repair
- [An accepted edit verifies the change, not the rule](./an-accepted-edit-verifies-the-change-not-the-rule.md) — contrasts: same instance-versus-rule gap with human acceptance as the local oracle, where there is no discarded design alternative to retain
- [Decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — grounds: supplies the forces a rationale would record — context fit, verifiability of the boundary, merge cost
- [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — mechanism: the step table is retained rationale in worked form, keeping the per-step context needs the boundaries answer
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — extends: classifies whether a decomposition begins with conditional, transferred, or no scope warrant, then requires refutation-capable use to earn transfer
- [Design rationale management in Commonplace](../reference/design-rationale-management.md) — evidenced-by: records the inherited-constraint/local-requirement/free-choice distinction and observes from the other side that artifacts collapsing it make later transfer assessment harder
