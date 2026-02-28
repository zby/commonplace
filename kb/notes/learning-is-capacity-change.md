---
description: Simon's definition — learning is any change that produces a more or less permanent change in a system's capacity for adapting to its environment. Capacity decomposes into generality and a compound (reliability+speed+cost) that trades against it; three mechanisms (stabilisation, crystallisation, distillation) operate on this trade-off differently.
type: note
traits: [has-external-sources]
status: seedling
areas: [learning-theory]
---

# Learning is capacity change

Herbert Simon: "Learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment." By this definition, almost every KB improvement is learning — even fixing a typo increases adaptive capacity because the system can now answer a question it would have confused before. The distinction isn't between "content change" and "capacity change" — all content changes improve capacity. But capacity is not a single dimension — it decomposes into several components that don't move in the same direction.

## Dimensions of capacity

### Generality — how widely does the capacity apply?

| Change | Scope | Example |
|--------|-------|---------|
| Fix a typo | One retrieval | System can now match a query it would have missed |
| Sharpen a description | One note's findability | All queries that might match this note work better |
| Add a connection | Two notes' mutual discoverability | Navigation between these ideas now exists |
| Define structured sections for a type | All future notes of that type | Every related-system note gets consistent structure |
| Discover a design principle | All future decisions in that area | "Types and directories are orthogonal" applies broadly |
| Improve methodology | All future KB operations | The verifiability gradient changes how everything stabilises |

Argyris's [single-loop vs double-loop learning](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) maps onto this axis as rough regions: single-loop corrects within existing rules (narrow scope), double-loop changes the governing variables themselves (wide scope) — discovering that [why directories despite their costs](../claw-design/why-directories-despite-their-costs.md), developing the [learning mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md), redesigning the [methodology enforcement approach](../claw-design/methodology-enforcement-is-stabilisation.md).

### Reliability, speed, cost — the learning compound

An LLM can multiply numbers. A calculator can multiply numbers. The calculator has far more capacity for multiplication — it never hallucinates 7×8=54, it handles arbitrarily large numbers, it runs in microseconds. But the LLM has more generality — it can also translate, summarise, write prose.

[Crystallisation](./deploy-time-learning-the-missing-middle.md) (prompt → code) is the most dramatic learning mechanism — it improves reliability, speed, and cost simultaneously by changing the substrate. Replacing an LLM validation check with a Python script doesn't change *what* gets checked — it changes how reliably (never hallucinates), how fast (milliseconds vs seconds), and how cheaply (free vs API call) it gets checked. These three dimensions move together because crystallisation is fundamentally a substrate change — from stochastic LLM to deterministic code. What you give up is generality: the script handles exactly what it handles, nothing more.

But the compound isn't exclusive to crystallisation. [Stabilisation](./agentic-systems-learn-through-three-distinct-mechanisms.md) (storing outputs, writing conventions) also improves reliability and speed, just less dramatically. [Distillation](../claw-design/skills-derive-from-methodology-through-distillation.md) (extracting procedures from reasoning) improves speed and cost by reducing context load. All three mechanisms trade generality for compound gains — they differ in how much and through what operation.

Learning cuts across Argyris's loops — it can be single-loop (crystallising one check into a script) or double-loop (deciding that [claim notes should use Toulmin-derived sections](../claw-design/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md)). What learning changes is the reliability+speed+cost compound, not the generality axis.

### Other dimensions

- **Composability** — a verified claim is more useful as a premise than an unverified one. The capacity gain isn't in the claim itself but in what other things can build on it. This may be a consequence of reliability rather than independent.

The list is likely incomplete. The point is that capacity is not a simple function of any single dimension — more generality sometimes means more capacity (the LLM handles novel situations no script could), more reliability sometimes means more capacity (the script never gets it wrong). All three learning mechanisms show that reliability, speed, and cost are correlated: they improve together as artifacts harden. The fundamental trade-off is generality against this compound. The optimal point depends on the task and the environment.

## Why this matters for the learning loop

The [KB learning loop](../claw-design/automating-kb-learning-is-an-open-problem.md) frames the open problem as needing automated mutations (extract, split, synthesise, relink, retire). These mutations differ on both axes:

**By generality:**
- **Extract, reformulate** — narrow scope, improving individual notes
- **Relink, regroup, synthesise** — medium scope, changing how knowledge connects
- **Retire, restructure** — wide scope, changing the system's organising principles

**By crystallisability** (reliability+speed+cost compound):
- **Crystallisable operations** (link checking, section validation, index regeneration) — already automatable as scripts, gaining reliability, speed, and cost simultaneously
- **Judgment operations** (is this claim worth keeping? should these notes merge?) — require LLM or human assessment, may crystallise later as patterns emerge

Automating narrow-scope improvements is relatively tractable (ingest pipelines, LLM extraction, validation scripts). Automating wide-scope improvements is the hard part — it requires judgment about what principles generalise. Crystallisation is a separate axis — often tractable regardless of scope, because the question "can this be made deterministic?" is itself fairly deterministic.

The [wikiwiki principle](../claw-design/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) addresses the UX side: by making each refinement step low-friction and in-place, narrow-scope learning (adding frontmatter, sharpening descriptions) happens continuously rather than in batches, freeing attention for the wide-scope judgment that can't be automated.

## Sources

- Herbert Simon: "Learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment."
- Chris Argyris: [Single-loop vs double-loop learning](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/) — single-loop corrects within existing rules; double-loop changes the governing variables.
- [Knowledge acquisition](https://en.wikipedia.org/wiki/Knowledge_acquisition) — extracting and structuring knowledge from sources; one region on the learning spectrum, not a separate activity.

Topics:
- [learning-theory](./learning-theory.md)
