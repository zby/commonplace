---
description: "Agile's 'changing requirements' hide two distinct phenomena — genuine change (world moved) and late discovery that downstream specs committed to a wrong interpretation of an underspecified upstream spec — short iterations limit interpretation-error propagation, not just change-response latency"
type: kb/types/note.md
traits: []
tags: [learning-theory, deploy-time-learning]
---

# Changing requirements conflate genuine change with disambiguation failure

Agile's "changing requirements" conflate two phenomena: genuine world-change and late discovery that downstream specs committed to a wrong reading of an underspecified upstream spec. Short iterations bound how far a wrong interpretation propagates—not only how fast teams respond to genuine change. Markets move, users give feedback, stakeholders revise goals—but some churn is **late discovery of interpretation errors**: the requirements did not change; they were never precise enough to prevent divergent readings.

## The cascading interpretation problem

Specs are always [underspecified](./agentic-systems-interpret-underspecified-instructions.md) — natural language doesn't have precise denotations. When Spec A is underspecified, Spec B (written downstream) silently commits to one interpretation of A. Further specs build on B's interpretation. If that interpretation later turns out wrong, the entire downstream chain breaks — and it looks like "requirements changed."

But nothing changed. The ambiguity was present in Spec A from the start. What happened is that B's author performed a **projection** — collapsing the space of valid interpretations to one — and nobody noticed until the consequences surfaced. The later the discovery, the more downstream work is invalidated.

The same one-to-many mapping appears in the [spec-to-program projection model](./agentic-systems-interpret-underspecified-instructions.md) for LLM systems; traditional development follows the same structure with interpretation buried in implementation rather than surfaced as a distinct step.

## Two kinds of "changing requirements"

What agile calls "changing requirements" conflates:

1. **Genuine change** — the world moved. The market shifted, users want something different, a stakeholder revised their goals. The original spec was correct at the time; the target moved.
2. **Disambiguation failure surfacing late** — as in the cascade above: someone downstream committed to one reading, the bet lost, and the spec itself did not change.

These demand different responses. Genuine change requires adapting to new information. Disambiguation failure requires going back to the original spec and choosing a different interpretation — or narrowing the spec to prevent the same ambiguity from recurring.

## What short iterations actually do

The agile insight that short iterations "reduce risk" is usually framed as: deliver faster so you can respond to change faster. But for disambiguation failures, the mechanism is different: **short iterations limit how far a wrong interpretation can propagate before it's caught**.

In waterfall, a wrong interpretation in an early spec can cascade through months of downstream work before anyone deploys and discovers the error. In agile, you deploy after weeks — so the wrong interpretation has less downstream work built on top of it when it surfaces. The cost of correction grows with how much was built on the wrong reading.

This reframes iteration length as an **interpretation-error propagation bound**, not just a change-response latency. Even in a world where requirements never genuinely changed, short iterations would still be valuable — because specs are always underspecified and interpretation errors are inevitable.

## Deploy-time learning

[Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) extends the same loop to human–AI systems: each deploy surfaces interpretation choices that prose specs left open, and [constraining](./definitions/constraining.md) narrows the spec for the next cycle. Every prompt invocation performs an explicit projection, so misreadings surface faster—but the agile propagation bound still applies: shorter cycles limit how much downstream work rests on a wrong reading before correction.

## Open Questions

- What fraction of "requirement changes" in real agile projects are genuine change vs disambiguation failures? Is there empirical data?
- Does this reframing change how teams should do retrospectives — distinguishing "we learned the world changed" from "we discovered our reading of the spec was wrong"?
- Are there spec-writing practices that specifically reduce cascading interpretation errors rather than just reducing ambiguity in a single spec? See [specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) for lifecycle-dependent answers.

---

Relevant Notes:

- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — sharpens: the downstream cascade starts with a runtime event whose degraded status should have been surfaced when the first ambiguity was locally repaired