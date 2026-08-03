---
description: "Definition — evidence bears on an improvement objective when it carries information about the criterion: gradients, rewards, errors, viability signals, tests, judgments; no evaluator required"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Evidence bearing on an improvement objective

Evidence **bears on an improvement objective** when it carries information about how the system stands relative to that objective, and a change is **responsive** to it when the evidence causally shapes the change — what is changed, how much, or whether it is kept. This is the clause that makes a [self-improving system](./self-improving-system.md)'s changes improvement-directed rather than merely caused, and it is deliberately indifferent to architecture.

## Scope

The evidence can be any signal diagnostic of the criterion:

- **gradients and error signals** — derived from a loss the objective defines;
- **rewards** — returns from an environment against a reward function;
- **viability signals** — essential variables leaving or re-entering declared bounds;
- **test results, proofs, and validator verdicts** — mechanical checks against a stated contract;
- **measurements and usage traces** — observed performance, incidents, benchmark outcomes;
- **human judgments** — review verdicts, maintainer standards, rubric applications.

A counterfactual test makes the causal clause operational: hold the incumbent and other relevant updater inputs fixed, then remove or replace the evidence. What the updater computes or installs must change — or, for a stochastic updater, its distribution must change. Retrieval, parsing, or logging alone does not establish responsiveness if the resulting update is unchanged.

The evidence does **not** need to appear in a separate evaluator component. In direct-determination pathways the update rule consumes it wholesale — the gradient step *is* the response. Only the [proposal-selection subtype](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) implements the criterion as a gate that consumes evidence to accept or reject.

## Exclusions

- **Uninformative triggers.** A timer, a fresh request, an unconditional event — these cause changes without carrying any information about the objective. Change on trigger alone is self-modification, not self-improvement.
- **Idle evidence.** Evidence that exists but does not causally affect the change makes nothing responsive; a dashboard nobody's update rule or judgment consumes bears on the objective and changes nothing.
- **Evidence of the wrong thing.** A signal diagnostic of some *other* criterion can drive changes that are responsive — to that other objective. Which objective the evidence bears on decides what the system is directed at, [and directedness is all it decides](./self-improving-system.md).
- **Objectives specified by the change.** Relabelling the target of an existing update — reading gradient steps on a loss as improvement toward *whatever these weights now do better* — leaves the causal history untouched while making the criterion trivially satisfied. Every operative self-change admits such a relabelling, so causal shaping alone does not screen it out: the objective must also be [specifiable independently of the change it is invoked to license](../self-improvement-is-relative-to-a-declared-objective.md).

## Misuse Cases

- Treating any input the system reacts to as improvement evidence — reaction is not responsiveness to a criterion.
- Requiring the evidence to flow through an explicit gate — that is the subtype's architecture, not the semantic requirement.
- Reading evidence-responsiveness as evidence of improvement — a faithful response to a mis-specified objective degrades the system exactly as responsively.

---

Relevant Notes:

- [Self-improving system](./self-improving-system.md) — defined-in: the definition whose evidence-responsiveness clause this term sharpens
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: the subtype where the evidence is consumed by an explicit evaluator
- [Oracle strength spectrum](../oracle-strength-spectrum.md) — extends: grades what different evidence suppliers can establish, where an evaluator exists to consume them
- [Self-improvement is relative to a declared objective](../self-improvement-is-relative-to-a-declared-objective.md) — extends: why causal shaping needs independent specifiability beside it, and what the objective's declared standing adds to the attribution
