---
description: Definition — constraining narrows the space of valid interpretations an underspecified spec admits, from partial narrowing (conventions, structured sections) to full commitment (stored outputs, deterministic code) — one of two co-equal learning mechanisms alongside distillation
type: note
traits: []
tags: [learning-theory]
status: current
---

# Constraining

One of two co-equal learning mechanisms in deployed agentic systems, alongside [distillation](./distillation.md). Constraining **narrows the interpretation space** — reducing the range of valid interpretations an [underspecified spec](./agentic-systems-interpret-underspecified-instructions.md) admits. At the light end, you add constraints: a naming convention rules out some interpretations while leaving many valid ones. At the heavy end, you commit to a single interpretation: storing a specific LLM output or extracting a deterministic function collapses the space to a point. Commitment is the extreme case of constraint — what they share is that the space gets smaller and the system becomes more predictable.

## The constraining spectrum

Constraining is a gradient, not a single operation. Each step trades generality for gains in the reliability+speed+cost compound:

| Constraining | What changes | Capacity gain |
|--------------|-------------|---------------|
| Store an LLM output | Commit to one interpretation | One decision becomes permanent |
| Write a description field | Enable search without reading | One note becomes findable |
| Create a convention | Make future operations predictable | All operations of that kind become faster |
| Add structured sections | Enable type-specific operations | The document affords new workflows |
| Extract a deterministic function | Move from LLM to code | One operation becomes reliable, fast, free |

The last step — [codification](./codification.md) — is the far end of the spectrum where the medium itself changes (natural language → executable code). It produces the largest compound gain because it removes the LLM from the loop entirely. But it's not a separate mechanism — it's what constraining looks like when it crosses a medium boundary.

Many constraints never need to codify. A well-written description field is constrained (findable, predictable) but will never become code. A naming convention constrains agent behavior without any phase transition.

## Relaxing

Relaxing — replacing a constrained component with a general-purpose one — is the reverse operation. It increases generality at the cost of the compound. When scale makes a general approach good enough on reliability+speed+cost, the [bitter lesson boundary](bitter-lesson-boundary.md) tells you to relax.

The constrain/relax cycle is a learning cycle. Each constraining step narrows the [interpretation space](./agentic-systems-interpret-underspecified-instructions.md) — ruling out some of what the spec previously admitted. Each relaxing reopens it — making the system more capable for the general case. The cycle isn't maintenance — it's how the system adapts.

## Relationship to distillation

Constraining and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Constrained** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, codified script) |

You can constrain without distilling (store an LLM output — commit to one interpretation, no extraction from reasoning). You can distil without constraining (extract a skill from notes — still natural language, still underspecified). The full compound gain comes when both operations apply.

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

---

Relevant Notes:

- [codification](./codification.md) — the far end of the constraining spectrum: constraining that crosses a medium boundary
- [distillation](./distillation.md) — co-equal mechanism: targeted extraction shaped by use case, context budget, and agent; orthogonal to constraining
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the underspecification framework that constraining operates on
- [storing LLM outputs is constraining](./storing-llm-outputs-is-constraining.md) — the simplest instance: committing to one interpretation by keeping a specific output
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — applies: the instruction → skill → hook → script gradient is constraining applied to methodology
- [error messages that teach are a constraining technique](./error-messages-that-teach-are-a-constraining-technique.md) — instance: teaching error messages constrain interpretation space by simultaneously blocking wrong outputs and demonstrating correct ones
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the verifiability gradient across which constraining operates
- [bitter lesson boundary](./bitter-lesson-boundary.md) — determines when constraining is permanent vs when relaxing is needed
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — grounds: probabilistic compliance model (p,δ,k) and Drift Bounds Theorem quantify how much drift each enforcement layer permits — formal statement of the constraining trade-off
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "encode standards directly into the repository" is constraining in practitioner language at production scale
