---
description: "Cumulativity counts dependence through the retained result only; counting the evidence channel that result caused would make it coextensive with operativity"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Accumulation counts dependence through the retained result, not through the evidence it caused

Whether later improvement uses what earlier improvement retained is **cumulativity**: an informational dependence across episodes. A later episode builds on an earlier one when information introduced or selected by the earlier operative change shapes the later candidate, evaluation, update, or retained successor — the later episode may read or transform the retained state, compute an update at it, or apply a delta that preserves part of it.

Bare informational dependence, however, is satisfied by every operative change. [Operativity](./definitions/operative-change.md) already means the change affects subsequent operation over the relevant horizon, and affecting subsequent operation means affecting which evidence subsequently arises: an operative incumbent partly determines whether a viability bound is breached, whether a test fails, what a reviewer sees. A criterion that admits any dependence path from earlier retention to later improvement is therefore coextensive with operativity and separates nothing. Cumulativity has content only if it counts dependence through the retained result itself, holding fixed the evidence that result caused.

## The substitution test

To read cumulativity off a pathway, hold the later episode's new evidence and randomness fixed, then substitute a different earlier retained result. If the substitution changes the later improvement — because the result is consumed or preserved — the pathway is cumulative across those episodes. If the earlier result only governs behavior until an independently generated replacement overwrites it, it is operative but non-cumulative. Merely beginning while the earlier state remains operative does not count.

Clamping the evidence channel is what makes the test answerable about a specific mechanism rather than about a system in general.

## The clamped channel carries real influence

The exclusion is a commitment, not a simplification: the clamped path is a genuine dependence that the criterion declines to count.

Ashby's Homeostat is the clean case. Its retained setting both controls behavior and determines whether reorganization is triggered at all, so the incumbent shapes the very failure evidence that provokes its own replacement. Counting that would make the Homeostat cumulative — and by the same argument would make every operative self-change cumulative through its consequences.

The two channels come apart empirically, which is why the distinction is available at all. Once a Homeostat violation fires, [the next values come from the next entries of a random table](../sources/ashby-design-for-a-brain-ultrastability.md); holding the violation and table position fixed, substituting another incumbent leaves the successor unchanged. Dependence flows entirely through the trigger, and nothing about the earlier setting — not the values it used, not that it survived a while — reaches its successor. The narrower question the clamp isolates is the one the concept was introduced for: does the improvement process consume or preserve what an earlier episode worked out, or does it only replace it?

## Placements

**Cumulative and opaque.** Online gradient descent: the retained weights are the point at which the next gradient is evaluated and the base to which it is applied, so substituting different weights changes the update on identical data. Nothing is inspectable, so accumulation does not require reflection.

**Cumulative and non-reflective by design.** [Self-Improving Algorithms](../sources/self-improving-algorithms.md): a training phase learns task-relative distribution structure, then a stationary regime retains the tuned data structures as the operative basis for later inputs. Learned structure compounds without becoming an inspectable self-representation.

**Reflective and non-cumulative.** A controller whose runtime reads an editable `current-policy` file, and whose improvement routine responds to a viability violation by overwriting the whole file with the next policy from a fixed randomized table, without reading the incumbent or recording prior trials. Each policy is reflectively represented and operative between resets, and no result informs its successor. Representation is not accumulation.

**Operative and non-cumulative without representation.** The Homeostat above — the non-reflective version of the same failure.

## Scope

- Cumulativity is a reading over named episodes or a stated horizon, not a property asserted of a system. A pathway may carry some earlier changes forward and discard others, and the attribution inherits the declared horizon [membership is already read against](./definitions/self-improving-system.md).
- Which retained information counts as improvement-relevant depends on the criterion in play, so the reading is objective-indexed as well, [since self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md).
- Cumulativity says nothing about whether what accumulates is any good. A pathway compounds errors as dependably as it compounds gains.

## Open Questions

- **How much preservation counts.** "Applies a delta that preserves part of it" is graded while the criterion is binary. Gradient descent preserves nearly everything; an overwrite from an independent source preserves nothing; a routine that replaces most of a policy but keeps one clause sits uncomfortably between. Whether that threshold can be set principledly, or whether cumulativity should become a graded reading, is unsettled.
- **Aggregating over a run.** Reading a whole pathway rather than an episode pair needs some way to combine per-pair verdicts, and a count of cumulative pairs would meet the same commensurability difficulty [that blocks comparing per-function autonomy profiles](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).

---

Relevant Notes:

- [Operative change](./definitions/operative-change.md) — defined-in: the property cumulativity collapses into without the channel restriction
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: membership, and the declared horizon this reading inherits
- [Reflection buys addressability](./reflection-buys-addressability.md) — contrasts: what routing retention through a self-representation does add, which the reflective non-cumulative case shows is not accumulation
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why improvement-relevance, and so this reading, is objective-indexed
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: the same aggregation difficulty over a different profile dimension
- [Ashby's Homeostat](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: the operative-but-non-cumulative case, including the trigger-channel dependence the clamp excludes
- [Self-Improving Algorithms](../sources/self-improving-algorithms.md) — evidence: cumulative retention without an inspectable self-representation
