---
description: "Curated head for the learning-theory tag — how systems learn, verify, and improve, with routes through its major child areas and the fundamentals that sit under no child"
type: types/tag-readme.md
complete: true
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through durable artifacts.

The area is organized around [deploy-time learning](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) as the unifying framework. **Accumulation** — adding knowledge to the store — is the most basic learning operation, with [explanatory-reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) as its key property: facts sit at the low end, theories at the high end. Accumulated knowledge is transformed by [constraining](../notes/definitions/constraining.md) and by working use-shaped artifacts out from it ([theory and methodology form a two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md)); the conjecture phase of the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) posits the high-explanatory-reach theories that are accumulation's most valuable items, and [recognition](../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) is the expensive step in getting there.

## Major child areas

These child tags route major parts of the area. A few fundamentals carry only the parent tag: [learning is not only about generality](../notes/learning-is-not-only-about-generality.md) (Simon's definition of learning), [LLM learning phases fall between human learning modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md), and [in-context learning presupposes context engineering](../notes/in-context-learning-presupposes-context-engineering.md). Outside the notes collection, [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) compares the external systems that learn from their own traces.

- [deploy-time-learning](./deploy-time-learning-README.md) — the phenomenon: deployment meets users, surprises, and forces change after first release; what use reveals that design could not
- [constraining](./constraining-README.md) — narrowing the interpretation space, from conventions to deterministic code; codification, relaxing, and the decision heuristics
- [discovery](./discovery-README.md) — positing a general concept and recognizing particulars as its instances; explanatory-reach as what it produces
- [artifact-analysis](./artifact-analysis-README.md) — the four-field vocabulary (substrate, form, lineage, authority) for retained behavior-shaping artifacts
- [agent-memory](./agent-memory-README.md) — memory architecture: spaces, contamination, policy learnability, and the crosscutting decomposition
- [llm-reliability](./llm-reliability-README.md) — oracle theory, error correction, and the deviation taxonomy; the area applies verification concepts to LLM output deviations
- [self-improving-systems](./self-improving-systems-README.md) — theory builders and their warrant: systems that revise their own theories and machinery, the update architecture, and what licenses autonomy

## Start here

- [Theory builder](../notes/definitions/theory-builder.md) — localized theories that are consumed and criticized for what they say, with the result of criticism shaping the next conjecture; whether a builder learns is tested, not assumed. The [research companion](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) states the program's conjectures about builders
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — the unifying framework: persistent cross-session adaptation through retained behavior-shaping artifacts, without weight updates
- [learning is not only about generality](../notes/learning-is-not-only-about-generality.md) — accumulation with explanatory-reach as its key property; Simon's definition grounds the decomposition
- [agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — the underspecification foundation: spec-to-program projection and the constrain/relax cycle
- [the verifiability gradient](../notes/verifiability-gradient.md) — the ladder deploy-time artifacts sit on
- [both a narrowed and a use-shaped artifact trade generality for reliability, speed, and cost](../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) — how the two transforming mechanisms relate
- [recognition, not linking, is the hard problem in knowledge systems](../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — where connecting knowledge actually costs, and how naming amortizes it

## Related Tags

- [tags](./README.md) — the hub; applies learning theory to KB architecture and evaluation
- [document-system](./document-system-README.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents
- [context-engineering](./context-engineering-README.md) — where in-context learning meets the system layer that selects and organizes knowledge
