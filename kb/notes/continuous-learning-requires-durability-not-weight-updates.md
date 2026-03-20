---
description: The real disagreement is whether durable changes to tips, prompts, rules, schemas, tests, and memory artifacts count as learning; Simon's capacity-change definition says they do
type: note
traits: []
tags: [learning-theory]
status: current
---

# Continuous learning requires durability, not weight updates

When AI labs discuss "continuous learning," they usually mean weight updates during or after deployment: online learning, fine-tuning on logs, replay buffers, RL from interaction. That is a real form of continuous learning, but it is not the only one.

The stronger claim is simpler: **continuous learning requires durable adaptive change, not specifically weight change**. Herbert Simon's definition in [learning is not only about generality](./learning-is-not-only-about-generality.md) is the key test: learning is any change that produces a more or less permanent change in a system's capacity for adapting to its environment. By that standard, a system also learns when it accumulates durable symbolic artifacts that change future behavior: tips mined from trajectories, prompts revised from experience, schemas that reject previous failures, tests that catch recurring mistakes, rules and procedures that guide later runs.

The unexamined assumption is that "capacity change" requires parameter change. But when a system improves across sessions and the improvement lands in an inspectable artifact rather than parameters, the same standard applies. If the artifact persists and later behavior depends on it, capacity has changed — Simon's definition is satisfied regardless of the medium.

[In-context learning](./in-context-learning-presupposes-context-engineering.md) reveals where the real boundary lies. A better next answer caused by something still sitting in the current context window is not continuous learning, because the change evaporates when the session ends. Once the improvement is promoted into a durable substrate, the system has crossed from transient adaptation to continuous learning. The important boundary is **ephemeral vs durable**, not **weights vs not-weights**.

This substrate lens organizes systems that otherwise look unrelated. [Trajectory-informed memory generation](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) and [constraining during deployment](./constraining-during-deployment-is-continuous-learning.md) differ in mechanism, oracle strength, and artifact form, but both produce durable capacity change through inspectable artifacts — which is the only thing the definition requires.

Weight updates and symbolic artifacts are two learning substrates, not a real case and a metaphorical one. The interesting question is no longer "is this really learning?" but "what does each substrate buy or sacrifice?"

---

Relevant Notes:

- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: Simon's definition makes capacity change, not weight change, the criterion
- [constraining during deployment is continuous learning](./constraining-during-deployment-is-continuous-learning.md) — exemplifies: versioned prompts, schemas, tools, and tests are one concrete artifact-side learning loop
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — extends: artifact-side learning fills the durable middle between weight training and ephemeral context
- [Learning substrates, backends, and artifact forms](./learning-substrates-backends-and-artifact-forms.md) — extends: names the main non-weight substrate family and separates substrate class from storage and artifact choices
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is the unsurprising weight-side case; this note argues the artifact-side case is learning too
- [trace-derived learning techniques in related systems](./trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems already split cleanly into weight-promotion and artifact-promotion loops
