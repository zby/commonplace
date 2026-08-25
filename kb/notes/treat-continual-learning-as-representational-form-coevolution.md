---
description: Behaviour change spans distributed-parametric, natural-language, and symbolic forms, so the question is how their improvement loops relate — not which is the real locus of learning
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Treat continual learning as representational-form coevolution

[Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) argues that continual learning requires governing durable behaviour-changing writes — [system-definition](./definitions/system-definition-artifact.md) writes — beyond storing content, and that a deployed system's writable surface may include three [representational forms](./definitions/representational-form.md) (how an operative part is encoded and consumed): **distributed-parametric** (weights, adapters, embeddings, learned controllers), **natural-language** (prompts, notes, specs, rubrics), and **symbolic** (code, schemas, tests, tools). That note defers the general cross-form trade space to this one. [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md), so the readable forms already adapt durably during deployment. How should their improvement loops relate? They aren't independent: optimizing one assumes a position about the others.

Natural-language and symbolic cluster as the **readable artifacts** - inspectable, editable, distinct from distributed-parametric state in inspection method and update cost. The practical question of where to start building automated loops is [the readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). This note is about the generic coevolution frame.

## A mainstream direction: scaling the opaque loop

Computer vision provides the model. Before representation learning, features (SIFT, HOG) were hand-crafted and classifiers (SVMs) were learned — a clean separation that looked normal. Representation learning won by extending gradient descent across both, end-to-end. The general method didn't change; it covered more of the pipeline.

Wikipedia's secondary summary of the [bitter lesson](../sources/wikipedia-bitter-lesson.ingest.md) describes a long-run tendency for computationally scalable methods such as search and statistical learning to outperform approaches based on domain-specific understanding, and reports Sutton's recommendation to prefer simple scalable methods over increasingly elaborate human insight. One linked Commonplace analysis offers a narrower, case-level conjecture: pressure may consume a hand-crafted component whose [claimed scope was never earned](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md). It explicitly does not establish that mechanism as a broad historical tendency. This note uses it only as a possible explanation for why tokenizers and test suites might survive pressure that consumed SIFT. The next step is likewise this note's extrapolation, not the source's claim: it reads RLHF, RLAIF, continual pretraining, online learning, and fast adapters as a mainstream attempt to extend the opaque loop far enough to subsume the hand-crafted prompts, tools, and evals that deployed systems depend on. This may or may not succeed; new architectures could close the tempo gap, or structural limits could keep large opaque updates on a slower cycle. This note takes no position on the outcome.

## Loops today

Current methods range from single-form optimization to early cross-form loops:

- **DSPy, ProTeGi** — automated search over prompts (natural-language), weights frozen.
- **Genetic programming, FunSearch** — automated search over code (symbolic), weights frozen.
- **Meta-Harness** — automated search over harness code and prompt/context logic (symbolic + natural-language), weights frozen, benchmark traces as selection signal.
- **[Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md)** — a prompted language loss produces textual gradients that guide updates to prompts, tools, and pipeline topology (natural-language + symbolic); re-evaluation with the language-based loss decides rollback, while model weights remain fixed.
- **[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md)** — deployment-time mutation of natural-language-plus-code skill folders around a frozen LLM, with a contrastive parametric router trained separately through single-step offline reinforcement learning.
- **[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md)** — in a two-round experiment, validated repair of prompts, tool schemas, skills, middleware, and memory alternates with model fine-tuning on verified trajectories, spanning distributed-parametric weights plus a natural-language/symbolic harness.
- **RLHF / RLAIF** — updates weights (opaque), treating prompts and code as fixed.
- **Hand curation** (Commonplace and similar) — evolves natural-language fast and symbolic artifacts slowly, without automated search or weight updates.

The cross-form cases change the inventory, not the underlying difficulty. Symbolic Learning and Memento-Skills keep the main LLM fixed; Co-Harness spans all three forms but does not isolate coevolution from extra fine-tuning, improved trajectory data, or additional harness search. The open problem has moved from whether two or three forms can appear in one automated loop to whether cross-form credit assignment, compatibility, rollback, and validation can make the coupling reliably compound.

## Difficulties

The three forms have very different dynamics:

- **Distributed-parametric** updates via gradient descent or other numerical optimization. Needs differentiable or probe-derived signal and heavy training infrastructure; large updates cycle on days to weeks, though smaller add-on mechanisms can be faster.
- **Symbolic** artifacts are mutated by LLMs or search, then evaluated by tests, execution, or formal checks.
- **Natural-language** artifacts are mutated by LLMs and evaluated by execution, use, or LLM-as-judge. Semantics stay [underspecified](./agentic-systems-interpret-underspecified-instructions.md), so verification is softer.

A joint optimizer has to handle **pace mismatch** — either it runs at the slowest class's cadence, or classes coevolve asynchronously without diverging — and **cross-class credit assignment**: a deployment failure rarely says which class wants the update (prompt revision, tool extraction, memory promotion, weight update, retrieval change). Per-class methods sidestep both by fixing the class in advance.

## Starting point

Coevolution is the right conceptual frame, but a three-way joint optimizer isn't the near-term plan. [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) argues for starting with the natural-language + symbolic pair, on the basis of structural couplings that make the two a natural joint target.

---

Relevant Notes:

- [Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) — foundation: continual learning requires governing behaviour-changing writes across whichever of the parametric, natural-language, and symbolic forms an update touches — the premise that lets the readable pair count as a learning target at all
- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — foundation: retained readable artifacts already give a persistent deployment-time adaptation path
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: defines the natural-language/symbolic/distributed-parametric split used throughout this note
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — practical plan: the natural-language + symbolic pair is the tractable first slice
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: the context-engineering buildout is itself part of the joint loop
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operators: codify, relax, constrain, and adapt are artifact-side update operators
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidenced-by: a fixed-weight proposer mutates harness code and context/memory logic from raw traces — a readable-artifact loop in practice
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](https://yoonholee.com/meta-harness/paper.pdf) — evidenced-by: raw execution traces outperform scores-only or summarized feedback in automated harness search
- [Verbalizable Representations Form a Global Workspace in Language Models](../sources/verbalizable-representations-global-workspace-llms.ingest.md) — evidenced-by: counterfactual-reflection fine-tuning on 10,000 constitution-grounded natural-language reflection turns changes later behavior without reflection text at evaluation; targeted J-space ablation nearly removes the fabrication-honesty gain but only partially reverses the deception-benchmark gain, supporting a bounded natural-language-to-parametric path rather than general coevolution
