---
description: Deploy-time learning fills the gap between training and in-context — repo artifacts provide durable, inspectable adaptation through three mechanisms (stabilisation, crystallisation, distillation) with a verifiability gradient from prompt tweaks to deterministic code
type: note
traits: [has-comparison]
areas: [learning-theory]
---

# Deploy-time learning: The Missing Middle

## Three Timescales

Deployed AI systems adapt at three timescales, each with a different substrate:

| Timescale | When | Substrate | Properties |
|-----------|------|-----------|------------|
| **Training** | Before deployment | Weights | Durable but opaque; requires a training pipeline; cannot incorporate deployment-specific information |
| **In-context** | Within a session | Context window | Inspectable but ephemeral; evaporates when the session ends |
| **Deploy-time learning** | Across sessions, during deployment | Repo artifacts | Durable, inspectable, and verifiable; accumulates over time |

Deploy-time learning is not a new training paradigm — the model weights don't change. It is **system-level adaptation**: the deployed system's behavior improves because its *artifacts* improve. Like in-context learning it happens during deployment; like training it persists durably. What makes it possible is encoding knowledge into repo artifacts rather than weights or context.

This learning operates through [three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md): **stabilisation** (narrowing distributions), **crystallisation** (prompt→code phase transition), and **distillation** (extracting procedures from reasoning). This note focuses on the verifiability gradient that runs across all three, with crystallisation — the phase transition to deterministic code — at the far end.

The machinery behind deploy-time learning — version control, diffs, tests, CI, code review — is unremarkable to programmers. But AI researchers, trained to think about adaptation in terms of weights and gradients, tend to look past it. Repo artifacts sit in a disciplinary blind spot — "just engineering" to the ML community, yet doing genuine system-level learning.

## Why Repo Artifacts

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Deploy-time learning is about making things verifiable. Karpathy identifies three properties that make a task verifiable: it must be **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate the result automatically). The more verifiable a task is, the more you can hill-climb on it — whether through RL at training time or through iteration at runtime.

The grades of the verifiability gradient are grades of learning. Moving down the table means making more of your system resettable, efficient to test, and automatically rewardable — which in turn enables tighter iteration loops.

Other approaches try to fill this space: RAG databases, persistent memory, fine-tuning on deployment logs, automated prompt optimization. The practices aren't new — prompt versioning, eval-driven development, and CI-gated prompt testing are increasingly common in LLMOps. What the deploy-time learning framework contributes is a **unifying lens**: these practices form a gradient of verifiability, and understanding the gradient helps you choose the right hardness for each piece of your system.

The key property of hardened artifacts is that they are **diffable, executable, testable, and reviewable**. A memory note like "remember to validate emails" can drift or contradict itself silently — it is none of those things. A structured output schema enforces shape and can be diffed. A test fails loudly and runs in CI. Deterministic code removes the LLM from the loop entirely. Every grade along the way is an improvement over ephemeral context.

## The Verifiability Gradient

Deterministic code is the strongest form — full crystallisation — but learning is a gradient. Each step reduces reliance on the LLM and increases verifiability:

| Grade | Example | Resettable | Efficient | Rewardable |
|-------|---------|:---:|:---:|:---:|
| Restructured prompts | Breaking a monolithic prompt into sections | Yes | No — requires human review | No — judgment call |
| Structured output schemas | JSON schemas constraining response format | Yes | Yes — automated | Partial — shape is checked, content is not |
| Prompt tests / evals | Assertions over LLM output across test cases | Yes | Yes — automated | Mostly — statistical pass rates |
| Deterministic modules | Code that replaces what was previously LLM work | Yes | Yes — automated | Yes — pass/fail |

Moving down the table, verification gets cheaper and sharper. Restructured prompts require a human to judge quality. Deterministic module tests run in milliseconds and return a boolean. The sharper the verification, the tighter the iteration loop you can run — and the faster you can hill-climb.

## Concrete Examples

The [`examples/`](../../examples/) directory contains working before-and-after pairs that demonstrate stabilisation at different grades.

### Data report: statistics → code, interpretation → LLM

[`data_report/`](../../examples/data_report/) is the unstabilised version. A single LLM agent receives a CSV file and does *everything*: parse the CSV, compute statistics (mean, median, min, max), detect trends, and write a narrative report. The LLM is doing arithmetic it could get wrong, at token cost, for work that has a single correct answer.

[`data_report_stabilized/`](../../examples/data_report_stabilized/) extracts the mechanical parts into a Python tool (`tools.py`):
- **CSV parsing** → `csv.DictReader` (deterministic)
- **Statistics** → Python's `statistics` module (deterministic)
- **Trend detection** → a simple algorithm comparing first-half vs second-half averages (deterministic)

The LLM agent (`write_narrative.agent`) now receives pre-computed stats and trends, and does only what requires judgment: interpreting what the numbers mean for the business.

The call site in the orchestrator (`main.agent`) is unchanged — `analyze_dataset(path=...)` works the same way. The implementation committed to one precise interpretation of "compute statistics" — resolving the semantic fuzziness of the natural-language spec into deterministic code — while the interface stayed stable.

### Pitchdeck evaluation: a four-stage progression

The pitchdeck examples show the same task — evaluate PDF pitch decks — at four stabilisation levels:

| Example | What moved to code |
|---------|-------------------|
| [`pitchdeck_eval/`](../../examples/pitchdeck_eval/) | Nothing — all LLM, including filename slug generation |
| [`pitchdeck_eval_stabilized/`](../../examples/pitchdeck_eval_stabilized/) | File discovery, slug generation, path construction → Python tool (`list_pitchdecks()`) |
| [`pitchdeck_eval_code_entry/`](../../examples/pitchdeck_eval_code_entry/) | Orchestration loop → Python; agents handle reasoning only |
| [`pitchdeck_eval_direct/`](../../examples/pitchdeck_eval_direct/) | Direct API calls — three abstraction levels without the CLI |

At each stage, mechanical work moves to code while the LLM stays focused on what requires judgment (analyzing the pitch deck content). The slug generation is a small example but an instructive one: in the unstabilised version, the LLM is asked to "generate a file slug (lowercase, hyphenated, no extension)" — a spec that looks precise but actually admits multiple valid interpretations (how to handle special characters, what counts as a "word," whether to transliterate accented characters). Each run might resolve these ambiguities differently, and inconsistency means broken file paths. In the stabilised version, `python-slugify` commits to one interpretation, in code, once — resolving the fuzziness permanently.

## Failure Modes

Learning through artifacts is not a free lunch. Things that go wrong:

- **Premature crystallisation.** Committing to a specific interpretation before you've observed enough runs to know which interpretation is right locks in brittle assumptions. The stabilise/soften cycle is the antidote — stabilise only when patterns have emerged across runs, and be ready to soften back to a fuzzy spec when new requirements reveal that you committed to the wrong interpretation.
- **Goodharting on evals.** Prompt tests can enshrine the wrong behavior. If your eval cases aren't representative of real traffic, improvements on the eval set may regress in production.
- **Model drift.** Vendor model updates can break crystallised prompts and schemas. Regression evals are the defense — they detect drift even when the artifact hasn't changed.
- **Bad assumptions crystallised confidently.** An agent that writes a bad test crystallises a bad assumption that now passes CI. The quality gate is typically human review — crystallisation is a human-AI collaborative process, not a purely autonomous one.

## Related Work

The individual practices are well-established. Prompt versioning and "prompts as code" are standard LLMOps advice. Eval-driven development has its own frameworks (OpenAI Evals, promptfoo) and process models ([EDDOps](https://arxiv.org/abs/2411.13768)). Automated prompt optimisation (DSPy, ProTeGi) pursues a related goal — improving system behavior without weight updates — through search over prompt components. Agent skill libraries like [Voyager](https://arxiv.org/abs/2305.16291) and evaluator-guided program evolution like [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) accumulate executable code as a form of cross-episode memory.

Deploy-time learning is a **taxonomy** (three timescales of system adaptation) and a **verifiability gradient** (from prompt tweaks to deterministic code) — a synthesis of established practices into a concrete model for when and how to move between grades. Within this gradient, the [three learning mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — stabilisation, crystallisation, distillation — operate at different points.

For how stabilisation resolves semantic fuzziness — committing to one interpretation of a fuzzy spec in a language with precise semantics — and how the stabilise/soften cycle lets systems breathe, see [agentic systems interpret fuzzy specifications](./agentic-systems-interpret-fuzzy-specifications.md).

Topics:
- [learning-theory](./learning-theory.md)
