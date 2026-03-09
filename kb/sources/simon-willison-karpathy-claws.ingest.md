---
source_snapshot: simon-willison-karpathy-claws.md
ingested: 2026-03-09
type: conceptual-essay
domains: [ai-agents, terminology, agent-architecture, personal-computing]
---

# Ingest: Andrej Karpathy talks about "Claws"

Source: simon-willison-karpathy-claws.md
Captured: 2026-02-22
From: https://simonwillison.net/2026/Feb/21/claws/

## Classification

Type: **conceptual-essay** -- Simon Willison amplifies and contextualizes Karpathy's tweet-essay, arguing that "Claw" is crystallizing as a term of art for a new category of AI system. The primary content is definitional framing, not a build report or research finding.

Domains: ai-agents, terminology, agent-architecture, personal-computing

Author: Simon Willison is one of the most widely-read voices in the developer tools / AI intersection, with a strong track record of identifying terms and trends early (helped popularize "vibe coding" coverage). Karpathy, the quoted source, coined "vibe coding" itself and has broad credibility as an ML practitioner turned public educator. When both endorse a term, adoption is likely.

## Summary

Karpathy describes "Claws" as a new layer of the AI stack sitting on top of LLM agents, characterized by orchestration, scheduling, persistent context, tool calls, and personal-hardware execution. He highlights NanoClaw's ~4000-line auditable core and container-by-default execution as appealing properties. Willison endorses the terminological shift, arguing "Claw" is becoming the generic term for the OpenClaw-like category of agent systems that run locally, communicate via messaging protocols, and handle both direct instructions and autonomous scheduled tasks. The post is primarily about naming a category that has been emerging across multiple projects.

## Connections Found

The `/connect` discovery found six substantive connections, informed by the fact that the "Claw" term has already been deeply absorbed into the KB's vocabulary (20+ files reference it across notes, ingest reports, and comparative analyses):

1. **[claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md)** -- **grounds**: This source is the definitional anchor that note builds on. The note explicitly cites this snapshot as the source for what a "Claw" is and argues the learning loop must serve action capacity (classification, planning, communication), not just retrieval.

2. **[deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md)** -- **extends**: Claws embody deploy-time learning's "across sessions" timescale applied to agent infrastructure itself. Karpathy's emphasis on persistence and accumulated context is the Claw variant of artifact-mediated adaptation. Karpathy is also quoted in this note for the verifiability concept.

3. **[bounded-context-orchestration-model](../notes/bounded-context-orchestration-model.md)** -- **exemplifies**: Karpathy lists "orchestration, scheduling, context, tool calls" as defining Claw properties. Claws are a product-category instantiation of the symbolic scheduling model with persistence as an additional dimension.

4. **[ClawVault](../notes/related-systems/clawvault.md)** -- **enables**: This source provides the category definition that ClawVault is an instance of. ClawVault's scored observations, session handoffs, and reflection pipelines are a concrete Claw implementation.

5. **[inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md)** -- **exemplifies**: NanoClaw's ~4000-line core that "fits into both my head and that of AI agents" is a concrete endorsement of the inspectable substrate thesis from an independent practitioner.

6. **[What Survives in Multi-Agent Systems](./voooooogel-multi-agent-future.ingest.md)** -- **exemplifies**: Claws are the productized realization of voooooogel's prediction about what survives in multi-agent systems: filesystem collaboration, agent spawning, persistent cross-session state. What was theoretical now has a category name and commercial implementations.

The strongest connection is to [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) -- the source has already done its primary work by grounding the "Claw" concept that the note theorizes about. The term's adoption into the KB vocabulary is effectively complete.

## Extractable Value

1. **Term adoption already complete.** The "Claw" category name has been fully absorbed into the KB vocabulary, used in note titles, descriptions, and cross-references across 20+ files. The primary extractable value of this source -- the terminology -- has already been captured. [just-a-reference]

2. **NanoClaw's auditable ~4000-line core as evidence for inspectability.** Karpathy's emphasis on codebase size "fitting into both my head and that of AI agents" is an independent endorsement of the inspectable substrate thesis. Useful as a citation point but not a new insight for the KB. [just-a-reference]

3. **Container-by-default as ecosystem convergence signal.** NanoClaw's container approach adds another data point to the convergence pattern already noted in the related-systems index. Multiple independent Claw implementations choosing containers as the default security boundary strengthens the pattern. [just-a-reference]

4. **Karpathy's three-layer stack model (LLMs -> LLM agents -> Claws).** This framing positions the Claw category relative to other system types. The KB's computational model notes (symbolic scheduling, context efficiency) operate at the "LLM agents" layer. The question of whether and how the scheduling model extends to the persistent Claw layer -- adding scheduling across sessions and autonomous task execution -- remains unexplored. [experiment]

5. **Scheduling as a distinguishing feature.** Karpathy identifies scheduling (autonomous task execution, cron-like behavior) as a defining Claw property. The KB's scheduling model currently addresses within-session orchestration. Cross-session scheduling is a different problem with different constraints (state persistence, failure recovery, user intent drift). [experiment]

6. **Ecosystem proliferation as a convergence signal.** The mention of multiple independent Claw implementations (NanoClaw, nanobot, zeroclaw, ironclaw, picoclaw) is itself evidence that the architectural pattern is robust -- independent teams converge on similar designs. This convergence pattern is already tracked in the related-systems index but could be strengthened with the Claw ecosystem as additional evidence. [just-a-reference]

## Recommended Next Action

File as reference -- the source's primary value (the "Claw" category definition and terminology) has already been fully absorbed into the KB through the [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) note and its downstream connections. The extractable value items marked [experiment] (three-layer stack model, cross-session scheduling) are genuinely interesting but would need separate source material on specific Claw implementations to develop further -- this blog post is too thin on technical detail to ground new notes.
