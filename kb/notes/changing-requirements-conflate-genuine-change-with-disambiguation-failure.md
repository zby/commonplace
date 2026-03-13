---
description: "Agile's 'changing requirements' hide two distinct phenomena — genuine change (world moved) and late discovery that downstream specs committed to a wrong interpretation of an underspecified upstream spec — short iterations limit interpretation-error propagation, not just change-response latency"
type: note
traits: []
tags: [learning-theory]
status: seedling
---

# Changing requirements conflate genuine change with disambiguation failure

The standard agile narrative frames short iterations as a response to change: requirements shift because markets move, users give feedback, stakeholders change their minds. But some of what presents as "changing requirements" is actually **late discovery of interpretation errors** — the requirements didn't change, they were never precise enough to prevent divergent readings.

## The cascading interpretation problem

Specs are always [underspecified](./agentic-systems-interpret-underspecified-instructions.md) — natural language doesn't have precise denotations. When Spec A is underspecified, Spec B (written downstream) silently commits to one interpretation of A. Further specs build on B's interpretation. If that interpretation later turns out wrong, the entire downstream chain breaks — and it looks like "requirements changed."

But nothing changed. The ambiguity was present in Spec A from the start. What happened is that B's author performed a **projection** — collapsing the space of valid interpretations to one — and nobody noticed until the consequences surfaced. The later the discovery, the more downstream work is invalidated.

This is the same one-to-many mapping that the [spec-to-program projection model](./agentic-systems-interpret-underspecified-instructions.md) describes for LLM systems. Traditional development has the same structure, just less visibly: a human developer reads a spec, picks an interpretation, and builds on it. The interpretation choice is implicit — buried in implementation decisions rather than surfaced as a distinct step.

## Two kinds of "changing requirements"

What agile calls "changing requirements" conflates:

1. **Genuine change** — the world moved. The market shifted, users want something different, a stakeholder revised their goals. The original spec was correct at the time; the target moved.
2. **Disambiguation failure surfacing late** — the spec was always ambiguous. Someone downstream committed to one reading. That reading turned out wrong. The spec didn't change; the interpretation was always a gamble, and the bet lost.

These demand different responses. Genuine change requires adapting to new information. Disambiguation failure requires going back to the original spec and choosing a different interpretation — or narrowing the spec to prevent the same ambiguity from recurring.

## What short iterations actually do

The agile insight that short iterations "reduce risk" is usually framed as: deliver faster so you can respond to change faster. But for disambiguation failures, the mechanism is different: **short iterations limit how far a wrong interpretation can propagate before it's caught**.

In waterfall, a wrong interpretation in an early spec can cascade through months of downstream work before anyone deploys and discovers the error. In agile, you deploy after weeks — so the wrong interpretation has less downstream work built on top of it when it surfaces. The cost of correction is proportional to how much was built on the wrong reading.

This reframes iteration length as an **interpretation-error propagation bound**, not just a change-response latency. Even in a world where requirements never genuinely changed, short iterations would still be valuable — because specs are always underspecified and interpretation errors are inevitable.

## Implications for deploy-time learning

[Deploy-time learning extends agile's loop](./deploy-time-learning-is-agile-for-human-ai-systems.md) to human-AI systems. The disambiguation failure problem is amplified there because:

- LLM systems make the projection explicit — every prompt invocation picks an interpretation
- The interpretation choice is visible (you can compare outputs across runs) but not controllable (you can't predict which interpretation will be chosen)
- [Constraining](./constraining.md) is the direct mechanism for resolving disambiguation — committing to one interpretation and hardening it into a less ambiguous form

The deploy-time learning cycle (deploy → observe → constrain → repeat) is precisely a disambiguation loop: each iteration catches interpretation errors and narrows the spec for next time.

## Open Questions

- What fraction of "requirement changes" in real agile projects are genuine change vs disambiguation failures? Is there empirical data?
- Does this reframing change how teams should do retrospectives — distinguishing "we learned the world changed" from "we discovered our reading of the spec was wrong"?
- Are there spec-writing practices (from [legal drafting](./legal-drafting-solves-the-same-problem-as-context-engineering.md) or elsewhere) that specifically reduce cascading interpretation errors rather than just reducing ambiguity in a single spec? Augment's [bidirectional spec pattern](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) is a candidate: agents surface directional decisions (interpretation choices that changed the plan) back to the spec in real time, catching disambiguation failures before they cascade into downstream work.

---

Relevant Notes:

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the spec-to-program projection model that makes interpretation explicit
- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — extends: agile's loop applied to human-AI systems, where disambiguation is amplified
- [constraining](./constraining.md) — enables: the mechanism for resolving disambiguation by committing to one interpretation
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — parallel: law's centuries of methodology for preventing cascading interpretation errors in natural language specs
- [Augment bidirectional spec](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) — exemplifies: agents surface interpretation choices back to the spec in real time, a concrete practice for reducing cascading disambiguation errors
