---
description: Deploy-time learning fills the gap between slow distributed-parametric training and ephemeral in-context adaptation — durable system-definition artifacts updated across sessions during deployment
type: kb/types/note.md
traits: [has-comparison, title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Deploy-time learning is the missing middle

[Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) argues that the continual-learning objective foregrounds durable [system-definition](./definitions/system-definition-artifact.md) writes that install fast, and that such writes span three representational forms. This note develops the timing axis behind *fast*: when, across a deployed system's lifecycle, a durable write can land — and why the durable-and-fast cell is the one readable artifacts occupy.

## Three timescales

Two structural axes describe a durable write: *when* it lands across a deployed system's lifecycle, and whether it *persists* past the run that produced it. Three timescales populate them:

| Timescale | When it lands | Persists past the run? | Form that occupies it today (contingent) |
|-----------|---------------|------------------------|------------------------------------------|
| **Training** | Before deployment | Yes | Distributed-parametric state |
| **In-context** | Within a session | No — evaporates at session end | Context window |
| **Deploy-time** | Across sessions, during deployment | Yes | Readable system-definition artifacts (natural-language + symbolic) |

The **missing middle is the durable-and-fast cell**: training buys durability at the cost of speed, in-context buys speed at the cost of durability, and deploy-time is the corner that is both.

Timing and [representational form](./definitions/representational-form.md) are orthogonal, so the last column records what *currently* occupies each cell, not a law — any form could in principle land at any timescale. Readable artifacts hold the deploy-time cell today not because readability is intrinsic to that timing, but because parametric updates cannot yet validate fast enough to live there. Even where the update step gets cheap, its validation radius does not shrink with it: establishing that a parametric update changed only what it should is the expensive half, [which the readable-artifact loop bounds through explicit dependencies](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). That makes "readable forms own the middle" a current empirical claim with a named falsifier — [OpenClaw-RL](https://arxiv.org/html/2603.10165v1), which runs live RL from user interactions, is a frontier probe of parametric updates at deployment pace. If that path generalises, the deploy-time cell stops being readable-only.

Deploy-time learning is system-level adaptation: behaviour improves because *artifacts* improve — during deployment like in-context, durable like training, but inspectable and tool-compatible throughout.

## Why AI researchers look past it

Traditional stateful software — CRMs, rule engines, document stores — counts as learning by Simon's criterion, but trivially: ordinary engineering handles it, so researchers filter it out. What they miss is how *large* a behaviour change can grow from durable system-definition artifacts.

A single prompt edit looks small, but a library of tips, schemas, tools, and tests accumulated across sessions is a different object. [Context efficiency](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) is why: progressive disclosure, skill routing, and retrieval into [homoiconic context](./llm-context-interprets-instructions-and-content-through-one-medium.md) make the effective context far larger than the literal window, so stored artifacts can deliver behaviour change at weight-update scale. Researchers trained to think through gradients have mostly looked past it.

## Mechanisms

Two operators drive the updates: [constraining](./definitions/constraining.md) (narrowing the interpretation space) and adaptation (reshaping prior reasoning into task-ready artifacts). [Codification](./definitions/codification.md), the far end of constraining, is where prompts undergo a phase transition into deterministic code. Both are reversible: commitments tighten along [the verifiability gradient](./verifiability-gradient.md) when cross-run patterns make them safe, and loosen when new evidence shows them wrong. A system that can only tighten ratchets itself into brittleness.

## Co-evolving natural-language and code

Agile was already doing deploy-time learning, with an asymmetry: code and specs co-evolved, but only code executed, so moving a concern back to natural-language meant taking it out of production. LLMs close the asymmetry — prompts execute, so loosening a codified behaviour back to natural-language keeps the system running.

You deploy with behaviour in prompts, observe what works, codify the understood parts, and the prompts evolve as the code absorbs them. The boundary between code and natural-language moves as understanding accumulates.

The end state also differs. Agile treats natural-language specs as temporary — stories waiting to become code. Deploy-time learning recognises that some parts *should stay in natural language* because they require judgment deterministic code can't capture. The hybrid is the end state, not a waypoint.

## Boundary

This note is the timing argument alone. How distributed-parametric, natural-language, and symbolic [representational forms](./definitions/representational-form.md) should coevolve is [treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md).

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — foundation: the objective-level claim whose fast-install demand this note develops on the timing axis
- [Treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) — extends: asks how deploy-time natural-language/symbolic loops relate to distributed-parametric loops
- [The verifiability gradient](./verifiability-gradient.md) — extends: the ladder that deploy-time artifacts move along in both directions
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — sharpens: the repo is Commonplace's storage substrate choice for many durable system-definition artifacts
- [LLM contexts interpret instructions and content through the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md) — mechanism: lets content function as instruction, not only as data
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — lever: selective access patterns make the effective context far larger than the window, which is what lets stored-artifact behaviour change reach weight-update scale
- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — extends: agile's "changing requirements" reframed through the interpretation-error lens
- [Context Engineering for AI Agents in OSS](https://arxiv.org/pdf/2510.21413) — validates: 466 OSS projects treat AI context files as maintained software artifacts
- [ABC: Agent Behavioral Contracts](https://arxiv.org/html/2602.22302v1) — extends: behavioural contracts are verifiable repo artifacts that improve reliability without weight updates
- [Harness Engineering (Lopopolo, 2026)](https://openai.com/index/harness-engineering/) — exemplifies: "good harnesses compound" in practitioner language
- [Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/) — sibling: AI lowers the cost of mutating durable artifact stacks, not replacing them
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning depends on deploy-time learning to build the context-engineering machinery
