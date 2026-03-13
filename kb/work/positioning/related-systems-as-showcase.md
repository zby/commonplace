---
description: The related-systems reviews are a concrete demonstration of the KB's value — useful comparisons that could not have been produced by a bare LLM or a simple RAG setup
type: note
traits: []
tags: [kb-design]
status: seedling
---

# The related-systems reviews are the best proof the knowledge layer works

We have reviews of 15 agent memory systems — Mem0, Graphiti, Cognee, Letta, A-MEM, AgeMem, Ars Contexta, Thalo, ClawVault, CrewAI Memory, Siftly, sift-kg, Spacebot, Decapod, Hindsight, SAGE, and getsentry/skills — plus a [comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md) that synthesizes across all of them along six architectural dimensions.

These reviews were mostly vibed — minimal human input, agent-driven analysis. And they're already useful. Someone choosing an agentic memory system today would benefit from:

- The [agency model taxonomy](../../notes/related-systems/agentic-memory-systems-comparative-review.md) (who decides what to remember — agent-self-managed vs developer-managed vs human-collaborative vs RL-trained)
- Per-system reviews that go beyond README claims to actual code analysis
- Cross-cutting patterns: what converges (progressive disclosure, extraction automation) and what diverges (storage model, link structure, curation operations)
- Honest gap analysis — including gaps in our own system

## Why this matters for positioning

1. **It's a live demo.** The reviews themselves were produced using the KB. Each new review built on the previous ones — the comparative framework emerged from accumulation, not upfront design. This is the compounding effect in action.

2. **It solves a real problem people have right now.** The agent memory space is exploding and nobody has a good map. Our reviews provide one. This is immediately useful regardless of whether someone adopts our framework.

3. **It shows the difference between retrieval and composition.** A RAG system could surface individual facts about Mem0 or Graphiti. It could not produce the comparative review — that required traversing links across reviews, recognizing patterns, and synthesizing a novel argument (the agency trilemma). That's what composable knowledge enables.

4. **Mostly vibed = low barrier.** The reviews demonstrate that the framework doesn't require heroic human effort. An agent with structured knowledge and good conventions produces useful analysis with minimal steering.

## How to use this in positioning

- Lead with the comparative review as a flagship artifact — it's the most immediately valuable thing in the KB for an external audience
- Individual system reviews serve as proof of depth — pick 2-3 that the audience would recognize
- The "mostly vibed" story addresses the "sounds like a lot of work" objection
- Frame as: "this is what your agents could produce about YOUR domain if they had a knowledge layer"

## Open Questions

- Should we publish the reviews standalone (blog post, GitHub pages)?
- Do we need to add caveats about the vibed nature, or is transparency about it actually a strength?
- Which reviews need a quality pass before external exposure?
