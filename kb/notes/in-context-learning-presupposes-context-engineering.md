---
description: In-context learning only works when the right knowledge reaches the context window — the selection machinery that ensures this is itself learned and refined over deployment
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# In-context learning presupposes context engineering

Amodei [argues](../sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md) that continual learning may be unnecessary because pre-training + RL + in-context learning suffice. The claim treats in-context learning as a given capability — million-token windows can hold enough deployment-specific information within a session, so persistent cross-session adaptation adds little.

But in-context learning doesn't happen by itself. It only works when the right knowledge is already in the window. Something has to decide what "right" means, find the relevant knowledge, organize it, and load it — all before the model sees a single token. That something is [context engineering](./context-engineering.md): routing, loading, scoping, and maintenance.

Context engineering is not static infrastructure. It improves over deployment time. Teams learn which knowledge to route into context, how to structure it for the model, when to prune accumulated debris, and how to scope what each agent sees. This improvement produces exactly the artifacts the [deploy-time learning framework](./deploy-time-learning-the-missing-middle.md) describes: versioned prompts, routing rules, retrieval strategies, schemas, evals. These artifacts are durable, inspectable, diffable, and testable — everything that in-context learning alone is not.

Amodei's move is to eliminate weight updates during deployment. But in doing so he didn't eliminate learning — he relocated it. The learning moved from the model's weights to the system layer that feeds the model's context. That system layer is [continuously learning](./constraining-during-deployment-is-continuous-learning.md) in Herbert Simon's sense: it undergoes permanent changes that improve its capacity for adaptation.

The three [timescales](./llm-learning-phases-fall-between-human-learning-modes.md) remain necessary. Pre-training builds the general capability. In-context learning applies it within a session. Deploy-time learning builds the machinery that makes in-context learning effective — without it, the model has capability but no way to aim it at the right knowledge.

---

Relevant Notes:

- [context engineering](./context-engineering.md) — foundation: the machinery (routing, loading, scoping, maintenance) that in-context learning presupposes
- [deploy-time learning: the missing middle](./deploy-time-learning-the-missing-middle.md) — foundation: the framework that context engineering improvement belongs to; the artifacts it produces are the substrate of deploy-time learning
- [constraining during deployment is continuous learning](./constraining-during-deployment-is-continuous-learning.md) — extends: the system-layer adaptation that feeds context engineering meets Simon's definition of learning
- [LLM learning phases fall between human learning modes](./llm-learning-phases-fall-between-human-learning-modes.md) — extends: the three timescales remain necessary even if weight updates are eliminated; this note adds a dependency arrow between in-context and deploy-time
- [Dario Amodei ingest](../sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md) — responds to: Amodei's claim that continual learning may be unnecessary
