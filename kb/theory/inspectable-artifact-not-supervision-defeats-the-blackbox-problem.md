---
description: Readable scripts and validators let humans or agents inspect and revise individual rules in generated systems; neither symbolic membership nor human supervision alone supplies that inspection route
type: types/note.md
traits: [has-external-sources]
tags: [learning-theory, observability, constraining]
---

# Inspectable artifact, not supervision, defeats the blackbox problem

## The claim from ML

Chollet [observes](https://x.com/fchollet/status/2024519439140737442) that sufficiently advanced agentic coding is essentially machine learning: an optimization process (coding agents) iterates against a goal (spec + tests) until convergence, producing a blackbox artifact (the generated codebase) that is "deployed without ever inspecting its internal logic, just as we ignore individual weights in a neural network."

He predicts classic ML failure modes will follow: overfitting to the spec, Clever Hans shortcuts that don't generalize, data leakage, concept drift. And asks: what will be the Keras of agentic coding — the optimal high-level abstractions for steering this process?

## Where the framing breaks

The blackbox analogy holds only where the output is practically opaque for the behavior being inspected. Under the path on which a system runs a model as its interpreter, weights are [distributed-parametric](./definitions/representational-form.md): they do not expose separately addressed instruction-level rules. Readable scripts and validators do expose such rules where the artifact and its reference permit affordable inspection. Humans or LLMs can inspect their logic, review diffs, run tests, and revert changes. That route, not the reviewer's identity, is the relevant advantage.

Symbolic form alone does not supply it. A prompt is not symbolic merely because it is readable text; it becomes symbolic under a path that adopts a pinned model package, decoding included, as the reference for an operation. That codification can be opaque: reading the prompt does not expose the rule assigning its consequences. Large or obfuscated code can likewise obstruct inspection. The argument here concerns readable rules at an affordable inspection cost, not every symbolic artifact.

For that case, an LLM can review a diff and catch a Clever Hans shortcut in generated code, or compare an inspectable function against its specification and flag edge cases. Behavioral evals can detect failures in code or models; their availability is not the contrast. The distinctive route is locating and revising a separately stated rule against the failure, which a weight update does not expose under the instruction-level path.

## The failure mode mapping

Chollet's predicted ML problems have counterparts in artifact-level optimization. Code-extraction [codification](./definitions/codification.md) makes rule-level inspection and revision available where scripts or validators remain readable; the other mitigations below can also apply to learned models.

| ML failure mode | Artifact-level counterpart | Mitigation available |
|----------------|---------------------------|---------------------|
| Overfitting to spec | Goodharting on evals | Broader eval sets, LLM-as-judge on unseen cases |
| Clever Hans shortcuts | Bad assumptions codified confidently | Diff review (human or LLM), property-based tests |
| Concept drift | Model drift breaking prompts interpreted by a changing model | Regression evals, CI gates |
| Data leakage | Test/train contamination in eval suites | Held-out eval sets, adversarial test generation |

The specific inspection advantage is that a failed test can be compared with a readable rule and guide a local revision. Tests and held-out evals do not require that advantage: they can probe a model's behavior too. Neither inspection nor testing alone guarantees that the artifact satisfies its requirement.

## The real question

Chollet asks "what will be the Keras of agentic coding?" — the abstraction layer that lets humans steer codebase "training" with minimal cognitive overhead. The [verifiability gradient](./verifiability-gradient.md) is a candidate answer: it helps choose checks and decide which rules are ready to extract into scripts or validators. The constrain/relax cycle is the steering mechanism — commit stable patterns, relax when new requirements expose a bad commitment. The inspection-based version of this cycle requires readable rules and a capable reviewer, not necessarily a human. Adopting a model as the reference can codify an operation without supplying that inspection route.

---

Relevant Notes:

- [codification](./definitions/codification.md) — grounds: code extraction can make an interpreted rule inspectable in a script or validator; adoption-based codification need not
- [the verifiability gradient](./verifiability-gradient.md) — grounds: available checks guide extraction into readable scripts or validators
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — evidenced-by: embedding latent spaces are opaque artifacts; curated propositional links are inspectable — the adjacency-vs-connection distinction is inspectability applied to knowledge architecture
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: 1M lines of agent-generated code, fully repo-hosted, CI-gated, and PR-reviewed — inspectable artifacts at production scale with zero manual code
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](./agent-runtime-analysis-should-separate-scheduling-context-state.md) — component view: classes inspectable repo artifacts and tools under the external-state concern
