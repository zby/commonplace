---
description: "Agentic action can be direct or model-mediated; a retained action model matters only when its consumption path affects intervention selection"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, artifact-analysis]
---

# An action model matters only through its consumption path

An agentic loop can select an action directly from an observation and objective: a rule fires, a workflow advances, or a learned policy produces the next action. Alternatively, it can use a representation of the situation to diagnose what is happening, determine which actions apply, or compare their likely effects before acting. This second pathway is model-mediated only where the representation participates in action selection. An ontology that is stored but never consulted is inert, just as a policy that is documented but never loaded has no [behavioral authority](./definitions/behavioral-authority.md).

Model mediation becomes useful when the available evidence and objective do not determine an intervention directly. The common cases involve hidden or ambiguous state, heterogeneous components and tools, several plausible causes or actions, delayed consequences, competing constraints, or novel tasks that must be mapped onto known capabilities and limitations. The model may represent entities and relations, current state, affordances and preconditions, action effects, or some combination. An ontology is one explicit way to organize the entities and relations; it is not the only possible form and does not by itself supply predictions or action selection.

When such a representation persists for later loops, it is a [retained artifact](./definitions/retained-artifact.md), and the existing [four-field record](./axes-of-artifact-analysis.md) applies to its operative part and consumption path. Its representational form may be prose, symbolic, distributed-parametric, or mixed. Its lineage records the observations, specifications, or learning inputs it depends on and the changes that should invalidate it. Its authority record names the consumer, channel, and force that make it consequential: an acting model or planner may retrieve prose, query a graph, apply symbolic inference, or roll out a learned predictor to advise, constrain, rank, or select candidate actions. Storage substrate does not decide whether any of these paths exists.

A workflow may directly prescribe action; a validator may exclude actions; a policy may map state to action; an action model supports inference about the situation or interventions. One artifact can combine several of these operative parts, and one agentic system can use model-mediated selection for one pathway while directly executing another. The distinction therefore belongs to an action pathway, not to the system as a whole.

A representation reconstructed inside one context window can mediate the current action without being a retained artifact; persistence matters only when later loops can consume it. Self-improvement is a narrower application of the same architecture: the intervention changes the agentic system's own behavior-determining organization. In a reflective pathway, [that organization enters the represented action environment](./reflective-coverage-is-graded-across-representational-forms.md).

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — grounds: supplies the four-field record for a retained action model's operative part and consumption path
- [Behavioral authority](./definitions/behavioral-authority.md) — grounds: distinguishes a stored representation from one that actually influences action
- [Representational form](./definitions/representational-form.md) — grounds: separates prose, symbolic, distributed-parametric, and mixed action models
- [World models assess explanatory-reach through action-conditioned prediction](./world-models-assess-explanatory-reach-through-action-conditioned.md) — extends: develops the learned predictive route through candidate-action consequences
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — extends: its open questions apply the action-model argument when the intervention target is the system itself
