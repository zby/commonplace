---
description: Continual learning is usually scoped to weights; the stronger frame is coevolution across opaque, prose, and symbolic substrate classes, with the bitter lesson applying to the improvement loop itself
type: note
traits: [title-as-claim]
tags: [learning-theory]
---

# Treat continual learning as substrate coevolution

In mainstream ML, "continual learning" means updating weights without catastrophic forgetting. That scope is too narrow. Deployed AI systems adapt through three [substrate classes](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — **opaque** (weights and other hidden state), **prose** (prompts, notes, natural-language specs, rubrics), and **symbolic** (code, schemas, tests, tools) — and those adaptations are coupled. Continual learning should therefore be treated as **coevolution across substrate classes**: the joint loop is the object of study, not any single class in isolation.

## Substrate classes coevolve

[Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) establishes that prose and symbolic artifacts adapt durably during deployment. Weights adapt via ongoing training. These look like separate tracks, but in practice they coevolve:

- The value of weights depends on the prose and symbolic artifacts they compose with: tools, retrieval, evals, prompts.
- What artifacts need to encode depends on what the weights already handle well.
- Optimizing any one class assumes a position about the others.

Agile observed half of this coupling: code and specs coevolved, but only code executed. LLMs close the asymmetry — prose executes too — so prose can stay in production while it changes, and the coevolution becomes bidirectional.

## The joint loop is where the general method lives

People naturally factor optimization problems by substrate: features here, classifier there; prompt here, weights there. They assume each part can be tuned while the others stay fixed. That intuition has a track record of losing.

Computer vision is the sharpest example. Before representation learning, features (SIFT, HOG) were hand-crafted and classifiers (SVMs) were learned — a clean separation that looked normal. Representation learning won by extending gradient descent across both features and classifier, end-to-end. The general method did not change; it covered more of the pipeline. Architecture, loss, and data augmentation stayed hand-crafted for years, but expanding the optimization boundary was enough to eat hand-crafted feature engineering.

The same pattern is likely playing out now. Current methods keep the substrate classes separate:

- **DSPy, ProTeGi** automate search over prompts (prose), with weights frozen.
- **Genetic programming, FunSearch** automate search over code (symbolic), with weights frozen.
- **RLHF / RLAIF** updates weights (opaque), treating prompts and code as fixed.
- **Hand curation** (Commonplace and similar) evolves prose fast and symbolic artifacts slowly — without automated search or weight updates.

Each method is partial. Even unifying two classes — for example, a joint optimizer over weights and prompts — would be a significant step, analogous to what end-to-end gradient descent did for features plus classifier.

## The bitter lesson applies to the loop, not the class

The [bitter lesson](../sources/wikipedia-bitter-lesson.md) recurs: every time a hand-crafted method looks locally optimal, a general method that leverages more computation eventually eats it. The lesson applies to the process we use to improve a system, not to any substrate class taken alone.

The prediction is not "the bitter lesson applies separately to opaque, prose, and symbolic substrates." The prediction is that hand-crafted per-class methods will lose to general methods that span classes. Current prompt optimizers, program-evolution systems, RLHF pipelines, and curation methodologies sit in the feature-engineering position: useful, necessary for discovering what the loop needs to capture, but ultimately transitional.

## Difficulties

The three classes have very different dynamics:

- **Opaque** updates via gradient descent. It needs differentiable signal and heavy training infrastructure. Cycle times: days to weeks.
- **Symbolic** artifacts are mutated by LLMs or search, then evaluated by tests, execution, or formal checks. Cycle times: hours to days.
- **Prose** artifacts are mutated by LLMs in seconds and evaluated by execution, use, or LLM-as-judge. Semantics stay [underspecified](./agentic-systems-interpret-underspecified-instructions.md), so verification is softer.

Unifying them under a single objective is nontrivial. A joint optimizer either operates at the slowest pace or lets classes coevolve asynchronously without diverging.

The harder problem is cross-class credit assignment. A deployment failure rarely says whether the right update is a prompt revision, memory promotion, new test, tool extraction, retrieval change, symbolic relaxation, or weight update. Pace mismatch is a scheduling problem. Credit assignment is a routing problem, and per-class methods sidestep it by fixing the substrate in advance.

## Possible approaches

A tractable first step is to unify two classes at a time:

- **Prose + symbolic** is the most accessible. Both are readable, both can be mutated by LLMs, and both can be evaluated by execution or judgment. Programming methodologies (agile, TDD, refactoring) already treat symbolic artifacts as objects of iterative improvement; their tooling (version control, diffs, tests, CI, review) transfers directly to prose, as KB systems demonstrate. The main missing piece is cross-session accumulation with automated selection.
- **Opaque + prose** has hand-tuned precursors. RLHF updates weights from prose-expressed preferences, and LLM providers appear to coevolve system prompts with model releases — revising one when the other changes behavior. What is missing is automation: both couplings are hand-tuned bundles, not joint optimization under a single selection rule.
- **Opaque + symbolic** has no clean instantiation yet. RLVR and code-generation RLHF look like candidates, but the generated code is ephemeral and the verifiers are hand-authored and frozen. The symbolic side provides a reward channel, not a learning substrate. A real instantiation would need weights and a persistent symbolic artifact — a tool library, spec set, or accumulating test suite — updating together and each informing the other.

Each two-class unification would be analogous to what end-to-end gradient descent did for features plus classifier: one extension of the general method, eating the hand-crafted alternative within its scope.

## Stepping-stone posture

Hand-crafted work on prose and symbolic artifacts, including Commonplace, is how we discover the loop's shape. The bitter-lesson logic is visible only in hindsight: SIFT and HOG were not wasted; they showed what representation learning needed to capture. Methodology work on durable artifacts serves the same role. It articulates the operators ([codify](./definitions/codification.md), relax, [constrain](./definitions/constraining.md), [distill](./definitions/distillation.md)), the signals deployment produces, and the selection rules for when a revision sticks. The more legible these become, the sooner a general joint optimizer can extract and replace them.

Hand-crafted evolution is also better than no evolution. Until a general joint optimizer arrives, hand curation keeps deployment insights from evaporating. Without it, each session starts fresh and knowledge fails to accumulate across runs. The currently available alternative to Commonplace-style curation is not automation; it is forgetting.

The goal is not to preserve the methodology — it's to make it extractable.

---

Relevant Notes:

- [Substrate class, backend, and artifact form are separate axes that get conflated](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — foundation: defines the opaque/prose/symbolic split used throughout this note
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — foundation: establishes prose and symbolic artifacts as durable adaptation substrates
- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — aligns: both notes argue the scope of continual learning has been drawn too narrowly
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: deploy-time learning builds the context-engineering machinery; this note frames that buildout as itself part of the joint loop
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operators: codify, relax, constrain, and distill are artifact-side update operators in the joint loop
