---
description: Runtime structure and runtime governance are separable, but the runtime's structure determines which inspection, validation, correction, and drift-control operations governance can actually perform
type: note
traits: []
tags: [architecture, computational-model]
status: seedling
---

# Runtime structure determines the control surfaces available to governance

It is useful to separate runtime **structure** from runtime **governance**, but "separate axes" can be misleading if it implies independence. The structural decomposition answers what the runtime is made of: scheduler, context engine, execution substrate. Governance answers how the system is informed, validated, corrected, and kept from drifting over time. These are different questions, but governance is not free-floating. It can only operate through the control surfaces the runtime's structure exposes.

That is why governance should not be modeled as a fourth peer component beside scheduler, context engine, and substrate. A component owns part of normal execution. Governance functions cut across components instead: review may inspect outputs from the context engine, compare artifacts in the substrate, and then trigger corrective edits that alter future scheduling decisions. The role is supervisory, not a separate execution slot in the runtime anatomy.

## Why the distinction still matters

The split remains analytically useful because the two decompositions partition the system differently.

- **Structure** asks: what decides what happens next, what each call sees, and where exact state and actions live?
- **Governance** asks: how are those decisions and artifacts checked, constrained, corrected, and re-aligned over time?

Keeping these questions separate avoids a category error. Files, tools, and routing artifacts are not themselves validation or correction. Conversely, review gates and cleanup loops are not additional runtime anatomy; they are ways of steering the existing anatomy.

## Structural affordances for governance

Each structural component affords particular governance operations.

**Scheduler.** When progression logic is explicit, governance can attach retry limits, decomposition rules, delegation boundaries, escalation paths, and recovery policies to it. When scheduling is hidden inside a framework-owned chat loop, those governance operations become weak or indirect because the system cannot inspect or alter "what happens next" except through prompt advice.

**Context engine.** When context selection is explicit, governance can audit routing rules, check what entered a bounded call, measure compaction quality, and review whether the right materials were loaded. When context is inherited as an undifferentiated transcript, governance loses these handles; it can complain about prompt quality, but it cannot precisely govern loading decisions that were never externalized.

**Execution substrate.** When state lives in inspectable external artifacts, governance can diff, test, review, revert, compare SHAs, and detect staleness. This is the strongest governance surface because exact external state is easier to validate than hidden internal state. The substrate is therefore not just where actions land; it is also what makes strong governance possible.

## The dependence is asymmetric

The relationship is not symmetrical.

- Structure **affords and constrains** governance. A runtime with no inspectable substrate cannot support repo-style review and rollback. A runtime with no explicit context engine cannot support precise loading audits.
- Governance **hardens and reshapes** structure over time. Repeated review findings can turn into scripts, checks, or policy boundaries, making previously soft guidance part of the runtime's effective structure.

So the right picture is neither "one unified taxonomy" nor "two fully independent axes." It is a layered relationship: structural choices determine the control surfaces available to governance; governance exploits those surfaces to keep the runtime reliable over time.

## Consequence for runtime comparison

This changes how runtimes should be compared. It is not enough to ask whether two systems both have scheduling, context loading, and tools. The next question is whether those parts are exposed in a way that governance can act on them. Two runtimes can have similar structure but very different governance capacity because one externalizes its state and decisions while the other leaves them implicit.

The complementary [structure x governance matrix](./structure-governance-matrix.md) operationalizes this claim for commonplace by showing which governance operations are actually available on which structural surfaces.

---

Relevant Notes:

- [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — grounds: names the structural decomposition this note qualifies
- [Structure x governance matrix (commonplace)](./structure-governance-matrix.md) — operationalizes: shows the claim instantiated as a concrete matrix for this workshop
- [Methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md) — extends: describes one governance gradient that operates across the runtime rather than inside a single structural component
- [Semantic review catches content errors that structural validation cannot](../../notes/semantic-review-catches-content-errors-that-structural-validation-cannot.md) — exemplifies: review and validation are governance operations with different oracle and cost profiles
- [Inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: explains why externalized exact state gives governance unusually strong control surfaces
