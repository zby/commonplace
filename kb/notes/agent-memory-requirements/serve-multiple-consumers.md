---
description: "Memory systems need multiple surfaces because acting, scheduling, review, learning, governance, and active work consume memory differently"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
---

# Serve Multiple Consumers, Not One Retrieval Interface

Different consumers need different memory surfaces. Those surfaces should meet each consumer's use pattern instead of forcing acting, scheduling, review, learning, governance, maintenance, and work-in-flight uses through one retrieval interface.

No single surface satisfies that spread. Search is useful for question answering. Navigation is useful when the reader must follow articulated relationships. Triggered activation is useful when the agent would not know to ask. Trace replay is useful when a summary is under suspicion. Active work artifacts are useful when the task is not yet finished.

Retrieval surfaces should also be allowed to say "the evidence is weak." Returning a best match is not the same as returning sufficient evidence. [Cludebot](../../agent-memory-systems/reviews/cludebot.md) makes this explicit with an experimental confidence gate that scores coverage, top result strength, diversity, and agreement, then tells the caller when the memory context should be treated as weak.

## Methods

- Always-loaded control constraints for stable purpose, scope, routing, quality, and safety material that should be available before search.
- Search over traces, observations, source summaries, and durable artifacts for direct questions.
- Link navigation and indexes for reasoning through curated knowledge rather than isolated snippets.
- Progressive-disclosure pointers: descriptions, tags, source links, episode summaries, cue titles, and compact evidence records that help the context engine decide what not to load.
- Evidence-sufficiency signals that report weak coverage, low agreement, low diversity, or low confidence before the agent overuses a thin retrieval result.
- Retrospective episodes for "what happened when we tried this?" questions.
- Active [workshops](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) or work-surface artifacts for current state, unresolved alternatives, task queues, experiments, and discussion threads.
- Trace excerpts for audit and reconstruction when compressed memory is insufficient.

## Failure Modes

The main failure is interface collapse: all memory becomes search, chat recall, or a flat record store. That loses provenance for reviewers, priority for schedulers, activation for acting agents, and state for work in motion. Retrospective memory is not active work; work in motion needs state, dependencies, expiration, and unresolved alternatives.

## Evaluation Questions

- Does each major consumer have an appropriate memory surface?
- Does retrieval expose evidence sufficiency, not only ranked matches?
- Can the system distinguish retrospective recall from active work state?
- Can the context engine cheaply decide what not to load?

---

Relevant Notes:

- [A functioning KB needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - grounds the active-work versus retrospective-memory distinction
- [Agents navigate by deciding what to read next](../agents-navigate-by-deciding-what-to-read-next.md) - grounds progressive-disclosure pointers as a way to make load decisions cheaper
- [Knowledge storage does not imply contextual activation](../knowledge-storage-does-not-imply-contextual-activation.md) - explains why retrieval alone is insufficient
