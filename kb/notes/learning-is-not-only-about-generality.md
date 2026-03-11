---
description: Per Simon, any capacity change is learning; accumulation is the most basic learning operation and reach is its key property — facts (low reach) vs theories (high reach); capacity also decomposes into generality vs a reliability/speed/cost compound
type: note
traits: [has-external-sources]
status: current
areas: [learning-theory]
---

# Learning is not only about generality

People equate learning with generality — knowing more, handling more cases, covering wider scope. But making something more reliable, faster, or cheaper is equally learning. A system that can now multiply without hallucinating has learned, even though it handles no new cases. The insight is that capacity is not a single axis.

Herbert Simon's definition grounds this: "learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment." By this definition, almost every KB improvement is learning. But not all capacity changes are equal: a typo fix and a design principle discovery both increase capacity, but on different dimensions and at different scales.

## Generality — how widely does the capacity apply?

| Change | Scope | Example |
|--------|-------|---------|
| Fix a typo | One retrieval | System can now match a query it would have missed |
| Sharpen a description | One note's findability | All queries that might match this note work better |
| Add a connection | Two notes' mutual discoverability | Navigation between these ideas now exists |
| Define structured sections for a type | All future notes of that type | Every related-system note gets consistent structure |
| Discover a design principle | All future decisions in that area | "Types and directories are orthogonal" applies broadly |
| Improve methodology | All future KB operations | The verifiability gradient changes how everything constrains |

The scope axis contains a qualitative distinction, not just a quantitative one. **Accumulation** — adding knowledge to the store — is itself a learning operation, and the most basic one. But what you accumulate varies in [reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md). At the narrow end are **facts** — "the key is on the table," a specific claim, a particular observation. At the broad end are **rules and theories** — "types and directories are orthogonal," a design principle, an abstraction. Both are genuine learning through accumulation. Reach is the property that distinguishes them: facts are adaptive knowledge (useful for the immediate context but don't transfer), while theories are explanatory knowledge (they apply in contexts they weren't designed for, because they capture structure rather than circumstance).

Fact accumulation is real and valuable — [AgeMem's](./memory-management-policy-is-learnable-but-oracle-dependent.md) 23-49% improvement on task completion comes entirely from storing and retrieving the right facts. But facts alone don't compound into deeper understanding. [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — positing an abstraction and recognizing particulars as instances of it — is the operation that produces theories, and theories are the highest-reach items accumulation can store.

Argyris's [single-loop vs double-loop learning](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) maps onto this axis as rough regions: single-loop corrects within existing rules (narrow scope), double-loop changes the governing variables themselves (wide scope).

## The compound — reliability, speed, cost

Capacity has a second cluster of dimensions that tend to move together: **reliability** (how consistently it works), **speed** (how fast), and **cost** (how cheaply). These form a compound because they often improve simultaneously — [codification](./codification.md) is the clearest example, where moving from LLM to deterministic code improves all three at once by changing the substrate. But the compound isn't exclusive to codification: conventions improve reliability, caching improves speed, distilled skills reduce cost.

The generality-vs-compound trade-off is the primary dynamic: [constraining and distillation both trade generality for compound gains](./constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). Learning cuts across Argyris's loops — it can be single-loop (codifying one check into a script) or double-loop (deciding that [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md)).

## Other dimensions

Generality and the compound don't exhaust what matters. A verified claim is more useful as a premise than an unverified one — not because it improves the system's current capacity, but because it improves its **capacity to learn further**, making the artifact load-bearing for future reasoning. Composability is a meta-capacity: the ability to build on what the system already knows.

## Sources

- Herbert Simon: "Learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment."
- Chris Argyris: [Single-loop vs double-loop learning](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) — single-loop corrects within existing rules; double-loop changes the governing variables.
- [Knowledge acquisition](https://en.wikipedia.org/wiki/Knowledge_acquisition) — extracting and structuring knowledge from sources; one region on the learning spectrum, not a separate activity.

---

Relevant Notes:

- [constraining and distillation both trade generality for compound](./constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — extends: the two mechanisms that operate on the generality-vs-compound trade-off defined here
- [constraining](./constraining.md) — one mechanism: constrains the interpretation space, trading generality for compound
- [distillation](./distillation.md) — the other mechanism: targeted extraction from reasoning under context budget constraints
- [codification](./codification.md) — the far end of constraining where the compound gain is largest
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient that structures the compound dimension
- [first-principles reasoning selects for reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — grounds: Deutsch's reach criterion distinguishes facts (adaptive, no reach) from rules (explanatory, reach)
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the operation that converts facts into rules by positing abstractions
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: AgeMem learns a policy for managing facts (when to store, retrieve, summarize) but operates entirely on facts, never producing rules or reach

Topics:

- [learning-theory](./learning-theory.md)
