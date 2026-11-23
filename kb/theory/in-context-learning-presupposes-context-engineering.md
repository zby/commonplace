---
description: In-context learning only works when the right knowledge reaches the context window — the selection machinery that ensures this is itself learned and refined over deployment
type: types/note.md
traits: [has-external-sources]
tags: [learning-theory, context-engineering, continual-learning, self-improving-systems]
---

# In-context learning presupposes context engineering

Amodei [argues](https://www.dwarkesh.com/p/dario-amodei-2) that continual learning may be unnecessary because pre-training + RL + in-context learning suffice. The claim treats in-context learning as a given capability — million-token windows can hold enough deployment-specific information within a session, so persistent cross-session adaptation adds little.

But in-context learning doesn't happen by itself. It only works when the right knowledge is already in the window. Something has to decide what "right" means, find the relevant knowledge, organize it, and load it — all before the model sees a single token. That something is [context engineering](./definitions/context-engineering.md): routing, loading, scoping, and maintenance.

Teams can revise the rules that supply context when a session reveals a routing error. If an agent misses a relevant decision, for example, the team can change the retrieval rule and test whether the next agent sees it. The [revised rule persists across sessions](./deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md); the contents of the first agent's context window need not.

Even if the model needs no further weight updates, a team can still improve the system that supplies its context. When the revised rule helps on later tasks, [the deployed system has learned](./constraining-during-deployment-can-produce-learning-outside-weights.md).

The distinction is [what survives the session](./llm-learning-phases-fall-between-human-learning-modes.md). Conditioning on a retrieved decision helps the current agent. Revising the rule that retrieves decisions changes what future agents can condition on.

---

Relevant Notes:

- [context engineering](./definitions/context-engineering.md) — foundation: the machinery (routing, loading, scoping, maintenance) that in-context learning presupposes
- [Deployed systems can learn from feedback with fixed model weights](./deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) — foundation: explains how a revised routing rule can affect later sessions without a weight update
- [Constraining during deployment can produce learning outside weights](./constraining-during-deployment-can-produce-learning-outside-weights.md) — extends: the system-layer adaptation that feeds context engineering meets Simon's definition of learning
- [LLM learning phases fall between human learning modes](./llm-learning-phases-fall-between-human-learning-modes.md) — extends: distinguishes using the current context from revising what later sessions receive
- [Dario Amodei ingest](https://www.dwarkesh.com/p/dario-amodei-2) — responds to: Amodei's claim that continual learning may be unnecessary
