---
description: Current AI improvement concentrates on the opaque loop (weights), treating prose and symbolic work as static engineering; weights alone are insufficient for full systems, so non-opaque substrates need their own automated improvement loops — coevolution is the eventual goal
type: note
traits: [title-as-claim]
tags: [learning-theory]
---

# Treat continual learning as substrate coevolution

In mainstream ML, "continual learning" means updating weights without catastrophic forgetting. That scope is too narrow — but the real problem is deeper than missing substrates. Deployed AI systems adapt through three [substrate classes](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — **opaque** (weights and other hidden state), **prose** (prompts, notes, natural-language specs, rubrics), and **symbolic** (code, schemas, tests, tools). Currently, essentially all effort on automated improvement goes to the opaque substrate. Prose and symbolic work is classified as "engineering" — static structure that humans build and maintain, not something that learns. The expectation is that scaling the opaque loop will eventually subsume what engineers do. The argument here is that it won't — and that finding automated improvement loops for non-opaque substrates is independently valuable, with **coevolution across all three** as the eventual goal.

## Substrate classes coevolve

[Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) establishes that prose and symbolic artifacts adapt durably during deployment. Weights adapt via ongoing training. These look like separate tracks, but in practice they coevolve:

- The value of weights depends on the prose and symbolic artifacts they compose with: tools, retrieval, evals, prompts.
- What artifacts need to encode depends on what the weights already handle well.
- Optimizing any one class assumes a position about the others.

Agile observed half of this coupling: code and specs coevolved, but only code executed. LLMs close the asymmetry — prose executes too — so prose can stay in production while it changes, and the coevolution becomes bidirectional.

## The mainstream bet: the opaque loop subsumes everything

Computer vision provides the model for the current expectation. Before representation learning, features (SIFT, HOG) were hand-crafted and classifiers (SVMs) were learned — a clean separation that looked normal. Representation learning won by extending gradient descent across both features and classifier, end-to-end. The general method did not change; it covered more of the pipeline.

The mainstream reading of the [bitter lesson](../sources/wikipedia-bitter-lesson.md) extrapolates this: general methods that leverage computation eat hand-crafted components. Applied to AI systems today, the expectation is that the opaque loop — RLHF, RLAIF, continual pretraining, online learning — will eventually subsume the hand-crafted prompts, tools, evals, and knowledge artifacts that deployed systems depend on. Train long enough on the right data with the right reward signal, and the model won't need the engineering.

## Why the opaque loop alone is insufficient

Deployed AI systems don't run on weights alone. They compose with tools, schemas, evals, prompts, retrieval pipelines, and knowledge artifacts — and these non-opaque components are not scaffolding waiting to be subsumed:

- **Symbolic artifacts** encode formal guarantees: type checks, test assertions, schema validation. These sit in the [arithmetic regime](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) where codification is permanent advantage, not transitional scaffolding.
- **Prose artifacts** encode deployment-specific knowledge that changes faster than retraining cycles: organizational policy, domain rubrics, workflow conventions. Weights can't carry these because they change weekly while retraining takes months.
- The value of improved weights depends on the artifacts they compose with. Better weights with stale tools, outdated prompts, or missing evals don't produce a better system.

If the non-opaque components need to evolve with the system, treating them as static engineering is a bottleneck. The bitter lesson doesn't say "only weights matter" — it says general methods that leverage computation beat hand-crafted ones. That applies to *all* substrates. If you're hand-crafting your prose and symbolic artifacts, an automated loop should eventually beat that too.

## Per-substrate loops are independently valuable

Co-evolution across all three substrates is the eventual goal. But finding an automated improvement loop for *any* non-opaque substrate is independently valuable — it means adaptation can happen in that medium without depending entirely on human engineering.

Current methods that target individual substrates:

- **DSPy, ProTeGi** automate search over prompts (prose), with weights frozen.
- **Genetic programming, FunSearch** automate search over code (symbolic), with weights frozen.
- **Meta-Harness** automates search over harness code and prompt/context logic (symbolic + prose), with weights frozen and benchmark traces as the selection signal.
- **RLHF / RLAIF** updates weights (opaque), treating prompts and code as fixed.
- **Hand curation** (Commonplace and similar) evolves prose fast and symbolic artifacts slowly — without automated search or weight updates.

Each method is partial. [Meta-Harness](https://arxiv.org/abs/2603.28052) is important because it is no longer just hand curation: a coding agent mutates non-opaque artifacts, reads raw execution traces, and selects candidates by benchmark performance while the base model stays fixed. That makes it a concrete instance of the "engineering to loop" transition for harness artifacts. Even unifying two classes — for example, a joint optimizer over weights and prompts — would be a significant step, analogous to what end-to-end gradient descent did for features plus classifier. But the prerequisite is understanding what an improvement loop for each substrate looks like: what are the mutation operators, selection signals, and evaluation criteria?

## Difficulties

The three classes have very different dynamics:

- **Opaque** updates via gradient descent. It needs differentiable signal and heavy training infrastructure. Cycle times: days to weeks.
- **Symbolic** artifacts are mutated by LLMs or search, then evaluated by tests, execution, or formal checks. Cycle times: hours to days.
- **Prose** artifacts are mutated by LLMs in seconds and evaluated by execution, use, or LLM-as-judge. Semantics stay [underspecified](./agentic-systems-interpret-underspecified-instructions.md), so verification is softer.

Unifying them under a single objective is nontrivial. A joint optimizer either operates at the slowest pace or lets classes coevolve asynchronously without diverging.

The harder problem is cross-class credit assignment. A deployment failure rarely says whether the right update is a prompt revision, memory promotion, new test, tool extraction, retrieval change, symbolic relaxation, or weight update. Pace mismatch is a scheduling problem. Credit assignment is a routing problem, and per-class methods sidestep it by fixing the substrate in advance.

## Possible approaches

A tractable first step is to unify two classes at a time:

- **Prose + symbolic** is the most accessible. Both are readable, both can be mutated by LLMs, and both can be evaluated by execution or judgment. Programming methodologies (agile, TDD, refactoring) already treat symbolic artifacts as objects of iterative improvement; their tooling (version control, diffs, tests, CI, review) transfers directly to prose, as KB systems demonstrate. Meta-Harness is the live example: it searches harness code, prompts, retrieval, memory, and context assembly as one artifact surface, using run traces and benchmark results as the improvement loop. The main missing piece for KBs is cross-session accumulation with automated selection under softer oracles.
- **Opaque + prose** has hand-tuned precursors. RLHF updates weights from prose-expressed preferences, and LLM providers appear to coevolve system prompts with model releases — revising one when the other changes behavior. What is missing is automation: both couplings are hand-tuned bundles, not joint optimization under a single selection rule.
- **Opaque + symbolic** has no clean instantiation yet. RLVR and code-generation RLHF look like candidates, but the generated code is ephemeral and the verifiers are hand-authored and frozen. The symbolic side provides a reward channel, not a learning substrate. A real instantiation would need weights and a persistent symbolic artifact — a tool library, spec set, or accumulating test suite — updating together and each informing the other.

Each two-class unification would be analogous to what end-to-end gradient descent did for features plus classifier: one extension of the general method, eating the hand-crafted alternative within its scope.

## From engineering to loops

Hand-crafted work on prose and symbolic artifacts — including Commonplace — occupies a specific role in this picture. It is simultaneously **engineering** (the current category) and **loop discovery** (discovering what automated evolution of these substrates would require). The bitter-lesson logic is visible only in hindsight: SIFT and HOG were not wasted; they showed what representation learning needed to capture. Methodology work on durable artifacts serves the same role. It articulates the operators ([codify](./definitions/codification.md), relax, [constrain](./definitions/constraining.md), [distill](./definitions/distillation.md)), the signals deployment produces, and the selection rules for when a revision sticks.

Hand-crafted evolution is also better than no evolution. Until automated loops for non-opaque substrates arrive, hand curation keeps deployment insights from evaporating. Without it, each session starts fresh and knowledge fails to accumulate across runs. The currently available alternative to Commonplace-style curation is not automation; it is forgetting.

The goal is to graduate from engineering to loops — first for individual substrates, then across them.

---

Relevant Notes:

- [Substrate class, backend, and artifact form are separate axes that get conflated](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — foundation: defines the opaque/prose/symbolic split used throughout this note
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — foundation: establishes prose and symbolic artifacts as durable adaptation substrates
- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — aligns: both notes argue the scope of continual learning has been drawn too narrowly
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: deploy-time learning builds the context-engineering machinery; this note frames that buildout as itself part of the joint loop
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operators: codify, relax, constrain, and distill are artifact-side update operators in the joint loop
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidence: code-inspected system where a fixed-weight proposer mutates harness code and context/memory logic from raw traces, showing a non-opaque substrate loop in practice
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidence: paper coverage and ablation showing raw execution traces outperform scores-only or summarized feedback in automated harness search
