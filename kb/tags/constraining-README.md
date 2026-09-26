---
description: "Curated head for the constraining tag — narrowing the interpretation space of artifacts, from conventions to deterministic code; codification, relaxing, and the decision heuristics"
type: types/tag-readme.md
---

# constraining

Making semantics more focused by narrowing the space of valid interpretations an artifact admits — from partial narrowing (conventions) to full commitment (deterministic code). The primary mechanism for hardening deployed systems, with relaxing as its deliberate reverse. A child of [learning-theory](./learning-theory-README.md).

## Definition and spectrum

- [constraining](../notes/definitions/constraining.md) — definition and spectrum: definitions, conventions, structured sections, schemas, validators, and deterministic code
- [codification](../notes/definitions/codification.md) — the far end, where the medium itself changes from natural language to a symbolic artifact with formal semantics
- [agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — the foundation: the spec-to-program projection model, semantic boundaries, and the constrain/relax cycle

## Instances and techniques

- [Selecting an LLM output fixes a result, not its interpretation](../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) — boundary case: selection fixes result identity; it counts as constraining only when adoption also narrows which interpretations remain operative
- [constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md) — versioned constraining beats weight updates on inspectability and rollback
- [spec mining as codification](../notes/spec-mining-as-codification.md) — observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [error messages that teach are a constraining technique](../notes/error-messages-that-teach-are-a-constraining-technique.md) — in agent systems the error channel is an instruction channel
- [methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md) — review gates and validation as constraining applied to the KB's own methodology

## Deciding and reversing

- [codify-versus-LLM decision heuristics](../notes/codify-versus-llm-decision-heuristics.md) — four lenses on the codify-vs-LLM decision, with evidence they come apart at the edges
- [specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) — when to commit: before execution, during execution, or after repeated observation
- [progressive constraining commits only after patterns stabilize](../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — the default discipline: codify after the pattern proves the need
- [unified calling conventions enable bidirectional refactoring](../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — how to commit reversibly: neural and symbolic components behind the same callable interface
- [codification and relaxing navigate the bitter lesson boundary](../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — why reversibility matters: codification is a bet that may need relaxing
- [operational signals that a component is a relaxing candidate](../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — five testable signals for detecting when to reverse codification

## Related Tags

- [deploy-time-learning](./deploy-time-learning-README.md) — the post-release change constraining absorbs; the verifiability gradient locates constrained artifacts
