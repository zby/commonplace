---
description: "Reflection makes the system's own organization part of its action environment, so autonomous diagnosis may require an action-relevant self-model"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Reflection puts a system's own organization inside its action environment

An agentic process may select actions directly or through [a model it consumes while choosing an intervention](./an-action-model-matters-only-through-its-consumption-path.md). [Reflection](./definitions/reflective-system.md) creates a special case for model-mediated action: because reflective processes can act on a causally connected representation of their system's own organization, that organization becomes one of their possible intervention targets and part of the environment they must reason about.

Reflection alone does not require a comprehensive self-ontology: a process can append an explicit lesson without understanding the larger system. The stronger need arises when autonomous diagnosis and planning must locate evidence and choose an intervention. For Commonplace to perform that work computationally, it must distinguish enough of its artifacts, processes, dependencies, capabilities, and limitations to tell whether a problem belongs to a note, a type specification, a validator, or the runtime that executes it. Making every file editable is insufficient.

Today a human supplies much of that classification. Commonplace already retains fragments of a self-ontology in its types, collection contracts, ADRs, commands, and [reflective-system description](../reference/commonplace-as-a-reflective-system.md), but it is not yet clear which distinctions must become explicit and machine-operable for autonomous diagnosis and change. “Ontology” provisionally names those distinctions and relations; this note proposes neither a schema nor a new membership condition or profile axis.

## Open Questions

- Which distinctions about Commonplace must be retained rather than reconstructed by a model on each task?
- How should the ontology separate Commonplace from hosted models, runtimes, tools, and other dependencies?
- What evidence would show that an agent used the self-ontology to catch a bug, recognize a limitation, or interpret a genuinely new task?

---

Relevant Notes:

- [An action model matters only through its consumption path](./an-action-model-matters-only-through-its-consumption-path.md) — grounds: supplies the general agentic-action case that reflection narrows to the system itself
- [Self-improving system](./definitions/self-improving-system.md) — grounds: identifies operative, evidence-responsive change to the system's own organization
- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the causal self-representation that makes the system available as an object of action
- [A self-improving system needs a profile, not a ladder](./a-self-improving-system-needs-a-profile-not-a-ladder.md) — locates: treats this as an open question about reflective coverage rather than a new axis
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — extends: asks which aspects and relations a self-ontology would need to cover
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: describes the partial self-representation from which this investigation starts
