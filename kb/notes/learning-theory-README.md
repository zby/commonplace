---
description: "Curated head for the learning-theory tag — how systems learn, verify, and improve; routes to the covered child tags listed in covered_by."
type: kb/types/tag-readme.md
index_source: tag
index_key: learning-theory
covered_by: [deploy-time-learning, constraining, distillation, discovery, artifact-analysis, agent-memory, llm-interpretation-errors]
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through durable artifacts.

The area is organized around [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) as the unifying framework. **Accumulation** — adding knowledge to the store — is the most basic learning operation, with [reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) as its key property: facts sit at the low end, theories at the high end. Two orthogonal mechanisms ([constraining](./definitions/constraining.md) and [distillation](./definitions/distillation.md)) transform accumulated knowledge; a third operation ([discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)) produces the high-reach theories that are accumulation's most valuable items.

## The kinds of notes under this tag

Every note carrying `learning-theory` also carries at least one of these child tags (enforced by validation — the typed routing below is trustworthy):

- [deploy-time-learning](./deploy-time-learning-README.md) — the framework itself: adaptation through durable inspectable artifacts, learning fundamentals, and feedback quality
- [constraining](./constraining-README.md) — narrowing the interpretation space, from conventions to deterministic code; codification, relaxing, and the decision heuristics
- [distillation](./distillation-README.md) — targeted extraction of use-shaped artifacts from larger reasoning
- [discovery](./discovery-README.md) — positing a general concept and recognizing particulars as its instances; reach as what it produces
- [artifact-analysis](./artifact-analysis-README.md) — the four-field vocabulary (substrate, form, lineage, authority) for retained behavior-shaping artifacts
- [agent-memory](./agent-memory-README.md) — memory architecture: spaces, contamination, policy learnability, and the crosscutting decomposition
- [llm-interpretation-errors](./llm-interpretation-errors-README.md) — oracle theory, error correction, and reliability; the error-theory area applies verification concepts to LLM interpretation failures

## Start here

- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — the unifying framework: three timescales of system adaptation
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — accumulation with reach as its key property; Simon's definition grounds the decomposition
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — the underspecification foundation: spec-to-program projection and the constrain/relax cycle
- [the verifiability gradient](./verifiability-gradient.md) — the ladder deploy-time artifacts sit on
- [constraining and distillation both trade generality for reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability.md) — how the two transforming mechanisms relate
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the third operation, and why recognition is its hard problem

## Related Tags

- [tags](./tags-README.md) — the hub; applies learning theory to KB architecture and evaluation
- [document-system](./document-system-README.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents
- [context-engineering](./context-engineering-README.md) — where in-context learning meets the system layer that selects and organizes knowledge
