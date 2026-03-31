"deploy-time learning" is used without an inline definition on first use:

> "That something is [context engineering](./definitions/context-engineering.md): routing, loading, scoping, and maintenance."

Context engineering is defined inline (routing, loading, scoping, maintenance) — pass for that term.

"deploy-time learning" appears on the second paragraph:

> "the artifacts the [deploy-time learning framework](./deploy-time-learning-is-the-missing-middle.md) describes"

The note links to the deploy-time learning note but provides no inline gloss for what "deploy-time learning" means. A reader encountering this term without prior KB context cannot infer from the surrounding sentence what kind of learning this refers to or how it differs from pre-training or in-context learning. The linked framework is the definition source, but per gate rules a link does not substitute for an inline definition.

Suggested fix: "the artifacts the deploy-time learning framework describes — the layer of system-level adaptation (versioned prompts, routing rules, evals) that happens between training and in-context execution."

"Herbert Simon's sense" is cited:

> "That system layer is [continuously learning](./constraining-during-deployment-is-continuous-learning.md) in Herbert Simon's sense: it undergoes permanent changes that improve its capacity for adaptation."

The inline gloss ("it undergoes permanent changes that improve its capacity for adaptation") adequately paraphrases what Simon's definition is. Pass.

"RL" is used as an abbreviation:

> "pre-training + RL + in-context learning suffice"

RL (reinforcement learning) is standard ML vocabulary. Pass.
