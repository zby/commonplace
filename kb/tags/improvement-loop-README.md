---
description: "Curated head for the improvement-loop tag — proposal-selection loops: search for candidates, reject-capable evaluation, operative retention, search control, backtracking, and oracle quality"
type: types/tag-readme.md
complete: true
---

# improvement-loop

The machinery of improvement loops: how candidate changes are searched for, evaluated with the possibility of rejection, and retained so that later operation depends on them. The establishing note is [a proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). The parent head's update-architecture distinction applies here: in a direct update, evidence determines a change that is always adopted, as with gradients; in proposal selection, a candidate can be rejected before it becomes operative. Most notes here are about proposal selection. What theory guides the search and how it is criticized belongs to [theory-builder](./theory-builder-README.md). A child of [self-improving-systems](./self-improving-systems-README.md).

## Loop structure

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — the three required functions
- [An omitted improvement-loop function and a frozen one need different repairs](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) — five systems with frozen functions, and why a direct update lacks a gate without omitting one
- [False-positive generation is filtered; false-positive acceptance becomes operative](../notes/false-positive-generation-is-filtered-before-retention.md) — why errors at acceptance cost more than errors at generation
- [Distinct residue classes require distinct functions in a self-improving architecture](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md) — different reasons a decision stays untransferred point to different missing functions

## Search and search control

- [Open-ended improvement must allocate search before decisive evaluation is available](../notes/open-ended-improvement-allocates-search-before-evaluation.md) — even a proof-gated loop must first choose what to develop
- [Lightweight search control allocates further search without licensing adoption](../notes/lightweight-search-control-does-not-license-adoption.md) — the authority of a search judgment stops short of an operative change
- [Backtracking keeps lightweight search control provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md) — restoring an earlier state keeps a heuristic branch choice revisable
- [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — judge the controller by the branches it routes on, not as acceptance claims
- [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) — the operative test for a retained failure explanation
- [Natural-language project state may specialize weight-resident search heuristics](../notes/natural-language-project-state-specializes-search-heuristics.md) — intent, theory, and branch history steer heuristics the model already holds
- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) — an observed loop: computational search, operator selection

## Evaluation and selection

- [Choosing what to learn requires both validity and learning-value gates](../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — trustworthy to learn from is a different check from worth learning
- [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — selection needs inspectable failure evidence, not only a winner-picking oracle
- [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — error analysis and judge discrimination come before automated optimization
- [Weakly discriminated qualities tend to be underselected](../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — what an oracle cannot tell apart, selection does not enrich
- [Oracle accumulation improves selection for later candidates in its maintained domain](../notes/oracle-accumulation-improves-the-selection-environment.md) — a failure kept as a maintained check improves later selection

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — the parent, whose update-architecture section places proposal selection beside direct update
- [theory-builder](./theory-builder-README.md) — the theories that guide search; shares the notes on theory-guided search
- [software-factory](./software-factory-README.md) — factory revision is one target a loop can retain changes into
- [reflection](./reflection-README.md) — loops whose retained changes pass through a self-representation
- [warranted-autonomy](./warranted-autonomy-README.md) — which evaluation and acceptance decisions a computational actor is warranted to take
- [continual-learning](./continual-learning-README.md) — retention that accumulates across many loop iterations
