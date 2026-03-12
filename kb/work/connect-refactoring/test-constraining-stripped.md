---
description: Definition — constraining constrains the space of valid interpretations an underspecified spec admits, from partial narrowing (conventions, structured sections) to full commitment (stored outputs, deterministic code) — one of two co-equal learning mechanisms alongside distillation
type: note
traits: []
areas: [learning-theory]
status: current
---

# Constraining

One of two co-equal learning mechanisms in deployed agentic systems, alongside distillation. Constraining **constrains the interpretation space** — reducing the range of valid interpretations an underspecified spec admits. At the light end, you add constraints: a naming convention rules out some interpretations while leaving many valid ones. At the heavy end, you commit to a single interpretation: storing a specific LLM output or extracting a deterministic function collapses the space to a point. Commitment is the extreme case of constraint — what they share is that the space gets smaller and the system becomes more predictable.

## The constraining spectrum

Constraining is a gradient, not a single operation. Each step trades generality for gains in the reliability+speed+cost compound:

| Constraining | What changes | Capacity gain |
|--------------|-------------|---------------|
| Store an LLM output | Commit to one interpretation | One decision becomes permanent |
| Write a description field | Enable search without reading | One note becomes findable |
| Create a convention | Make future operations predictable | All operations of that kind become faster |
| Add structured sections | Enable type-specific operations | The document affords new workflows |
| Extract a deterministic function | Move from LLM to code | One operation becomes reliable, fast, free |

The last step — codification — is the far end of the spectrum where the medium itself changes (natural language → executable code). It produces the largest compound gain because it removes the LLM from the loop entirely. But it's not a separate mechanism — it's what constraining looks like when it crosses a medium boundary.

Many constrainings never need to codify. A well-written description field is constrained (findable, predictable) but will never become code. A naming convention constrains agent behavior without any phase transition.

## Relaxing

Relaxing — replacing a constrained component with a general-purpose one — is the reverse operation. It increases generality at the cost of the compound. When scale makes a general approach good enough on reliability+speed+cost, the bitter lesson boundary tells you to relax.

The constrain/relax cycle is a learning cycle. Each constraining constrains the interpretation space — ruling out some of what the spec previously admitted. Each relaxing reopens it — making the system more capable for the general case. The cycle isn't maintenance — it's how the system adapts.

## Relationship to distillation

Constraining and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Constrained** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, codified script) |

You can constrain without distilling (store an LLM output — commit to one interpretation, no extraction from reasoning). You can distil without constraining (extract a skill from notes — still natural language, still underspecified). The full compound gain comes when both operations apply.

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

Topics:
- [learning-theory](./learning-theory.md)
