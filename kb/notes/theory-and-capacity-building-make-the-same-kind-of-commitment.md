---
description: "Theory building and capacity building both retain resolutions their evidence does not entail; an explanatory commitment stays answerable to the object it describes while a constructive commitment changes the object, so retraction differs in kind"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, self-improving-systems]
---

# Theory building and capacity building make the same kind of fallible commitment

Experience can prompt a retained change that later behavior depends on without determining what that change should be. When several explanations or responses remain compatible with the evidence, whatever the learner retains resolves part of that underdetermination. Since [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md), such a retained resolution is a commitment: content the evidence does not entail, fixed by the act of retaining it.

Software development runs on two forms of this act.

An **explanatory commitment** selects an account of how or why something works: a mechanism, a causal connection, a generalization and its scope. It is the [discovery lifecycle](./definitions/discovery-lifecycle.md)'s ampliative conjecture seen from the retention side, and what it changes is the theory through which later situations are interpreted.

A **constructive commitment** selects how future work will be done: an architecture, representation, tool, workflow, invariant, convention. What it changes is the learner's production machinery — learning surface, because [the deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md).

Both count as learning when the change responds to evidence and is retained operatively.

## The parallel breaks at what the commitment does to its object

An explanatory commitment remains answerable to the object it describes: the account can be wrong, and later evidence can show it wrong.

A constructive commitment changes the object. Once implemented, the selected design is part of the system's actual organization. The decision becomes ground truth: its reasons demote to provenance, and later theory must account for the organization it produced whether or not it was a good decision.

Project theory therefore has a historical component. Understanding a system means knowing not only what its current structure does but which constructive commitments produced it and what they were answering. This is why [design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md), and why [project-theory possession requires comparing new demands with existing organization](./project-theory-relates-new-demands-to-existing-organization.md): the comparison runs against the commitments behind the organization, not only its visible structure.

## Both sides need backtracking, but the paths differ

Neither commitment needs to be correct or permanent; later experience can defeat the reasons for retaining it. Retracting an explanatory commitment means revising the theory and reconsidering conclusions that depended on it. Retracting a constructive commitment means restructuring the machinery that embodies it and repairing what was built on it — supersession followed by reconstruction, not a change of mind.

Refactoring is the disciplined case on the constructive side: backtracking over a design commitment while preserving the externally observable behavior other commitments depend on. Broader retractions become redesign. At either scale the operation is the same — backtrack over a commitment, propagate the revision through its dependents — and it is part of what [holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) demands of a theory-holder. It is also why the current artifact alone can be insufficient for coherent modification: the learner needs enough theory to recognize which visible structures embody commitments and what else depends on them.

## Theory mediation is one causal path between the two forms

Capacity does not have to be built through theory: search, optimization, and trajectory reuse can turn experience into constructive commitments directly. The theory-mediated hypothesis singles out one path:

```text
experience
  -> explanatory commitment
  -> theory-guided constructive commitment
  -> changed production machinery
  -> new experience
  -> theory revision
```

Its value is empirical: if direct use of retained experience produces comparable capacity at comparable cost, the mediation loses support. What the path requires in order to run is stated in [theory-mediated self-improvement needs interpretation and retention](./theory-mediated-self-improvement-needs-interpretation-and-retention.md).

The reverse path runs regardless. A constructive commitment creates machinery, the machinery produces new experience, and that experience can support, narrow, or defeat the theory that guided the construction. The two kinds of commitment can co-evolve without collapsing into one kind of retained state.

## Scope

- The split classifies resolutions, not artifacts. One retained change often bundles both: adopting a convention commits an account of why the pattern works and machinery that enforces it. Classify per resolution, as the commitment boundary itself does.
- Derived organization — an episode index, a computed statistic — is a third kind of retained learning state, not a milder commitment. It is regenerable from retained ground truth and governed by recompute, on the other side of the derivation/commitment boundary. The explanatory/constructive split partitions the commitment side only; the three kinds do not form a spectrum.
- "Capacity" here means retained production machinery in the deployed-system sense. Whether a parametric weight update, which also resolves underdetermination but retains no inspectable resolution, supports the retraction machinery described here is left open.

## Open Questions

- Does an artifact recording both an explanation and a decision — an ADR is the usual case — need per-resolution classification for its maintenance regime, or does labelling by dominant regime suffice?
- Constructive commitments accumulate into structure faster than explanatory ones are tested. Is there a useful notion of a system carrying more design than its theory can currently account for, and does it predict modification failure?

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: supplies the derivation/commitment boundary and the ground-truth inversion the constructive side inherits
- [Discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: names the explanatory side's act — an ampliative conjecture — and the lifecycle that tests it
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: retained changes to prompts, tools, workflows, and other production machinery count as learning surface
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: why the premises behind constructive commitments must themselves be retained
- [Project-theory possession requires comparing new demands with existing organization](./project-theory-relates-new-demands-to-existing-organization.md) — extends: develops the historical component into a bearer test for open-ended modification
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — extends: places backtracking over commitments inside fallible theory-guided search
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: states the functional requirements of the mediated causal path
