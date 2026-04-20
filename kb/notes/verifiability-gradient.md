---
description: Symbolic artifacts sit on a gradient from loose prose to deterministic code; higher-verifiability artifacts support tighter iteration loops, and learning moves artifacts along it in both directions
type: kb/types/note.md
traits: [has-comparison]
tags: [learning-theory]
---

# The verifiability gradient

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Karpathy identifies three properties that make a task verifiable: **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate results automatically). The more verifiable a task is, the more you can hill-climb on it — through RL at training time, or through iteration at runtime.

Symbolic artifacts used in [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) sit on a gradient of verifiability:

| Grade | Example | Resettable | Efficient | Rewardable |
|-------|---------|:---:|:---:|:---:|
| Restructured prompts | Breaking a monolithic prompt into sections | Yes | No — requires human review | No — judgment call |
| Structured output schemas | JSON schemas constraining response format | Yes | Yes — automated | Partial — shape is checked, content is not |
| Prompt tests / evals | Assertions over LLM output across test cases | Yes | Yes — automated | Mostly — statistical pass rates |
| Deterministic modules | Code that replaces what was previously LLM work | Yes | Yes — automated | Yes — pass/fail |

Moving down the table, verification gets cheaper and sharper. Restructured prompts need a human to judge quality; deterministic module tests run in milliseconds and return a boolean. Hardened artifacts are **diffable, executable, testable, and reviewable** — a memory note like "remember to validate emails" is none of those.

## The gradient runs both ways

The tempting reading is that learning means climbing the gradient — prompts become schemas become tests become code. But that treats hardening as the whole game. Learning means moving in *either* direction based on evidence:

- **Tighten** when verification holds up across runs. Repeated judgment calls become schemas; stable behavior becomes tests; settled algorithms become code.
- **Loosen** when the verification itself turns out to be wrong — a test passing while quality regresses, a schema that excludes valid outputs, an eval that goodharted. When the check that justified a constraint breaks, the constraint loses its warrant.

Verifiability makes the choice possible. You cannot decide whether to tighten or loosen without being able to check whether the current level is working — that is the practical payoff of the gradient's Karpathy-style properties.

[Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) develops the bidirectional dynamics and the signals that trigger relaxation. This note specifies the ladder those movements happen along.

## Placement, not climbing

The individual practices the gradient unifies — prompt versioning, eval-driven development, CI-gated prompt testing, automated prompt optimisation (DSPy, ProTeGi), evaluator-guided program evolution (FunSearch) — are each well-established in LLMOps. What the gradient adds is a **placement test**: for any given artifact, you can ask where it currently sits and whether that grade matches its evidential maturity. A judgment call hardened into a deterministic module before its pattern stabilises is misplaced; a stable behavior still living as loose prose is also misplaced.

---

Relevant Notes:

- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — frames where on the system-adaptation timescale the gradient operates
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — develops the bidirectional movement along the gradient
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — parallel framing: Karpathy's verifiability properties are an oracle-strength argument
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — exemplifies: behavioral contracts (YAML DSL specs with runtime enforcement) sit at the far end of the gradient for behavioral constraints
