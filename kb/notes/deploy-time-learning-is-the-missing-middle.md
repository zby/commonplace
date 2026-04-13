---
description: Deploy-time learning fills the gap between training and in-context — durable symbolic artifacts provide inspectable adaptation across sessions, hardening along a verifiability gradient
type: note
traits: [has-comparison, title-as-claim]
tags: [learning-theory]
---

# Deploy-time learning is the missing middle

## Three Timescales

Deployed AI systems adapt at three timescales, each with a different substrate:

| Timescale | When | Substrate | Properties |
|-----------|------|-----------|------------|
| **Training** | Before deployment | Weights | Durable but opaque; requires a training pipeline; cannot incorporate deployment-specific information |
| **In-context** | Within a session | Context window | Inspectable but ephemeral; evaporates when the session ends |
| **Deploy-time learning** | Across sessions, during deployment | Symbolic artifacts | Durable, inspectable, and verifiable; accumulates over time |

The three rows are common configurations, not an exhaustive partition — substrate and timing are orthogonal in principle. [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) is a fourth case (weight substrate, deployment timing) that runs live RL from user interactions, but training infrastructure stays heavy enough to keep that path rare.

Deploy-time learning is not a new training paradigm — the model weights don't change. It is **system-level adaptation**: the deployed system's behavior improves because its *artifacts* improve. Like in-context learning, it happens during deployment; like training, it persists durably. Symbolic artifacts hit a pragmatic sweet spot: durable, inspectable, and compatible with ordinary software tooling. In Commonplace those artifacts are mostly repo-hosted, though the [substrate class is broader than the backend](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md).

Two mechanisms drive it: [constraining](./definitions/constraining.md) (narrowing the interpretation space) and [distillation](./definitions/distillation.md) (extracting procedures from reasoning). [Codification](./definitions/codification.md) — the far end of constraining — is where prompts undergo a phase transition into deterministic code. This note focuses on the verifiability gradient that runs across both.

The machinery involved — version control, diffs, tests, CI, code review — is unremarkable to programmers. But AI researchers, trained to think of adaptation through weights and gradients, look right past it. Symbolic artifacts sit in a disciplinary blind spot: "just engineering" to the ML community, yet doing genuine system-level learning.

## The Verifiability Gradient

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Karpathy identifies three properties that make a task verifiable: it must be **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate results automatically). The more verifiable a task is, the more you can hill-climb on it — whether through RL at training time or through iteration at runtime. Deploy-time learning applies this insight to symbolic artifacts: each grade of hardening makes the artifact more verifiable, enabling tighter iteration loops.

| Grade | Example | Resettable | Efficient | Rewardable |
|-------|---------|:---:|:---:|:---:|
| Restructured prompts | Breaking a monolithic prompt into sections | Yes | No — requires human review | No — judgment call |
| Structured output schemas | JSON schemas constraining response format | Yes | Yes — automated | Partial — shape is checked, content is not |
| Prompt tests / evals | Assertions over LLM output across test cases | Yes | Yes — automated | Mostly — statistical pass rates |
| Deterministic modules | Code that replaces what was previously LLM work | Yes | Yes — automated | Yes — pass/fail |

Moving down the table, verification gets cheaper and sharper. Restructured prompts need a human to judge quality; deterministic module tests run in milliseconds and return a boolean. The throughline is that hardened artifacts are **diffable, executable, testable, and reviewable**. A memory note like "remember to validate emails" is none of those. A structured output schema enforces shape and can be diffed; a test fails loudly in CI; deterministic code removes the LLM from the loop entirely.

The individual practices — prompt versioning, eval-driven development, CI-gated prompt testing — are established in LLMOps. The verifiability gradient contributes a **unifying lens**: these practices form a spectrum, and knowing where each piece of your system sits helps you choose the right hardness.

## Failure Modes

- **Premature codification.** Committing to one interpretation before enough runs reveal which is right locks in brittle assumptions. The constrain/relax cycle is the antidote: constrain only when patterns have emerged across runs, and be ready to relax back to an underspecified spec when new requirements expose the wrong commitment.
- **Goodharting on evals.** Optimising for the eval metric until it stops tracking real quality. Prompt tests can enshrine the wrong behavior; if your eval cases aren't representative of real traffic, gains on the eval set may regress in production.
- **Model drift.** Vendor model updates can break codified prompts and schemas. Regression evals are the defense — they catch drift even when the artifact hasn't changed.
- **Bad assumptions codified confidently.** An agent that writes a bad test codifies a bad assumption that now passes CI. The quality gate is typically human review — codification is a human-AI collaborative process, not a purely autonomous one.

## Related Work

How systems learn through accumulated artifacts is well-studied outside ML:

- **Organizational learning** (Argyris & Schön, 1978) — double-loop learning: organizations adapt by revising governing assumptions, not just actions. Deploy-time learning is double-loop learning for agent systems — constraining revises the rules, not just the outputs.
- **Knowledge creation** (Nonaka & Takeuchi, 1995) — the SECI spiral: tacit → explicit → combination → internalization. Constraining and distillation map to the externalization and combination phases.
- **Agile** — [deploy-time learning shares agile's core innovation](./deploy-time-learning-is-agile-for-human-ai-systems.md): co-evolving prose and code through short iteration cycles. The difference is that agile assumes code wins eventually; deploy-time learning treats the hybrid as the end state.
- **Malleable software** (Kirsch, [The Flawed Ephemeral Software Hypothesis](../sources/the-flawed-ephemeral-software-hypothesis.ingest.md)) — the same thesis in software-engineering language: AI lowers the cost of mutating durable artifact stacks, not replacing them. Kirsch names the system-level pressures that keep artifacts durable even when generation becomes cheap — state, integration surfaces, interface stability, auditability, deployment-discovered edge cases.
  - His framing lacks the verifiability gradient, but provides useful public vocabulary for the durable-artifact claim.

The ML/LLMOps practices are also well-established. Prompt versioning and "prompts as code" are standard advice. Eval-driven development has its own frameworks (OpenAI Evals, promptfoo) and process models ([EDDOps](https://arxiv.org/abs/2411.13768)). Automated prompt optimisation (DSPy, ProTeGi) pursues the same goal — improving system behavior without weight updates — through search over prompt components. Agent skill libraries like [Voyager](https://arxiv.org/abs/2305.16291) and evaluator-guided program evolution like [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) accumulate executable code as a form of cross-episode memory.

**TODO:** The organizational learning and knowledge creation citations are from the agent's training data, not systematic. Revisit with deep search — both traditions likely have results about when formalization helps vs hinders learning.

Deploy-time learning offers two contributions: a **taxonomy** (three timescales of system adaptation) and a **verifiability gradient** (from prompt tweaks to deterministic code). Together they synthesize established practices into a concrete model for when and how to move between grades. For how constraining resolves semantic underspecification and how the constrain/relax cycle lets systems breathe, see [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md).

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: deploy-time learning is one durable non-weight form of continuous learning
- [Learning substrates, backends, and artifact forms](./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: the repo is commonplace's backend choice within the broader symbolic artifact substrate
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: the paper's conclusion that AI context files are "maintained software artifacts" that are "versioned, reviewed, quality-assured, and tested" is the deploy-time learning thesis stated as an empirical finding across 466 projects
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — extends: behavioral contracts (YAML DSL specs with runtime enforcement) are the far end of the verifiability gradient for behavioral constraints — verifiable repo artifacts that improve reliability without weight updates
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "good harnesses compound" is the deploy-time learning thesis in practitioner language; each constraint makes future work more reliable across a 1M LOC agent-generated codebase
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning depends on deploy-time learning to build the context engineering machinery that selects the right knowledge; responds to Amodei's claim that continual learning is unnecessary
