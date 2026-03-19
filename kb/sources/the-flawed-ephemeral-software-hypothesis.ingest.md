---
description: Essay distinguishing vibe coding from true software ephemerality, arguing that state, integration, interface stability, and auditability keep important systems anchored to durable artifact stacks.
source_snapshot: the-flawed-ephemeral-software-hypothesis.md
ingested: 2026-03-19
type: conceptual-essay
domains: [software-engineering, agent-systems, verification, artifact-durability]
---

# Ingest: The Flawed Ephemeral Software Hypothesis

Source: the-flawed-ephemeral-software-hypothesis.md
Captured: 2026-03-19
From: https://www.blackhc.net/essays/future_of_software/

## Classification
Type: conceptual-essay — Kirsch is arguing for a framing, not reporting a built system or presenting original empirical results. The essay's contribution is conceptual decomposition: vibe coding vs ephemeral software, ambiguity vs formal semantics, and malleability vs disposability.
Domains: software-engineering, agent-systems, verification, artifact-durability
Author: Andreas Kirsch is an ML researcher/practitioner writing from inside the current agentic-coding discourse. The signal here is not privileged data so much as a technically literate attempt to cash out hype claims in software-engineering mechanisms.

## Summary

Kirsch argues that AI coding tools make software easier to generate and modify, but do not make important software disposable. His core thesis is that code generation has never been the dominant bottleneck in mature systems; the hard part is discovering correct behavior under real-world ambiguity, edge cases, state migrations, integration quirks, interface expectations, and audit requirements. On this view, the future is not "ephemeral software" regenerated from prompts with high trust, but "malleable software": code and surrounding artifacts become cheaper to update together, while durable stacks of code, tests, specs, logs, schemas, and operational memory grow rather than disappear.

## Connections Found

`/connect` found a tight learning-theory cluster rather than a broad "AI coding" cluster. The strongest connection is to [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md), because Kirsch's decisive objection to ephemerality is exactly that natural-language specifications remain underspecified and each regeneration is a fresh interpretation, not a deterministic rebuild. It also extends [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md): Kirsch's "malleable software" is basically deploy-time learning stated at whole-system scale, with durable artifact stacks rather than prompt tweaks as the adaptation substrate.

The essay also sharpens [ephemeral-computation-prevents-accumulation](../notes/ephemeral-computation-prevents-accumulation.md) by naming where ephemerality stops working in practice: state, integration surfaces, interface stability, and auditability. It grounds [codification](../notes/codification.md) in practitioner language by arguing that code remains the source of truth because formal executable semantics are where ambiguity finally gets resolved. Finally, it supports the seedling note [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): Kirsch's economic argument is that cheap generation just moves cost into validation, integration testing, incident response, and trust maintenance.

## Extractable Value

1. **Concrete threshold variables for when ephemerality breaks**: state, integration surfaces, interface stability, and auditability are a better boundary test than vague "important software" language. This is high-reach because it explains *why* disposability fails across domains, not just *where* Kirsch thinks it fails. [quick-win]
2. **A two-axis decomposition of "ephemerality"**: regeneration frequency and artifact durability separate "we rewrite code more often" from "the codebase stops mattering." This is a cleaner analytical frame than treating all AI-assisted generation as evidence for disposability. [quick-win]
3. **"Malleable software" as public-facing vocabulary for deploy-time learning**: the KB already has the mechanism, but Kirsch supplies a more legible phrase for the system-level outcome: persistent artifact stacks with radically cheaper modification. [quick-win]
4. **Falsifiable indicators for the ephemerality hypothesis**: accepted prompt/spec-only audit regimes in regulated domains, median deployed code age collapsing to hours/days, and falling persisted-artifact volume per service are concrete measurements we could actually watch. This is better than arguing from vibes or startup rhetoric. [experiment]
5. **A stakeholder-friendly compiler/rewrite rebuttal**: Kirsch packages the formal-semantics argument and the historical rewrite argument in a way that transfers beyond LLM discourse. Useful when explaining why "just regenerate it" fails even if model capability improves. [just-a-reference]
6. **A useful separation between cheap generation and cheap trust**: the essay makes explicit that AI can commoditize code production while leaving trust-maintenance workflows expensive. That distinction transfers beyond software to any artifact domain with verification costs. [deep-dive]

## Limitations (our opinion)

This is a strong conceptual essay, but it is still mostly an argument by mechanism and analogy rather than by hard evidence. The essay cites market signals, rewrite history, and a few quality studies, but it does not present direct evidence on the thing it is really predicting: whether persisted engineering artifact stacks actually grow or shrink under heavy AI use. Its falsification section is good because it names the missing measurements; the current essay does not supply them.

The essay is also somewhat too code-centric for our framework. Kirsch says "code remains the source of truth," but our stronger version is closer to [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md): important systems stabilize through *artifact stacks*, not code alone. Tests, schemas, rollout policies, runbooks, audit logs, and operational traces are part of the durable layer too. This matters because his conclusion is directionally right, but "code remains central" is weaker than "durable inspectable artifacts remain central."

Finally, the essay may under-model hybrid futures. [Agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) and [ephemeral-computation-prevents-accumulation](../notes/ephemeral-computation-prevents-accumulation.md) together suggest a more varied picture than "ephemeral" versus "not ephemeral": many systems will likely combine ephemeral local regeneration with durable surrounding artifacts. Kirsch acknowledges this, but the polemical frame pushes him toward a binary rejection of ephemerality where the more accurate conclusion is probably substrate-splitting: ephemeral where verification is cheap and stakes are low, durable where ambiguity and consequence accumulate.

## Recommended Next Action

Done — Kirsch's malleable software thesis is covered in the Related Work section of [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md).
