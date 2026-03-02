---
description: Chollet frames agentic coding as ML producing blackbox codebases — crystallisation counters this not by requiring human review but by choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: current
---

# Inspectable substrate, not supervision, defeats the blackbox problem

## The claim from ML

Chollet [observes](https://x.com/fchollet/status/2024519439140737442) that sufficiently advanced agentic coding is essentially machine learning: an optimization process (coding agents) iterates against a goal (spec + tests) until convergence, producing a blackbox artifact (the generated codebase) that is "deployed without ever inspecting its internal logic, just as we ignore individual weights in a neural network."

He predicts classic ML failure modes will follow: overfitting to the spec, Clever Hans shortcuts that don't generalize, data leakage, concept drift. And asks: what will be the Keras of agentic coding — the optimal high-level abstractions for steering this process?

## Where the framing breaks

The blackbox analogy holds only if the output substrate is opaque. Neural network weights are opaque to any inspector — human or LLM. But repo artifacts (prompts, schemas, evals, deterministic code) are inherently inspectable. They can be diffed, tested, reverted, and reviewed — by humans or by LLMs. The substrate is what matters, not who reviews it.

An LLM can review a diff and catch a Clever Hans shortcut in generated code. It can run evals and detect overfitting to the test suite. It can compare a crystallised function against its specification and flag edge cases. None of this is possible with weight updates — not because LLMs lack judgment, but because weights lack structure.

## The failure mode mapping

Chollet's predicted ML problems map directly to [crystallisation](agentic-systems-learn-through-three-distinct-mechanisms.md) failure modes — but with mitigations that weight-based systems can't match:

| ML failure mode | Crystallisation equivalent | Mitigation available |
|----------------|---------------------------|---------------------|
| Overfitting to spec | Goodharting on evals | Broader eval sets, LLM-as-judge on unseen cases |
| Clever Hans shortcuts | Bad assumptions crystallised confidently | Diff review (human or LLM), property-based tests |
| Concept drift | Model drift breaking crystallised prompts | Regression evals, CI gates |
| Data leakage | Test/train contamination in eval suites | Held-out eval sets, adversarial test generation |

Every mitigation relies on the same property: the artifact is inspectable. You can write a test for a function. You can't write a test for a weight.

## The real question

Chollet asks "what will be the Keras of agentic coding?" — the abstraction layer that lets humans steer codebase "training" with minimal cognitive overhead. The [verifiability gradient](deploy-time-learning-the-missing-middle.md) is a candidate answer: it tells you which grade of crystallisation to use for each piece of your system, based on how verifiable you need it to be. The stabilise/soften cycle is the steering mechanism — crystallise when patterns emerge, soften when new requirements appear. And crucially, neither the gradient nor the cycle requires a human in the loop. They require an inspectable substrate.

---

Relevant Notes:
- [three distinct mechanisms](agentic-systems-learn-through-three-distinct-mechanisms.md) — foundation: crystallisation as system-level learning through repo artifacts
- [deploy-time-learning](deploy-time-learning-the-missing-middle.md) — the verifiability gradient that determines when and how to crystallise

Topics:
- [learning-theory](./learning-theory.md)
