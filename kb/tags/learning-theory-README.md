---
description: "Curated head for the learning-theory tag — how systems learn, verify, and improve: accumulation, continual learning, verification, memory, and self-improvement, anchored on selection-based learning, with routes through its child areas"
type: types/tag-readme.md
---

# Learning theory

This tag gathers theory of how systems learn, verify, and improve: accumulation and generalization, continual learning after deployment, verification and error correction, memory architecture, and self-improvement. The anchor is [selection-based learning](../theory/definitions/selection-based-learning.md): each change to what a system retains for its later work is proposed, judged and can be rejected, with whether a change made the system better left as a separate question. Its members span notes and external system analyses, and apply to any system that adapts through retained artifacts, not only to KBs. [Deploy-time learning](./deploy-time-learning-README.md) covers what deployment reveals beyond design and testing and how people or systems respond. Nearby but different: [self-improving-systems](./self-improving-systems-README.md) holds systems that make operative changes to their own organization, while this tag covers learning in general, whether or not the learner revises itself.

Work also qualifies when it substantively meets the inclusion condition of a declared child: [deploy-time-learning](./deploy-time-learning-README.md), [constraining](./constraining-README.md), [discovery](./discovery-README.md), [artifact-analysis](./artifact-analysis-README.md), [agent-memory](./agent-memory-README.md), [llm-reliability](./llm-reliability-README.md), or [self-improving-systems](./self-improving-systems-README.md). Their definitions, mechanisms, and boundary analyses belong here without a separate claim of learning or retained improvement. This is inclusion in a subject area, not evidence that the system under discussion learns.

**Accumulation** — adding knowledge to the store — is the most basic learning operation, with [explanatory-reach](../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) as its key property: facts sit at the low end, theories at the high end. Accumulated knowledge is transformed by [constraining](../theory/definitions/constraining.md) and by working use-shaped artifacts out from it ([theory and methodology form a two-layer execution system](../theory/theory-and-methodology-form-a-two-layer-execution-system.md)); the conjecture phase of the [discovery lifecycle](../theory/definitions/discovery-lifecycle.md) posits the high-explanatory-reach theories that are accumulation's most valuable items, and [recognition](../theory/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) is the expensive step in getting there.

## Major child areas

These child tags route major parts of the area. A few fundamentals carry only the parent tag: [Learning is not only about generality](../theory/learning-is-not-only-about-generality.md) (Simon's definition of learning), [LLM learning phases fall between human learning modes](../theory/llm-learning-phases-fall-between-human-learning-modes.md), and [in-context learning presupposes context engineering](../theory/in-context-learning-presupposes-context-engineering.md). Outside the notes collection, [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) compares the external systems that learn from their own traces.

- [deploy-time-learning](./deploy-time-learning-README.md) — what use reveals beyond design and testing, and the maintenance and learning responses
- [constraining](./constraining-README.md) — narrowing the interpretation space, from conventions to deterministic code; codification, relaxing, and the decision heuristics
- [discovery](./discovery-README.md) — positing a general concept and recognizing particulars as its instances; explanatory-reach as what it produces
- [artifact-analysis](./artifact-analysis-README.md) — the four-field vocabulary (substrate, form, lineage, authority) for retained behavior-shaping artifacts
- [agent-memory](./agent-memory-README.md) — memory architecture: spaces, contamination, policy learnability, and the crosscutting decomposition
- [llm-reliability](./llm-reliability-README.md) — oracle theory, error correction, and the deviation taxonomy; the area applies verification concepts to LLM output deviations
- [self-improving-systems](./self-improving-systems-README.md) — systems that make operative, evidence-responsive changes to their own organization, from gradient learners to selection-based learners; its children cover selection-based learning, the improvement loop, reflection, warranted autonomy, and continual learning

## Start here

- [Selection-based learning](../theory/definitions/selection-based-learning.md) — learning by decided changes to what a system retains for its later work; names the process Commonplace runs, not an improved outcome
- [Program refinement](../theory/definitions/program-refinement.md) — one artifact's permitted behaviors inside another's; a checked narrowing is a refinement step, an unchecked output a candidate
- [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) — persistent cross-session adaptation through retained behavior-shaping artifacts, without weight updates
- [Learning is not only about generality](../theory/learning-is-not-only-about-generality.md) — accumulation with explanatory-reach as its key property; Simon's definition grounds the decomposition
- [Prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — reference choice separates conformance, requirement adequacy and the inspection burden
- [The verifiability gradient](../theory/verifiability-gradient.md) — compares task-specific checks, reset conditions and retry costs
- [Constraining and extraction can trade generality for reliability, speed, or cost](../theory/constraining-and-extraction-both-trade-generality-for-reliability.md) — how the two transforming mechanisms relate
- [Recognition, not linking, is the hard problem in knowledge systems](../theory/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — where connecting knowledge actually costs, and how naming amortizes it
- [Implementations do not establish shared semantics](../theory/implementations-do-not-establish-shared-semantics.md) — agreement on tests supports scoped conformance claims, not the inference from formalized consumers to symbolic inputs
- [Symbolic form holds consumers to a semantic reference](../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) — codification commits an interpretation by rewriting or adoption while keeping conformance and requirement adequacy separate
- [Near-decomposability may make local inspection affordable](../theory/near-decomposability-may-make-local-inspection-affordable.md) — conjectured mechanism for affordable local inspection; separates locating an intervention point from establishing that a repair preserves required invariants

## Related Tags

- [evaluation](./evaluation-README.md) — where learning claims meet oracles, warrant, and experiment design
- [document-system](./document-system-README.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents
- [context-engineering](./context-engineering-README.md) — where in-context learning meets the system layer that selects and organizes knowledge
