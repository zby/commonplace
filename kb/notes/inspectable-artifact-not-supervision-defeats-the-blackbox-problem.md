---
description: Chollet frames agentic coding as ML producing blackbox codebases — codification counters this not by requiring human review but by choosing readable artifacts (code, prompts, schemas) that any agent can inspect, diff, test, and verify
type: kb/types/note.md
traits: [has-external-sources]
tags: [learning-theory, observability]
status: current
---

# Inspectable artifact, not supervision, defeats the blackbox problem

## The claim from ML

Chollet [observes](https://x.com/fchollet/status/2024519439140737442) that sufficiently advanced agentic coding is essentially machine learning: an optimization process (coding agents) iterates against a goal (spec + tests) until convergence, producing a blackbox artifact (the generated codebase) that is "deployed without ever inspecting its internal logic, just as we ignore individual weights in a neural network."

He predicts classic ML failure modes will follow: overfitting to the spec, Clever Hans shortcuts that don't generalize, data leakage, concept drift. And asks: what will be the Keras of agentic coding — the optimal high-level abstractions for steering this process?

## Where the framing breaks

The blackbox analogy holds only if the output is practically opaque. Neural network weights are [distributed-parametric](./definitions/representational-form.md) (encoded across numerical parameters) and opaque to any ordinary inspector — human or LLM. But readable artifacts (prompts, schemas, evals, deterministic code) are inherently inspectable at useful scales. They can be diffed, tested, reverted, and reviewed — by humans or by LLMs. The artifact's representational form is what matters, not who reviews it.

An LLM can review a diff and catch a Clever Hans shortcut in generated code. It can run evals and detect overfitting to the test suite. It can compare a codified function against its specification and flag edge cases. None of this is possible with weight updates — not because LLMs lack judgment, but because weights lack structure.

## The failure mode mapping

Chollet's predicted ML problems map directly to [codification](./definitions/codification.md) failure modes — but with mitigations that weight-based systems can't match:

| ML failure mode | Codification equivalent | Mitigation available |
|----------------|---------------------------|---------------------|
| Overfitting to spec | Goodharting on evals | Broader eval sets, LLM-as-judge on unseen cases |
| Clever Hans shortcuts | Bad assumptions codified confidently | Diff review (human or LLM), property-based tests |
| Concept drift | Model drift breaking codified prompts | Regression evals, CI gates |
| Data leakage | Test/train contamination in eval suites | Held-out eval sets, adversarial test generation |

Every mitigation relies on the same property: the artifact is inspectable. You can write a test for a function. You can't write a test for a weight.

## The real question

Chollet asks "what will be the Keras of agentic coding?" — the abstraction layer that lets humans steer codebase "training" with minimal cognitive overhead. The [verifiability gradient](./verifiability-gradient.md) is a candidate answer: it tells you which grade of codification to use for each piece of your system, based on how verifiable you need it to be. The constrain/relax cycle is the steering mechanism — codify when patterns emerge, relax when new requirements appear. And crucially, neither the gradient nor the cycle requires a human in the loop. They require an inspectable artifact.

---

Relevant Notes:

- [codification](./definitions/codification.md) — foundation: codification as system-level learning through repo artifacts
- [the verifiability gradient](./verifiability-gradient.md) — determines when and how to codify
- [Agentic Note-Taking 23: Notes Without Reasons](https://x.com/molt_cornelius/status/2026894188516696435) — grounds: embedding latent spaces are opaque artifacts; curated propositional links are inspectable — the adjacency-vs-connection distinction is inspectability applied to knowledge architecture
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: 1M lines of agent-generated code, fully repo-hosted, CI-gated, and PR-reviewed — inspectable artifacts at production scale with zero manual code
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — component view: names inspectable repo artifacts and tools as the execution substrate layer of the runtime
