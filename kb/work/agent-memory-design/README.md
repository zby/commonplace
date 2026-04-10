# Workshop: Agent Memory Design

## Question

What would an ideal memory system for agents look like if storage were treated as cheap, session logs were captured in full, and almost all design effort moved from storage policy to retrieval and activation?

## Why this workshop exists

This workshop starts from a strong working premise: the binding constraint in agent systems is not disk, it is bounded context. That suggests a design inversion:

- store aggressively, including session logs, intermediate artifacts, corrections, and observations
- spend design intelligence on retrieval, activation, promotion, and graduation

The goal is to work out what architecture makes that premise usable rather than noisy. A store-everything system without good retrieval is just a larger haystack.

The workshop is grounded in the KB's existing memory and context-engineering theory, plus the comparative review of agent memory systems. It focuses especially on the value of session logs as a substrate for decision provenance, correction consolidation, preference mining, procedure extraction, and ADR drafting.

## Current grounding

- [Agentic memory systems comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md) — comparative baseline across current memory architectures
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — why retrieval and activation are the real bottleneck
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) — raw traces are valuable but should not be loaded directly
- [Agent statelessness makes routing architectural, not learned](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — why memory routing must be externalized
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — why this design work belongs in `kb/work/`

## What this workshop needs to resolve

1. What layered architecture makes "store everything, load selectively" practical?
2. What retrieval methods surface action-relevant knowledge rather than just answer semantic queries?
3. What useful signal types can be extracted from session logs, and which of them have clear enough oracles to automate?
4. Where is the boundary between the memory system and standard project artifacts like code, docs, ADRs, and CLAUDE.md?
5. What graduation pathways turn accumulated observations into durable artifacts without creating premature maintenance burden?

## Working hypotheses

- Session logs are a primary memory substrate, not disposable exhaust.
- Raw traces should be retained for provenance but not loaded directly into active context.
- Observation and episode layers are likely the missing middle between raw traces and curated library notes.
- Search is a better fit for lower memory layers; navigation is a better fit for synthesized artifacts and library notes.
- The memory system should feed manual distillation workflows like ADRs and conventions before trying to replace them.

## Starter artifacts

- [framing.md](./framing.md) — overall premise, open questions, and why session logs matter
- [explore-layered-architecture.md](./explore-layered-architecture.md) — four-layer proposal: trace, observation, episode, library
- [explore-retrieval-activation.md](./explore-retrieval-activation.md) — retrieval strategies, cue design, and "why" queries across many sessions
- [explore-learning-from-logs.md](./explore-learning-from-logs.md) — extraction taxonomy, oracle quality, and graduation difficulty
- [explore-boundary-and-graduation.md](./explore-boundary-and-graduation.md) — where memory ends, where project artifacts begin, and how artifacts graduate
- [synthesis-ideal-memory-system.md](./synthesis-ideal-memory-system.md) — current synthesis draft combining the workshop's conclusions

## Open questions

- How inspectable should the retrieval policy be versus how much should be learned from usage?
- Can composite weak signals from session logs produce a practical soft oracle for promotion and graduation?
- How should episode boundaries be detected when work spans multiple sessions or interleaves topics?
- What storage medium fits each layer best without making the system operationally awkward?
- When does storing everything become retrieval pollution rather than useful substrate?
