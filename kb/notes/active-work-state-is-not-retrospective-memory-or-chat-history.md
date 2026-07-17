---
description: "Active work state needs current pointers, evidence gates, and closure; treating it as retrospective memory or chat history preserves the wrong state"
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [agent-memory, context-engineering]
---

# Active work state is not retrospective memory or chat history

Active work state is the retained state of unfinished work: the current goal, next action, blockers, still-binding decisions, open evidence gates, and closure criteria. It is memory in the broad sense that it is retained behavior-shaping state, but it is not retrospective memory and it is not chat history.

Retrospective memory answers "what happened?" or "what should we remember for later?" Chat history preserves the interaction trace in chronological order. Active work state answers a different question: "what is live now, what must happen next, and when can this work leave the active set?"

Those surfaces fail differently when collapsed. Chat history preserves too much tactical debris and makes each resumed session reconstruct the real state from a trace. Retrospective memory preserves lessons or episodes, but it usually lacks current task pointers, unresolved gates, directional dependencies, and a success state. A growing project instruction file can keep facts visible, but it has no built-in reason to delete work that is done.

The stronger design is a workshop surface: a compact current pointer plus a richer active ledger, both scoped to the project and removed from startup context when the work closes. The code-grounded [Claude Workstream Kit review](../agent-memory-systems/reviews/claude-workstream-kit.md) is useful because it implements this distinction directly: `ACTIVE.md` is pushed at session start, `workstream.md` carries the active ledger, closure requires evidence and user approval, and archive/tag/removal keep closed work from remaining ambient context. Its limits are equally instructive: evidence gates and fresh-context verification are mostly procedural instructions, so higher-authority systems still need executable validators or review gates.

For Commonplace, the implication is that active work belongs in the workshop layer first. Durable notes should receive extracted decisions, learnings, or requirements after closure; raw chat or session traces should remain evidence; and retrospective memory should not be asked to carry live state. A future active-work surface should therefore optimize for project scope, a cheap resume pointer, explicit gates, lifecycle closure, and extraction into library artifacts rather than for general recall.

---

Relevant Notes:

- [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - grounds: defines the library/workshop lifecycle distinction this note applies to active work state.
- [Serve Multiple Consumers, Not One Retrieval Interface](./agent-memory-requirements/serve-multiple-consumers.md) - extends: names active work as a separate memory surface and warns against interface collapse.
- [Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) - grounds: explains why persisted traces should not automatically become the next prompt.
- [The chat-history model trades context efficiency for implementation simplicity](./the-chat-history-model-trades-context-efficiency-for-implementation.md) - contrasts: chat history is useful as an exploratory default but becomes inefficient once the needed state shape is known.
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) - grounds: active work state must be read back at the moment it matters, not merely stored.
- [Claude Workstream Kit](../agent-memory-systems/reviews/claude-workstream-kit.md) - evidence: implements repo-local active work state with session-start read-back, lifecycle closure, evidence gates, and verifier roles.
- [Ingest: Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) - abstracted-from: initial source that proposed the active-work-state distinction before code-grounded review.
