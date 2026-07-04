<!-- Draft (2026-07-04): the reading path that makes the "interactive textbook" claim real —
a curated spine through the graph for a newcomer. Companion to
landing-for-agentic-systems-builders.md. Promotion target once stable: a curated index
in the library (location TBD — kb/notes/ index or site page). -->

# Reading path: the knowledge layer of agentic systems

A curated spine through the knowledge base for builders new to it. Every note's title is its claim; each step builds on the ones before it. Read it yourself in an hour, or hand this file to your coding agent as the traversal order and ask your questions as you go.

## Part 1 — The constraint

Everything in agentic-system design is downstream of one scarce resource.

1. [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — the binding constraint is silent reliability degradation across volume, complexity, and interference, not the provider's token limit.
2. [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — context is scarce for two distinct reasons, feasibility and cost, and feasibility binds first; nearly every architectural pattern is a response to this pressure.
3. [Context engineering](../../notes/definitions/context-engineering.md) — the discipline this forces: getting the right knowledge into a bounded context at the right time.

## Part 2 — Knowledge that changes behavior

Storing knowledge is easy. Making it change what the agent does is the actual problem.

4. [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — the load-bearing distinction of the whole KB: knowledge that exists, knowledge loaded into context, and knowledge that actually changes behavior are three different things.
5. [In-context learning presupposes context engineering](../../notes/in-context-learning-presupposes-context-engineering.md) — "the model will figure it out from context" assumes selection machinery that is itself a system you have to build and improve.
6. [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — the minimal quality basis for remembered knowledge: if artifacts aren't discoverable, composable, and trusted, storage is dead weight.
7. [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — memory decomposes into storage (solved), retrieval/activation (Part 1–2), and learning (Part 3); the hard problems live at the intersections, which is why "add a memory product" rarely fixes them.

## Part 3 — Learning during deployment

Your system will meet reality after you ship it. Where does what it learns go?

8. [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — between slow parametric retraining and ephemeral in-context adaptation sits the underbuilt layer: durable, inspectable artifacts updated across sessions during deployment.
9. [Distillation](../../notes/definitions/distillation.md) and [constraining](../../notes/definitions/constraining.md) — the two orthogonal moves that layer performs: extracting use-shaped artifacts from larger material, and narrowing the space of valid interpretations (up to [codification](../../notes/definitions/codification.md) into schemas and code).
10. [Constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md) — continuous learning can happen outside of weights: prompts, schemas, tools, and tests accumulate adaptive capacity you can read and audit.

## Part 4 — When it fails

11. [Interpretation errors are failures of the interpreter](../../notes/interpretation-errors-are-failures-of-the-interpreter.md) — real LLMs violate explicit constraints and fumble fully specified bookkeeping; design for an imperfect interpreter rather than a noisy-but-valid one.
12. [Failure modes](../../notes/failure-modes-README.md) — the taxonomy of ways knowledge can exist in your system without ever changing agent behavior.

## Capstone — the field, surveyed

- [What the matrix shows across 141 agent memory systems](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — every claim above, tested against the field: 141 code-grounded reviews classified on shared axes, showing that storage substrate predicts little and the real forks are who decides what to remember and whether memory ever reaches behavior.

## Where next

- [Browse by topic](../../notes/tags-README.md) — the tag hub: foundations, learning theory, context engineering, tool loop, observability, and more.
- [Browse the system reviews](../../agent-memory-systems/README.md) — find the systems closest to your architecture and read what their source code actually does.
