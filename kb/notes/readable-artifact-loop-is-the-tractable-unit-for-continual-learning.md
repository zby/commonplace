---
description: Within substrate coevolution, the readable pair (prose + symbolic) is the tractable unit to build a first automated loop around — shared context, current tempo, and an existing codification boundary make joint optimization clean; the pair is also under-explored relative to the mainstream opaque effort
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory]
---

# The readable-artifact loop is the tractable unit for continual learning

[Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) sets the frame: opaque, prose, and symbolic artifact classes all adapt durably; they are coupled; how their improvement loops relate is the open question. This note takes the practical next step. A full three-way joint optimizer is not the near-term plan. The tractable first slice is the **readable pair** — prose and symbolic together — which shares enough structure to form a single coupled optimization target. Mainstream ML is scaling the opaque loop; automating the readable-artifact loop is a parallel, under-explored avenue that stands on its own structural merits, regardless of how fast opaque updates mature.

## Why the readable pair is a natural unit

The readable artifact classes have distinctive properties that make them a coupled target:

- **Shared runtime medium.** Prose and symbolic artifacts both live in (or through) the [agent's context window](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) at inference time — prompts are context; tool schemas and artifact contents load as context. Every optimization of one trades off against the other because they compete for the same finite budget. [Codification](./definitions/codification.md) makes this concrete: moving behaviour from prose into a tool or deterministic function changes its context cost and its verifiability at once — a single edit at the codification boundary that touches both classes.
- **Current tempo.** Hand edits to readable artifacts already cycle much faster than large-model retraining. That doesn't promise *automated* loops will be fast — those procedures are what we're after — but it shows the upper bound isn't slow, giving the direction traction now while opaque-tempo research matures.
- **What they encode is genuinely explicit.** Symbolic artifacts encode formal guarantees (type checks, test assertions, schema validation) — codification is permanent advantage in the [arithmetic regime](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md), not scaffolding waiting to be subsumed. Prose artifacts encode deployment-specific knowledge — organizational policy, domain rubrics, workflow conventions — that changes on its own schedule. Whatever the opaque loop eventually absorbs, these artifacts remain legible, reviewable, and versionable in ways weights are not.
- **Coupling to the opaque layer is already live.** The value of improved weights depends on the artifacts they compose with; better weights with stale tools, outdated prompts, or missing evals don't produce a better system. The reverse also holds: what artifacts need to encode depends on what weights already handle well. A readable-artifact loop therefore operates inside an already-coupled system — it doesn't have to wait for three-way joint optimization to produce value.

Strictly speaking, the factoring that matters is by **update cost**, not artifact class. Today the readable artifacts all update fast and most opaque mechanisms update slowly, so the two pairings coincide. But small add-on models, LoRA adapters, routing networks, and embedding updates can move opaque mechanisms into the fast loop. The universal form of the argument is to build a tightly coupled loop around whatever updates at deployment pace, with looser asynchronous coupling to whatever remains slow.

## Why prose+symbolic, not the other pairings

Three two-class pairings are conceivable; only one has the structural couplings to support a near-term joint loop:

- **Prose + symbolic** is the natural unit. Both are readable, both can be mutated by LLMs, both can be evaluated by execution or judgment, and both compete for the same context budget — so joint optimization has a clean target (trade-offs along the codification boundary) and a clean scarce resource to optimize against. Programming methodologies (agile, TDD, refactoring) already treat symbolic artifacts as objects of iterative improvement; their tooling (version control, diffs, tests, CI, review) transfers directly to prose, as KB systems demonstrate. [Meta-Harness](https://arxiv.org/abs/2603.28052) is the live example: it searches harness code, prompts, retrieval, memory, and context assembly as one artifact surface, using run traces and benchmark results as the improvement loop. The main missing piece for KBs is cross-session accumulation with automated selection under softer oracles.
- **Opaque + prose** has hand-tuned precursors. RLHF updates weights from prose-expressed preferences, and LLM providers appear to coevolve system prompts with model releases — revising one when the other changes behavior. What is missing is automation: both couplings are hand-tuned bundles, not joint optimization under a single selection rule.
- **Opaque + symbolic** has no clean instantiation yet. RLVR and code-generation RLHF look like candidates, but the generated code is ephemeral and the verifiers are hand-authored and frozen. The symbolic side provides a reward channel, not a learning target. A real instantiation would need weights and a persistent symbolic artifact — a tool library, spec set, or accumulating test suite — updating together and each informing the other.

Each two-class unification would do for its scope what end-to-end gradient descent did for features plus classifier: extend the general method and eat the hand-crafted alternative. The prose+symbolic pairing has the structural couplings that give it the most traction today.

## From engineering to loops

Hand-crafted work on readable artifacts — including Commonplace — occupies a specific role in this picture. It is simultaneously **engineering** (the current category) and **loop discovery** (discovering what automated evolution of these artifacts would require). The bitter-lesson logic is visible only in hindsight: SIFT and HOG were not wasted; they showed what representation learning needed to capture. Methodology work on durable artifacts serves the same role. It articulates the operators ([codify](./definitions/codification.md), relax, [constrain](./definitions/constraining.md), [distill](./definitions/distillation.md)), the signals deployment produces, and the selection rules for when a revision sticks.

Hand-crafted evolution is also better than no evolution. Until automated loops for readable artifacts arrive, hand curation keeps deployment insights from evaporating. Without it, each session starts fresh and knowledge fails to accumulate across runs. The currently available alternative to Commonplace-style curation is not automation; it is forgetting.

The goal is to graduate from engineering to loops — first for the readable pair, where structural couplings give the most traction, and then across the wider three-class picture as fast opaque mechanisms mature.

---

Relevant Notes:

- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — frame: coevolution across opaque, prose, and symbolic artifact classes; this note argues the readable pair is the tractable first slice
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: defines the opaque/prose/symbolic split; the readable pair is the non-opaque union
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — foundation: prose and symbolic artifacts as durable adaptation targets; this note treats the pair as a single coupled target
- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — foundation: behaviour change is the open half of continual learning, with weights and readable system-definition artifacts as the two mechanisms — the premise that lets the readable pair count as a learning target at all
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the shared scarce resource that makes prose and symbolic artifacts a structurally coupled optimization target
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operators: codify, relax, constrain, and distill are the update operators on the codification boundary
- [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md) — evidence: code-inspected system where a fixed-weight proposer mutates harness code and context/memory logic from raw traces, showing a readable-artifact loop in practice
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidence: paper coverage and ablation showing raw execution traces outperform scores-only or summarized feedback in automated harness search
