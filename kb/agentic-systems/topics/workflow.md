# Workflow & Recovery

This topic follows multi-step work across delegation, verification, failure, resumption and delivery.

## Research questions

- How are tasks split, dependencies ordered and results integrated?
- Which gates must pass before work is accepted or delivered?
- What is retained after failure, and what must be repeated on resume?
- How are duplicate actions, stale results and interrupted workers handled?

## Design-space questions

Retained state, retry policy and ownership of external effects interact.
Which combinations let work resume without repeating effects or accepting
stale results? The [future-work agenda](./README.md#future-work) proposes
interruption tests around effect boundaries. A checkpoint mechanism alone
does not establish safe recovery.

## Inspect implementations

The [current workflow accounts](../comparisons/workflow/systems.md) link directly
to the corresponding member of each accepted analysis. Start with the system's
overview and boundary when interpreting a route: different analyses inspect
different versions and scopes.

The [workflow lens landing](../comparisons/workflow/README.md) explains that member's
scope. There is no structured comparison table or cross-system synthesis for
this lens yet. These questions are a research agenda, not findings about every
listed system.

[Agent Memory](./memory.md) provides related comparisons of retention and later
consumption. [Methods & Data](../methods.md) explains evidence levels;
[All research topics](./README.md) returns to the topic index.
