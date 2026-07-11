---
description: Constraining via LLM code generation freezes a single projection of the spec in one shot, but progressive constraining observes behavior across many runs and commits only the interpretations that consistently emerge
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# Progressive constraining commits only after patterns stabilize

LLMs can generate code from a spec — spec in, code out. But this is *projection*, not compilation: the LLM resolves the semantic ambiguity of the spec and produces one valid implementation from the space the spec admits. See [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) for why spec-to-program is many-to-one rather than semantics-preserving.

This property gives LLM code generation a specific character: it is **one-shot constraining** — freeze a single projection of the spec into code. Whatever interpretation the LLM landed on this run becomes law, and the other valid interpretations are discarded silently. Regenerating the same spec later may produce a different law.

The alternative is **progressive constraining**: don't freeze on one run. Observe the LLM's behavior across many runs, identify which interpretations it consistently favours, and extract *those* stable patterns into deterministic code — keeping the LLM for genuinely ambiguous cases.

Example: a file-renaming agent initially uses LLM judgment for everything. You notice it always lowercases and replaces spaces with underscores — so you extract `sanitize_filename()` to code. The agent still handles ambiguous cases ("is '2024-03' a date or a version?"), but the common path is now deterministic.

The two modes trade off differently:

- **One-shot** commits immediately. You get a deterministic artifact now, but the commitment is arbitrary — whatever the LLM sampled on that run. If the spec was wide, the chance that the frozen projection matches what you actually wanted is low.
- **Progressive** defers commitment. You only codify what's empirically stable across runs, so the resulting code reflects behavior the system actually exhibited — not a single sample of what the spec allows. You pay for this with observation time and the cost of running the underspecified version longer.

Progressive is [codification](./definitions/codification.md) taken seriously: commit to symbolic media where a pattern has proven itself, not where the spec happens to admit it. One-shot is faster when the spec is narrow enough that one projection is as good as another — or when you genuinely don't care which interpretation wins. Progressive pays off when the interpretation space is wide and only part of it matters in practice.

Either way, **version both spec and artifact**. Regeneration is another projection — potentially a different resolution of the same ambiguity — not a deterministic rebuild from source.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the projection model explains why code generation freezes one of many valid interpretations
- [codification](./definitions/codification.md) — related: progressive constraining is codification applied only to patterns that stabilize across runs
- [constraining](./definitions/constraining.md) — related: both modes are constraining moves; they differ in when commitment happens
- [storing-llm-outputs-is-constraining](./storing-llm-outputs-is-constraining.md) — parallel: storing a single generated artifact is also a one-shot projection; the same tradeoff between immediate commitment and preserved optionality applies to artifacts, not just code
