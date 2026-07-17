---
description: "Curated head for the deploy-time-learning tag — the framework of system adaptation through durable, inspectable artifacts, plus learning fundamentals and feedback quality"
type: kb/types/tag-readme.md
index_source: tag
index_key: deploy-time-learning
---

# deploy-time-learning

The organizing framework of the learning-theory area: deployed systems adapt through symbolic artifacts — durable, inspectable, verifiable — filling the gap between training and in-context learning. Notes here cover the framework itself, the learning fundamentals it rests on, and the feedback signals that govern its quality. A child of [learning-theory](./learning-theory-README.md).

## The framework

- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — three timescales of system adaptation; co-evolving prose and code as agile-style deploy-time learning
- [the verifiability gradient](./verifiability-gradient.md) — the ladder deploy-time artifacts sit on, from restructured prompts through schemas and evals to deterministic code
- [readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — the loop that makes behaviour change cheap: readable system-definition artifacts revised in place
- [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — the system and its knowledge substrate evolve together rather than one training the other

## Learning fundamentals

- [learning is not only about generality](./learning-is-not-only-about-generality.md) — accumulation as the basic operation, with reach as its key property; capacity decomposes into generality vs a reliability/speed/cost compound
- [LLM learning phases fall between human learning modes](./llm-learning-phases-fall-between-human-learning-modes.md) — warns against literal human-LLM learning analogies
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — "no continual learning needed" relocates the learning to the system layer rather than eliminating it
- [choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — accumulation policy: true is necessary but not sufficient
- [abstract an experience only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — the abstract-vs-preserve decision: generalize only when the lesson's boundary is statable, else keep the instance

## Feedback and signal quality

- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — short iterations bound interpretation-error propagation, not just change-response latency
- [evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — comprehension and specification must precede optimization, or automation amplifies the wrong objective
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — what the learning loop can learn is bounded by what its diagnostics distinguish
- [apparent success is an unreliable health signal](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) — completion without verification teaches the wrong lesson

## Related Tags

- [constraining](./constraining-README.md) — the primary hardening mechanism inside the framework
- [discovery](./discovery-README.md) — the operation that produces the framework's highest-reach artifacts
