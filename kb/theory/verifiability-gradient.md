---
description: Retained artifacts differ in how cheaply they can be reset, re-run and rewarded; code extraction can improve several of those together, none follows from symbolic form or determinism alone, and learning moves artifacts in both directions
type: types/note.md
traits: [has-comparison]
tags: [learning-theory, constraining, evaluation]
---

# The verifiability gradient

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.
> — Andrej Karpathy, [Verifiability](https://karpathy.bearblog.dev/verifiability/)

Karpathy identifies three properties that make a task verifiable: **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate results automatically). The more verifiable a task is, the more you can hill-climb on it — through RL at training time, or through iteration at runtime.

Retained artifacts used in [deployment-time adaptation through retained artifacts](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) sit on a gradient of verifiability:

| Grade | Example | Resettable | Efficient | Rewardable |
|-------|---------|:---:|:---:|:---:|
| Restructured prompts | Breaking a monolithic prompt into sections | Yes | No — requires human review | No — judgment call |
| Structured output schemas | JSON schemas constraining response format | Yes | Yes — automated | Partial — shape is checked, content is not |
| Prompt tests / evals | Assertions over LLM output across test cases | Yes | Yes — automated | Mostly — statistical pass rates |
| Deterministic modules | Code that replaces what was previously LLM work | Yes | Yes — automated | Against its own tests — pass/fail; task adequacy needs a separate oracle |

Moving down the table, verification gets cheaper and sharper. Restructured prompts need a human to judge quality; deterministic module tests run in milliseconds and return a boolean. Four properties move together down the table without being one property: whether a consumer is held to a reference, how cheaply the artifact can be inspected, how cheaply it executes, and how strong an oracle it admits. Code extraction improves several at once in a named case, such as a `format_date()` function with its test suite. None follows from symbolic membership or from determinism alone: an adopted model package is a fixed reference that supplies no task oracle, and a text note like "remember to validate emails" can be diffed and reviewed while lacking an executable check.

## The gradient runs both ways

The tempting reading is that learning means climbing the gradient — prompts become schemas become tests become code. But that treats hardening as the whole game. Learning means moving in *either* direction based on evidence:

- **Tighten** when verification holds up across runs. Repeated judgment calls become schemas; stable behavior becomes tests; settled algorithms become code.
- **Loosen** when the verification itself turns out to be wrong — a test passing while quality regresses, a schema that excludes valid outputs, an eval that goodharted. When the check that justified a constraint breaks, the constraint loses its warrant.

Verifiability makes the choice possible. You cannot decide whether to tighten or loosen without being able to check whether the current level is working — that is the practical payoff of the gradient's Karpathy-style properties.

[Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) develops the bidirectional dynamics and the signals that trigger relaxation. This note specifies the ladder those movements happen along.

## Placement, not climbing

The individual practices the gradient unifies — prompt versioning, eval-driven development, CI-gated prompt testing, automated prompt optimisation (DSPy, ProTeGi), evaluator-guided program evolution (FunSearch) — are each well-established in LLMOps. What the gradient adds is a **placement test**: for any given artifact, you can ask where it currently sits and whether that grade matches its evidential maturity. A judgment call hardened into a deterministic module before its pattern stabilises is misplaced; a stable behavior still living as loose natural-language is also misplaced.

---

Relevant Notes:

- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) — frames the deployment-time adaptation path whose retained artifacts the gradient grades
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — develops the bidirectional movement along the gradient
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — parallel framing: Karpathy's verifiability properties are an oracle-strength argument
- [Symbolic form holds consumers to a semantic reference](./symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: reference adoption is separate from inspection cost and from adequacy to the task
- [ABC: Agent Behavioral Contracts](https://arxiv.org/html/2602.22302v1) — exemplifies: behavioral contracts (YAML DSL specs with runtime enforcement) sit at the far end of the gradient for behavioral constraints
