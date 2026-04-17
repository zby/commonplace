---
description: Deploy-time learning fills the gap between training (slow, opaque) and in-context (ephemeral) — durable system-definition artifacts updated across sessions during deployment
type: note
traits: [has-comparison, title-as-claim]
tags: [learning-theory]
---

# Deploy-time learning is the missing middle

[Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) names system-definition artifacts as the cheap behaviour-change mechanism alongside expensive weight updates. This note places that mechanism on the timing axis.

## Three timescales

Deployed systems adapt at three timescales, each on a different substrate:

| Timescale | When | Substrate | Properties |
|-----------|------|-----------|------------|
| **Training** | Before deployment | Weights | Durable but opaque; heavy infrastructure; can't incorporate deployment-specific information |
| **In-context** | Within a session | Context window | Inspectable but ephemeral; evaporates at session end |
| **Deploy-time** | Across sessions, during deployment | Durable system-definition artifacts (prose + symbolic) | Durable, inspectable, versionable |

Substrate and timing are orthogonal axes in principle. The combination the table leaves empty — weight updates at deployment pace — exists but stays rare because training infrastructure is heavy. [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md), which runs live RL from user interactions, is a current example.

Deploy-time learning is system-level adaptation: behaviour improves because *artifacts* improve — during deployment like in-context, durable like training, but inspectable and tool-compatible throughout.

## Why AI researchers look past it

Traditional stateful software — CRMs, rule engines, document stores — counts as learning by Simon's criterion, but trivially: ordinary engineering handles it, so researchers filter it out. What they miss is how *large* a behaviour change can grow from durable system-definition artifacts.

A single prompt edit looks small, but a library of tips, schemas, tools, and tests accumulated across sessions is a different object. [Context efficiency](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) is why: progressive disclosure, skill routing, and retrieval into [homoiconic context](./llm-context-is-a-homoiconic-medium.md) make the effective context far larger than the literal window, so stored artifacts can deliver behaviour change at weight-update scale. Researchers trained to think through gradients have mostly looked past it.

## Mechanisms

Two operators drive the updates: [constraining](./definitions/constraining.md) (narrowing the interpretation space) and [distillation](./definitions/distillation.md) (re-compressing prior reasoning into task-ready artifacts). [Codification](./definitions/codification.md), the far end of constraining, is where prompts undergo a phase transition into deterministic code. Both are reversible: commitments tighten along [the verifiability gradient](./verifiability-gradient.md) when cross-run patterns make them safe, and loosen when new evidence shows them wrong. A system that can only tighten ratchets itself into brittleness.

## Co-evolving prose and code

Agile was already doing deploy-time learning, with an asymmetry: code and specs co-evolved, but only code executed, so moving a concern back to prose meant taking it out of production. LLMs close the asymmetry — prompts execute, so loosening a codified behaviour back to prose keeps the system running.

You deploy with behaviour in prompts, observe what works, codify the understood parts, and the prompts evolve as the code absorbs them. The boundary between code and prose moves as understanding accumulates.

The end state also differs. Agile treats natural-language specs as temporary — stories waiting to become code. Deploy-time learning recognises that some parts *should stay in prose* because they require judgment deterministic code can't capture. The hybrid is the end state, not a waypoint.

## Boundary

This note is the timing argument alone. How opaque, prose, and symbolic substrates should coevolve is [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md).

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — foundation: places system-definition artifacts on the timing axis
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: asks how deploy-time prose/symbolic loops relate to opaque weight loops
- [The verifiability gradient](./verifiability-gradient.md) — extends: the ladder that deploy-time artifacts move along in both directions
- [Axes of substrate analysis](./axes-of-substrate-analysis.md) — sharpens: the repo is commonplace's backend choice within the broader system-definition substrate
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets content function as instruction, not only as data
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — lever: selective access patterns make the effective context far larger than the window, which is what lets stored-artifact behaviour change reach weight-update scale
- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — extends: agile's "changing requirements" reframed through the interpretation-error lens
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.ingest.md) — validates: 466 OSS projects treat AI context files as maintained software artifacts
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — extends: behavioural contracts are verifiable repo artifacts that improve reliability without weight updates
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "good harnesses compound" in practitioner language
- [Flawed Ephemeral Software Hypothesis](../sources/the-flawed-ephemeral-software-hypothesis.ingest.md) — sibling: AI lowers the cost of mutating durable artifact stacks, not replacing them
- [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: in-context learning depends on deploy-time learning to build the context-engineering machinery
