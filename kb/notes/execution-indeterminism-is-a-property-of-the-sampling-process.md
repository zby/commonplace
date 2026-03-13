---
description: The same prompt can produce different outputs across runs due to token sampling — this is a property of the execution engine, theoretically eliminable but practically ubiquitous, and often confused with the deeper issue of underspecification
type: note
tags: [llm-interpretation-errors]
status: seedling
---

# Execution indeterminism is a property of the sampling process

LLMs sample from probability distributions over tokens. The same prompt can produce different outputs across runs. This is a property of the execution engine — conceptually simpler than underspecification, and theoretically eliminable via deterministic decoding (temperature=0).

In practice, true determinism is hard to guarantee (floating-point non-determinism, batching effects, infrastructure changes) and may not be desirable — temperature > 0 helps explore reasoning paths, enables self-consistency techniques, and avoids degenerate repetitive outputs. All deployed systems exhibit indeterminism.

## Why this matters as a distinct claim

Indeterminism is **engineering noise** — variation in how a chosen interpretation is executed, not variation in which interpretation is chosen. At temperature=0, the LLM still picks one interpretation from the space the spec admits; you just get the same one every time. This is why lowering temperature alone doesn't solve the "wrong interpretation" problem — it eliminates variation without ensuring the remaining interpretation is the one you wanted.

Counterintuitively, indeterminism **obscures** the deeper issue of [underspecification](./agentic-systems-interpret-underspecified-instructions.md). Because outputs vary across runs, people attribute the variation to randomness — "it's stochastic" — and reach for familiar tools: temperature tuning, retries, sampling strategies. This framework avoids confronting the real difference from traditional programming: that the specification language doesn't have precise semantics.

The remedy is **sampling control**: temperature adjustment, deterministic decoding, best-of-N selection. These address run-to-run variation but leave both [underspecification](./agentic-systems-interpret-underspecified-instructions.md) and [interpretation error](./interpretation-errors-are-failures-of-the-interpreter.md) untouched.

---

Relevant Notes:

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — elaborates: the full framework including how indeterminism and underspecification layer on each other
- [prompt underspecification is a property of the specification language](./prompt-underspecification-is-a-property-of-the-specification-language.md) — sibling: the deeper phenomenon that indeterminism obscures
- [interpretation errors are failures of the interpreter not the spec](./interpretation-errors-are-failures-of-the-interpreter.md) — sibling: the third phenomenon, also unaddressed by sampling control
- [LLM interpretation errors](./llm-interpretation-errors-index.md) — parent area: the three-phenomena taxonomy this note is part of

Sources:

- Ma et al. (2026). [Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.md) — cleanest empirical separation of indeterminism from underspecification: by varying prompt framing (emotion/personality) while holding task constant, they isolate the effect of interpretation choice from run-to-run sampling noise
