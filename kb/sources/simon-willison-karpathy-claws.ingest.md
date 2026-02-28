---
source_snapshot: simon-willison-karpathy-claws.md
ingested: 2026-02-22
type: conceptual-essay
domains: [ai-agents, terminology, personal-computing, agent-architecture]
---

# Ingest: Andrej Karpathy talks about "Claws"

Source: simon-willison-karpathy-claws.md
Captured: 2026-02-22
From: https://simonwillison.net/2026/Feb/21/claws/

## Classification

Type: **conceptual-essay** -- Simon Willison amplifies and contextualizes Karpathy's tweet-essay, arguing that "Claw" is crystallizing as a term of art for a new category of AI system. The primary content is definitional framing, not a build report or research finding.

Domains: ai-agents, terminology, personal-computing, agent-architecture

Author: Simon Willison is one of the most widely-read voices in the developer tools / AI intersection, with a strong track record of identifying terms and trends early (he helped popularize "vibe coding" coverage). Karpathy, the quoted source, coined "vibe coding" itself and has broad credibility as an ML practitioner turned public educator.

## Summary

Karpathy describes "Claws" as a new layer of the AI stack sitting on top of LLM agents, characterized by orchestration, scheduling, persistent context, tool calls, and personal-hardware execution. He highlights NanoClaw's ~4000-line auditable core and container-by-default execution as appealing properties. Willison endorses the terminological shift, arguing "Claw" is becoming the generic term for the OpenClaw-like category of agent systems that run locally, communicate via messaging protocols, and handle both direct instructions and autonomous scheduled tasks. The post is primarily about naming a category that has been emerging across multiple projects.

## Connections Found

/connect discovered four substantive connections to existing knowledge notes plus one sibling snapshot:

1. **[voooooogel-multi-agent-future](../../../docs/notes/research/voooooogel-multi-agent-future.md)** (exemplifies) -- Claws are the productized realization of voooooogel's prediction about what survives in multi-agent systems: filesystem collaboration, agent spawning, persistent cross-session state. What was theoretical a month ago now has a category name and commercial implementations.

2. **[container-security-boundary](../../../docs/notes/container-security-boundary.md)** (validates) -- NanoClaw's "runs everything in containers by default" directly validates the design direction explored in this note. Containers as the single security mechanism is not just an llm-do idea; it is emerging as the default in the Claw ecosystem.

3. **[deploy-time-learning](../../../docs/notes/deploy-time-learning-the-missing-middle.md)** (extends) -- Claws apply crystallisation's third timescale (across-session adaptation) to agent infrastructure itself. Persistent scheduling and accumulated context mean the agent system adapts over time, not just the artifacts it produces. This is a dimension crystallisation does not currently address.

4. **[dynamic-agents-runtime-design](../../../docs/notes/dynamic-agents-runtime-design.md)** (contrasts) -- Claws sit at the persistent end of a spectrum where llm-do's dynamic workers sit at the ephemeral, session-scoped end. Both share the concept of runtime-created agents with tool access, but Claws add persistence, scheduling, and cross-session identity.

5. **Sibling snapshot: Personal Brain OS** (convergence) -- Both this post and koylanai's "file system is the new database" piece describe personal AI systems converging on local execution + filesystem memory + session persistence, reinforcing that this is a recognized category, not isolated experiments.

The strongest connection is the contrast with dynamic-agents-runtime-design -- it directly positions llm-do's design choices on a spectrum where Claws represent the other end. The voooooogel connection is also strong: Claws are what "sticking around" looks like in practice.

## Extractable Value

1. **Terminology tracking: "Claw" as category name** -- If this term sticks (Karpathy + Willison signal suggests it will), llm-do should be positioned relative to it. llm-do is not a Claw, but it operates in adjacent design space. Having clear language for the boundary matters. [quick-win]

2. **NanoClaw's ~4000-line auditable core as validation** -- The emphasis on codebase size fitting "into both my head and that of AI agents" is a direct endorsement of the small-core, auditable-by-agents design philosophy. This is a useful external data point for arguing that llm-do's compact design is a feature, not a limitation. [just-a-reference]

3. **Container-by-default as ecosystem convergence** -- NanoClaw's container approach confirms this is not just a good idea but an emerging industry default. Strengthens the case for prioritizing container execution in llm-do. [just-a-reference]

4. **Scheduling as the gap** -- Claws include autonomous scheduling (cron-like task execution) as a defining feature. llm-do currently has no scheduling capability. This is the clearest functional gap between llm-do and the Claw category. Worth tracking as a potential future direction. [experiment]

5. **Persistence spectrum as design vocabulary** -- The session-scoped (llm-do) vs. persistent (Claws) contrast is a useful conceptual axis for explaining llm-do's design position. "We chose the ephemeral end of the persistence spectrum because..." is a clearer framing than "we don't do that." [quick-win]

6. **"Layer on top of LLM agents" framing** -- Karpathy's stack model (LLMs -> LLM agents -> Claws) suggests a question: where does llm-do sit? It is an agent framework (layer 2), not a Claw (layer 3). But its dynamic workers and crystallisation features push toward layer 3 territory without the full persistence/scheduling commitment. This tension is worth articulating. [deep-dive]

## Recommended Next Action

Write a note titled "claws-category-and-llm-do-positioning" connecting to [dynamic-agents-runtime-design](../../../docs/notes/dynamic-agents-runtime-design.md) and [deploy-time-learning](../../../docs/notes/deploy-time-learning-the-missing-middle.md) -- it would argue that llm-do occupies a deliberate position on the ephemeral-to-persistent spectrum, sharing Claws' emphasis on runtime agent creation and container isolation but choosing session-scoped ephemerality and crystallisation-via-artifacts over always-on persistence and scheduling. The note would use the Claw category definition as a foil to clarify what llm-do is and is not.
