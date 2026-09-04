---
description: "Theory-mediated system learning joins runtime self-modeling and self-adaptation with empirical refinement of fallible explicit theories; Workspace Optimization is a contemporary implementation analogy rather than the overall closest antecedent"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [learning-theory, deploy-time-learning, self-improving-systems, foundations]
---

# Theory-mediated system learning combines runtime self-modeling with empirical theory refinement

No single predecessor is closest to theory-mediated system learning on every
relevant dimension. A similarity claim must say what it compares:

- the **object and target** of representation — whether the retained model is
  about the modifying system's own structure, purposes, requirements, or goals;
- the **learning mechanism** — whether an explicit, fallible theory guides
  inference and is itself revised by empirical contradiction; or
- the **implementation pattern** — whether a contemporary LLM system learns by
  editing persistent code and text around a fixed model.

These dimensions identify different neighboring lineages. Collapsing them into
one ranking makes a recent system look closest because its software stack
resembles the current implementation, even when older work matches the
scientific question more directly.

## Runtime self-modeling and self-adaptation supply the structural lineage

[Computational reflection](../sources/maes-computational-reflection-1988.ingest.md)
introduced the central structural relation: a computational process operates
through a causally connected representation of selected aspects of itself.
[Models@run.time](https://doi.org/10.1109/MC.2009.326) developed runtime models
of a system's structure, behavior, or goals as machinery for inspection and
adaptation. [Requirements
reflection](https://doi.org/10.1145/1810295.1810329) proposed making
requirements first-class runtime entities so that a system could reason about,
explain, and modify them while it operates. Architecture-based systems such as
[Rainbow](https://doi.org/10.1109/MC.2004.175) used explicit architectural
models to monitor and adapt a running system.

This family is closest to **what the theory is about and what it changes**. The
represented object is the running system's own organization, requirements, or
goals, and the representation lies on a causal path into changes to that system.
That is closer to a retained program theory governing modification of the
behavior-determining system than a theory whose primary object is an external
environment.

The remaining gap is learning architecture. Classical runtime-model and
self-adaptive systems usually begin with a supplied model language, goal or
requirements vocabulary, monitoring boundary, adaptation operators, and
evaluation policy. They need not treat the runtime model as a fallible
explanatory theory whose content and scope are revised by delayed consequences,
and they generally leave these adaptation-machinery choices outside the
revision surface. Such choices belong to a [software house's production
machinery](./definitions/software-house.md) when they participate in the
complete producer, whether or not the house uses a Greenfield-style factory.
Their fixed placement limits claimed production reach when they carry required
task- or product-scope-specific production knowledge. It is not an inherent
defect when a component is warranted general machinery over the declared reach.

## Theory refinement supplies the epistemic lineage

[Explanation-based
generalization](https://doi.org/10.1023/A:1022691120807) is an established case
of theory-mediated learning: background theory determines what can be inferred
from an experience rather than merely accompanying an empirical learner.
[Theory refinement combining analytical and empirical
methods](https://doi.org/10.1016/0004-3702(94)90028-0) goes closer to the present
mechanism by beginning with an imperfect explicit theory, using empirical
failures to locate defects, and revising the theory rather than learning only
from scratch.

This family is closest to **how a fallible explicit theory learns**. The theory
shapes interpretation and search; evidence can count against the theory rather
than only against one candidate answer; and repair can be localized to the
represented knowledge that produced the failure.

Its usual target is nevertheless an external classification or problem domain,
not the purposes and architecture of the learning system itself. Classical
theory refinement therefore supplies the epistemic half of the proposed path
without supplying its reflective self-target.

## Workspace Optimization supplies a contemporary implementation analogy

[Workspace
Optimization](../sources/workspace-optimization-how-to-train-your-agent.ingest.md)
is unusually close to the present implementation pattern. It keeps the
foundation model fixed while making surrounding code and text editable, routes
prediction failures toward responsible artifacts, and replays prior transitions
after edits. Its persistent workspace is inspectable, executable, and consumed
by later model calls.

That makes it a strong precedent for non-weight learning surfaces, local credit
assignment, and counterexample-driven artifact repair. It does not make it the
overall closest antecedent to the research program. Its explicit theory
primarily models an external game environment within one run. Its role
decomposition, validation, and adoption policy remain supplied, and the
reported result does not establish cross-session recurrence of a revised theory
of the behavior-determining system itself.

Workspace Optimization should therefore be described as a **close contemporary
LLM-agent implementation analogue**, not ranked above the runtime
self-modeling, self-adaptation, and theory-refinement traditions.

## The proposed program joins the lineages

Theory-mediated system learning proposes one causally co-indexed longitudinal
path:

```text
addressable theory of a software system's purposes and organization
  -> theory-guided search, diagnosis, and modification
  -> change to the behavior-determining system
  -> independent or delayed consequence
  -> read-back against the same theory
  -> explicit theory revision
  -> changed later modification
```

Runtime reflection and self-adaptation supply the self-model and causal target.
Theory refinement supplies the fallible-theory and empirical-repair mechanism.
LLMs supply a current semantic interpreter and search process over theories that
have not been fully formalized. Persistent natural-language and symbolic
artifacts provide addressable working state, while code and runtime carry exact
transitions, checks, and continuity.

The further ambition is that required task- or product-scope-specific decompositions,
evaluators, and improvement methods can be computationally acquired or
challenged rather than supplied anew by people as the demand class widens. The
ambition does not require every general algorithm, runtime, interface, or
trusted kernel to modify itself. No source above establishes the complete
evidence-to-production-knowledge transition, and the current program has not yet
demonstrated it either. The combination is the research target, not a settled
novelty result.

## Consequences for comparison and experiment

Different neighbors imply different baselines:

- a **runtime self-model or architecture-based adaptation baseline** tests what
  claim-addressable natural-language program theory adds beyond an explicit
  but designer-supplied system model;
- an **explicit theory-refinement baseline** tests whether the proposed
  long-horizon self-modification setting adds more than classical correction of
  a fallible domain theory;
- a **Workspace Optimization baseline** tests the value of a program self-theory
  against editable external state, local failure attribution, and replay; and
- direct search, parametric adaptation, meta-learning, and stronger models test
  whether explicit theory is needed at all for the observed recovery or
  transfer.

A result showing only persistent artifact editing, fast adaptation, modular
reuse, or prediction-error correction would not identify the full mechanism.
The discriminating result must connect theory mediation, change to the modifying
system, empirical read-back, selective theory revision, and later changed
modification on one traceable path.

## Scope

- This note positions the program; it is not a complete literature review or a
  priority claim over every historical source.
- "Closest" is meaningful only after the comparison axis is stated. Structural
  precursor, epistemic mechanism, implementation analogue, and experimental
  competitor are different relations.
- A runtime requirements or architectural model is not automatically a program
  theory in the present sense. The comparison concerns its self-target and
  causal role, not an identity of concepts.
- A theory-refinement system is not automatically reflective. Explicit theory
  revision can concern a world outside the learner.
- Supplied adaptation machinery bounds the demonstrated reach when it embeds
  target-specific production knowledge. Human provenance or fixedness alone does
  not show that scoped learning or computational closure is incomplete.
- The proposed synthesis may turn out not to outperform simpler combinations of
  runtime models, direct search, artifact repair, and parametric adaptation.

## Open Questions

- What is the strongest implementation of requirements reflection or
  Models@run.time that can serve as a programming-agent baseline?
- Can a theory-refinement treatment be made information- and compute-comparable
  to the proposed retained-theory treatment?
- Does natural-language theory provide value beyond a structured runtime model
  when both expose the same purposes and dependencies?
- Which part of Workspace Optimization's advantage comes from editable state,
  local ownership, replay, or theory-level organization?
- Which supplied adaptation choices carry task-specific competence that the
  learning process must acquire, and which are warranted general machinery over
  the declared reach?

---

Relevant Notes:

- [A research program for learning software factories](../articles/automated-software-houses-with-fixed-llms.md) — context: states the combined program and its proposed interventions
- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the causally connected self-representation relation inherited from computational reflection
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: states the causally co-indexed path the synthesis must realize
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — extends: applies the theory-guided mechanism to longitudinal software modification and recovery
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why target-specific decomposition choices bound reach without making every fixed component defective
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places runtime models, artifacts, tools, code, and weights inside one learning boundary
- [Broad software demands create pressure for agentic factory development](./broad-software-demands-create-pressure-for-agentic-factory-development.md) — extends: states the production-knowledge acquisition burden that the further ambition requires
- [Workspace Optimization](../sources/workspace-optimization-how-to-train-your-agent.ingest.md) — exemplifies: supplies the contemporary editable-workspace implementation analogy and its bounded evidence
- [Maes, Computational Reflection](../sources/maes-computational-reflection-1988.ingest.md) — abstracted-from: supplies the causal self-representation lineage
