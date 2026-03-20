---
description: Deploy-time learning fills the gap between training and in-context — durable symbolic artifacts provide inspectable adaptation across sessions along a verifiability gradient
type: note
traits: [has-comparison]
tags: [learning-theory]
---

# Deploy-time learning: The Missing Middle

## Three Timescales

Deployed AI systems adapt at three timescales, each with a different substrate:

| Timescale | When | Substrate | Properties |
|-----------|------|-----------|------------|
| **Training** | Before deployment | Weights | Durable but opaque; requires a training pipeline; cannot incorporate deployment-specific information |
| **In-context** | Within a session | Context window | Inspectable but ephemeral; evaporates when the session ends |
| **Deploy-time learning** | Across sessions, during deployment | Symbolic artifacts | Durable, inspectable, and verifiable; accumulates over time |

Deploy-time learning is not a new training paradigm — the model weights don't change. It is **system-level adaptation**: the deployed system's behavior improves because its *artifacts* improve. Like in-context learning it happens during deployment; like training it persists durably. Weight updates during deployment are possible in principle — [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) performs live RL from user interactions — but training infrastructure is too heavy for most deployment contexts. Symbolic artifacts hit a pragmatic sweet spot: durable, inspectable, and compatible with ordinary software tooling. In Commonplace those artifacts are mostly repo-hosted, but the [substrate class is broader than the backend](./learning-substrates-backends-and-artifact-forms.md).

This learning operates through two mechanisms — [constraining](./constraining.md) (narrowing the interpretation space) and [distillation](./distillation.md) (extracting procedures from reasoning). Codification is the far end of constraining, where prompts undergo a phase transition to deterministic code. This note focuses on the verifiability gradient that runs across both.

The machinery involved — version control, diffs, tests, CI, code review — is unremarkable to programmers. But AI researchers, trained to think about adaptation in terms of weights and gradients, tend to look past it. Symbolic artifacts sit in a disciplinary blind spot — "just engineering" to the ML community, yet doing genuine system-level learning.

## The Verifiability Gradient

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Karpathy identifies three properties that make a task verifiable: it must be **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate the result automatically). The more verifiable a task is, the more you can hill-climb on it — whether through RL at training time or through iteration at runtime. Deploy-time learning applies this insight to symbolic artifacts: each grade of hardening makes the artifact more verifiable, enabling tighter iteration loops.

| Grade | Example | Resettable | Efficient | Rewardable |
|-------|---------|:---:|:---:|:---:|
| Restructured prompts | Breaking a monolithic prompt into sections | Yes | No — requires human review | No — judgment call |
| Structured output schemas | JSON schemas constraining response format | Yes | Yes — automated | Partial — shape is checked, content is not |
| Prompt tests / evals | Assertions over LLM output across test cases | Yes | Yes — automated | Mostly — statistical pass rates |
| Deterministic modules | Code that replaces what was previously LLM work | Yes | Yes — automated | Yes — pass/fail |

Moving down the table, verification gets cheaper and sharper. Restructured prompts require a human to judge quality. Deterministic module tests run in milliseconds and return a boolean. The key property throughout is that hardened artifacts are **diffable, executable, testable, and reviewable** — a memory note like "remember to validate emails" is none of those things, while a structured output schema enforces shape and can be diffed, a test fails loudly in CI, and deterministic code removes the LLM from the loop entirely.

The individual practices — prompt versioning, eval-driven development, CI-gated prompt testing — are established in LLMOps. What the verifiability gradient contributes is a **unifying lens**: these practices form a spectrum, and understanding where each piece of your system sits helps you choose the right hardness.

## Concrete Examples

The [`examples/`](../../examples/) directory contains working before-and-after pairs that demonstrate constraining at different grades.

### Data report: statistics → code, interpretation → LLM

[`data_report/`](../../examples/data_report/) is the unconstrained version. A single LLM agent receives a CSV file and does *everything*: parse the CSV, compute statistics (mean, median, min, max), detect trends, and write a narrative report. The LLM is doing arithmetic it could get wrong, at token cost, for work that has a single correct answer.

[`data_report_constrained/`](../../examples/data_report_constrained/) extracts the mechanical parts into a Python tool (`tools.py`):
- **CSV parsing** → `csv.DictReader` (deterministic)
- **Statistics** → Python's `statistics` module (deterministic)
- **Trend detection** → a simple algorithm comparing first-half vs second-half averages (deterministic)

The LLM agent (`write_narrative.agent`) now receives pre-computed stats and trends, and does only what requires judgment: interpreting what the numbers mean for the business.

The call site in the orchestrator (`main.agent`) is unchanged — `analyze_dataset(path=...)` works the same way. The implementation committed to one precise interpretation of "compute statistics" — resolving the semantic underspecification of the natural-language spec into deterministic code — while the interface stayed stable.

### Pitchdeck evaluation: a four-stage progression

The pitchdeck examples show the same task — evaluate PDF pitch decks — at four constraining levels:

| Example | What moved to code |
|---------|-------------------|
| [`pitchdeck_eval/`](../../examples/pitchdeck_eval/) | Nothing — all LLM, including filename slug generation |
| [`pitchdeck_eval_constrained/`](../../examples/pitchdeck_eval_constrained/) | File discovery, slug generation, path construction → Python tool (`list_pitchdecks()`) |
| [`pitchdeck_eval_code_entry/`](../../examples/pitchdeck_eval_code_entry/) | Orchestration loop → Python; agents handle reasoning only |
| [`pitchdeck_eval_direct/`](../../examples/pitchdeck_eval_direct/) | Direct API calls — three abstraction levels without the CLI |

At each stage, mechanical work moves to code while the LLM stays focused on what requires judgment (analyzing the pitch deck content). The slug generation is a small example but an instructive one: in the unconstrained version, the LLM is asked to "generate a file slug (lowercase, hyphenated, no extension)" — a spec that looks precise but actually admits multiple valid interpretations (how to handle special characters, what counts as a "word," whether to transliterate accented characters). Each run might resolve these ambiguities differently, and inconsistency means broken file paths. In the constrained version, `python-slugify` commits to one interpretation, in code, once — resolving the underspecification permanently.

## Failure Modes

- **Premature codification.** Committing to a specific interpretation before you've observed enough runs to know which interpretation is right locks in brittle assumptions. The constrain/relax cycle is the antidote — constrain only when patterns have emerged across runs, and be ready to relax back to an underspecified spec when new requirements reveal that you committed to the wrong interpretation.
- **Goodharting on evals.** Prompt tests can enshrine the wrong behavior. If your eval cases aren't representative of real traffic, improvements on the eval set may regress in production.
- **Model drift.** Vendor model updates can break codified prompts and schemas. Regression evals are the defense — they detect drift even when the artifact hasn't changed.
- **Bad assumptions codified confidently.** An agent that writes a bad test codifies a bad assumption that now passes CI. The quality gate is typically human review — codification is a human-AI collaborative process, not a purely autonomous one.

## Related Work

Systems learning through accumulated artifacts is well-studied outside ML:

- **Organizational learning** (Argyris & Schön, 1978) — double-loop learning: organizations adapt by revising governing assumptions, not just actions. Deploy-time learning is double-loop learning for agent systems — constraining revises the rules, not just the outputs.
- **Knowledge creation** (Nonaka & Takeuchi, 1995) — the SECI spiral: tacit → explicit → combination → internalization. Constraining and distillation map to externalization and combination phases.
- **Agile** — [deploy-time learning shares agile's core innovation](./deploy-time-learning-is-agile-for-human-ai-systems.md): co-evolving prose and code through short iteration cycles. The difference is that agile assumes code wins eventually; deploy-time learning treats the hybrid as the end state.
- **Malleable software** (Kirsch, [The Flawed Ephemeral Software Hypothesis](../sources/the-flawed-ephemeral-software-hypothesis.ingest.md)) — the same thesis in software-engineering language: AI lowers the cost of mutating durable artifact stacks, not replacing them. Kirsch names system-level pressures that keep artifacts durable — state, integration surfaces, interface stability, auditability, deployment-discovered edge cases — even when generation becomes cheap. His framing lacks the verifiability gradient (different parts of the stack harden to different degrees), but provides useful public vocabulary for the durable-artifact claim.

The ML/LLMOps practices are also well-established. Prompt versioning and "prompts as code" are standard advice. Eval-driven development has its own frameworks (OpenAI Evals, promptfoo) and process models ([EDDOps](https://arxiv.org/abs/2411.13768)). Automated prompt optimisation (DSPy, ProTeGi) pursues a related goal — improving system behavior without weight updates — through search over prompt components. Agent skill libraries like [Voyager](https://arxiv.org/abs/2305.16291) and evaluator-guided program evolution like [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) accumulate executable code as a form of cross-episode memory.

**TODO:** The organizational learning and knowledge creation citations are from the agent's training data, not systematic. Revisit with deep search — both traditions likely have results about when formalization helps vs hinders learning.

Deploy-time learning is a **taxonomy** (three timescales of system adaptation) and a **verifiability gradient** (from prompt tweaks to deterministic code) — a synthesis of established practices into a concrete model for when and how to move between grades. For how constraining resolves semantic underspecification and how the constrain/relax cycle lets systems breathe, see [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md).

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: deploy-time learning is one durable non-weight form of continuous learning
- [Learning substrates, backends, and artifact forms](./learning-substrates-backends-and-artifact-forms.md) — sharpens: the repo is commonplace's backend choice within the broader symbolic artifact substrate
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: the paper's conclusion that AI context files are "maintained software artifacts" that are "versioned, reviewed, quality-assured, and tested" is the deploy-time learning thesis stated as an empirical finding across 466 projects
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — extends: behavioral contracts (YAML DSL specs with runtime enforcement) are the far end of the verifiability gradient for behavioral constraints — verifiable repo artifacts that improve reliability without weight updates
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "good harnesses compound" is the deploy-time learning thesis in practitioner language; each constraint makes future work more reliable across a 1M LOC agent-generated codebase
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning depends on deploy-time learning to build the context engineering machinery that selects the right knowledge; responds to Amodei's claim that continual learning is unnecessary
