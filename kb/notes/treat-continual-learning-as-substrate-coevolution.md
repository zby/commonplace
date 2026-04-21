---
description: Behaviour change spans three artifact classes — opaque (weights), prose (prompts, notes, specs), and symbolic (code, schemas, tests) — so the coevolution question is how their improvement loops relate, not which is the real locus of learning
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory]
---

# Treat continual learning as substrate coevolution

[Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) names two behaviour-change mechanisms: expensive weight updates and cheap readable system-definition artifacts. [Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) places the readable mechanism on the timing axis. Splitting the readable side by semantic regime gives three [artifact classes](./axes-of-artifact-analysis.md) — **opaque** (weights and other hidden state), **prose** (prompts, notes, specs, rubrics), and **symbolic** (code, schemas, tests, tools). How should their improvement loops relate? They aren't independent: optimizing one assumes a position about the others.

Prose and symbolic cluster as the **readable artifacts** — inspectable, editable, distinct from opaque in backend and update cost. The practical question of where to start building automated loops is [the readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). This note is about the generic coevolution frame.

## The mainstream direction: scaling the opaque loop

Computer vision provides the model. Before representation learning, features (SIFT, HOG) were hand-crafted and classifiers (SVMs) were learned — a clean separation that looked normal. Representation learning won by extending gradient descent across both, end-to-end. The general method didn't change; it covered more of the pipeline.

The [bitter lesson](../sources/wikipedia-bitter-lesson.md) extrapolates: general methods that leverage computation eat hand-crafted components. Applied today, mainstream research extends the opaque loop — RLHF, RLAIF, continual pretraining, online learning, fast adapters — hoping to subsume the hand-crafted prompts, tools, and evals that deployed systems depend on. This may or may not succeed; new architectures could close the tempo gap, or structural limits could keep large opaque updates on a slower cycle. This note takes no position on the outcome.

## Per-class loops today

Current methods target individual classes:

- **DSPy, ProTeGi** — automated search over prompts (prose), weights frozen.
- **Genetic programming, FunSearch** — automated search over code (symbolic), weights frozen.
- **Meta-Harness** — automated search over harness code and prompt/context logic (symbolic + prose), weights frozen, benchmark traces as selection signal.
- **RLHF / RLAIF** — updates weights (opaque), treating prompts and code as fixed.
- **Hand curation** (Commonplace and similar) — evolves prose fast and symbolic artifacts slowly, without automated search or weight updates.

Each is partial. Even unifying two classes — a joint optimizer over weights and prompts, say — would be a significant step, analogous to what end-to-end gradient descent did for features plus classifier. The prerequisite is understanding what an improvement loop for each class looks like: mutation operators, selection signals, evaluation criteria.

## Difficulties

The three classes have very different dynamics:

- **Opaque** updates via gradient descent. Needs differentiable signal and heavy training infrastructure; large updates cycle on days to weeks, though smaller add-on mechanisms can be faster.
- **Symbolic** artifacts are mutated by LLMs or search, then evaluated by tests, execution, or formal checks.
- **Prose** artifacts are mutated by LLMs and evaluated by execution, use, or LLM-as-judge. Semantics stay [underspecified](./agentic-systems-interpret-underspecified-instructions.md), so verification is softer.

A joint optimizer has to handle **pace mismatch** — either it runs at the slowest class's cadence, or classes coevolve asynchronously without diverging — and **cross-class credit assignment**: a deployment failure rarely says which class wants the update (prompt revision, tool extraction, memory promotion, weight update, retrieval change). Per-class methods sidestep both by fixing the class in advance.

## Starting point

Coevolution is the right conceptual frame, but a three-way joint optimizer isn't the near-term plan. [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) argues for starting with the prose+symbolic pair, on the basis of structural couplings that make the two a natural joint target.

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — foundation: two behaviour-change mechanisms (weights, readable artifacts) — the premise that lets the readable pair count as a learning target at all
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — foundation: places the readable mechanism on the timing axis
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: defines the opaque/prose/symbolic split used throughout this note
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — practical plan: the prose+symbolic pair is the tractable first slice
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: the context-engineering buildout is itself part of the joint loop
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operators: codify, relax, constrain, and distill are artifact-side update operators
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidence: a fixed-weight proposer mutates harness code and context/memory logic from raw traces — a readable-artifact loop in practice
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidence: raw execution traces outperform scores-only or summarized feedback in automated harness search
