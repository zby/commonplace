---
description: "Backtracking preserves the provisional status of a heuristic branch choice by restoring an earlier usable state and redirecting search after contrary evidence"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Backtracking keeps lightweight search control provisional

A branch chosen by
[lightweight search control](./lightweight-search-control-allocates-further-search-without-licensing-adoption.md)
may be wrong. Backtracking keeps that choice provisional when the process can
preserve an earlier usable state, recognize evidence against the current
branch, return to that state, and redirect search.

Without an operative return path, a trial can become a de facto commitment.
Later work may depend on it, the prior state may become costly to recover, and a
judgment that was meant only to allocate search may acquire the consequences of
acceptance.

Backtracking does not show that the original heuristic was good. It also does
not recover spent effort or guarantee that contrary evidence will be noticed.
Its narrower function is to keep branch selection from becoming final merely
because the branch was tried.

## Scope

- Backtracking may restore an artifact, a plan, a theory state, or another
  search position; it is not limited to reverting code.
- A reversible branch can still cause irreversible external effects. The claim
  applies only to the state the process can actually restore.

---

Relevant Notes:

- [Lightweight search control allocates further search without licensing adoption](./lightweight-search-control-allocates-further-search-without-licensing-adoption.md) — grounds: supplies the provisional branch choice
- [Holding a program theory means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md) — extends: places backtracking inside longitudinal program modification and recovery
