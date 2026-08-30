---
description: "A search judgment is lightweight when its authority stops at allocating further investigation, probing, continuation, suspension, or abandonment rather than licensing an operative change"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Lightweight search control allocates further search without licensing adoption

[Open-ended improvement must allocate search before decisive evaluation is
available](./open-ended-improvement-allocates-search-before-evaluation.md).
Call a judgment **lightweight search control** when its authorized consequence
is limited to changing which branch receives further search. It may make a
question worth investigating, select a probe, continue or suspend a branch, or
redirect effort elsewhere.

The same judgment does not by itself license an operative change. "Worth
investigating" and "warranted to adopt" are different conclusions. The first
may rely on evidence too weak for the second because the selected branch remains
subject to stronger evaluation before adoption.

"Lightweight" names the judgment's authority, not its cost, formality, or
confidence. A costly analysis can remain lightweight when it only allocates
further search. A cheap rule can be an acceptance control when passing it makes
a change operative.

## Scope

- Lightweight control can still waste resources or systematically miss valuable
  branches. Limited authority does not make the controller effective.
- The claim does not specify how search should be allocated or what evidence is
  sufficient for adoption.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: separates bringing a candidate into consideration from accepting it
- [Operative change](./definitions/operative-change.md) — defined-in: supplies the horizon-relative behavioral threshold that lightweight search control cannot cross by itself
- [Backtracking keeps lightweight search control provisional](./backtracking-keeps-lightweight-search-control-provisional.md) — mechanism: explains how restoring an earlier usable state prevents a branch trial from becoming a de facto adoption
- [A search controller is tested by what it brings to stronger evaluation](./a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — extends: gives the distributional evaluation appropriate to a controller whose judgments do not claim acceptance authority
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: explains why search can use weaker authority than adoption when bad candidates still face a downstream filter
