# How a system built around prompt limitations would look

## The starting observation

Context doesn't enter the LLM through some mysterious channel — it goes through the prompt. Every piece of knowledge, every instruction, every prior exchange competes for the same finite token budget. Once you see this clearly, the dominant chat-history architecture starts to look like a design choice optimized for simplicity, not for making good use of that budget.

The question isn't "how do I manage context?" as though context were a separate concern. The question is: which tokens, in what form, at what time?

## What the chat model assumes

The dominant architecture is conversational:

- User and model exchange messages
- Full history accumulates in the prompt
- Each turn inherits the growing transcript
- "Memory" means bolting retrieval onto this conversation

This works for interactive use, and at small scale it works fine — a few turns of focused conversation are all signal. But the problems are accumulation problems. As sessions grow and tasks get complex:

- The prompt fills with transcripts rather than knowledge
- History is organized by time, not by relevance
- The model re-reads everything on every turn, including noise, false starts, and corrections
- There's no mechanism to learn across sessions — each conversation starts fresh or inherits the whole prior transcript (which is worse)

## What changes when you design around the constraint

### The prompt becomes an assembly target, not a transcript

Every token that enters the window should be there because the current task needs it, not because it happened earlier in the session. This is the `select(K)` function from the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — the scheduler picks what the next call should see, rather than inheriting whatever accumulated.

### External structured storage becomes the primary state

In the chat model, the conversation IS the state. In a prompt-limited system, external storage is primary and the prompt is a projection of it. The system maintains a knowledge base — structured, searchable, distilled — and loads selectively based on task requirements.

This is the key insight for continuous learning: the solution is external storage. Not bigger windows — they address volume but not complexity, and demand grows with supply (a Jevons paradox). Not fine-tuning — too slow to update, loses provenance, can't be inspected or selectively loaded. Not naive RAG that retrieves chunks into an otherwise conversational prompt.

What's proposed here IS retrieval-augmented generation in the broad sense — external storage, selective retrieval, assembly into a prompt. But it differs from typical RAG in treating the knowledge base and the selection function as the primary architectural concern, not an add-on to a chat loop.

### Knowledge is pre-processed for retrieval

Raw conversation transcripts are the worst format for later reuse. They mix signal with noise, bury conclusions in back-and-forth, carry phrasing that served the moment.

A prompt-limited system distills knowledge at storage time:

- Conversations produce notes, not transcripts
- Observations are separated from the reasoning that produced them
- Knowledge is structured for the next reader, not the current speaker
- Indexes and descriptions enable navigation without loading full documents

### Progressive disclosure replaces flat loading

Not everything loads at once. Instructions are layered by frequency of need:

- Always-loaded: minimal routing information (a map, not a manual)
- On-reference: definitions and constraints that load when their topic comes up
- On-demand: detailed procedures and knowledge loaded for specific tasks

This is [instruction specificity matching loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — the prompt budget is allocated like cache tiers.

### Execution boundaries become compression points

When a sub-task completes, its result crosses the boundary as a compressed artifact, not a full transcript. The parent doesn't need to know how the child reasoned — just what it concluded. This is where [distillation](../../notes/distillation.md) should be designed in: execution boundaries are the natural place to decide what survives and in what form. This doesn't happen automatically — it's an architectural choice that must be implemented at each boundary. Many systems skip it and pass full results, which is how transcript accumulation creeps back in.

## The architectural scope of this

When you build around prompt limitations, you're not just engineering what goes into the context window. You're restructuring:

- **Storage format** — knowledge structured for selective retrieval, not conversation replay
- **Retrieval architecture** — task-relevant loading, not temporal accumulation
- **Knowledge lifecycle** — distillation at storage time, curation over time
- **Session boundaries** — each call gets a fresh assembled prompt, not inherited history
- **Inter-agent communication** — compressed artifacts at execution boundaries, not shared transcripts
- **Tool design** — tool descriptions consume prompt tokens; tools must be designed for context economy, not just functionality
- **Learning mechanism** — write to external storage, not "remember this conversation"

"Context engineering" understates this. A better analogy: the prompt window is to agent systems what algorithmic complexity is to traditional systems. You don't just "optimize your algorithms" — the entire system (data structures, caching, communication protocols) is designed around the cost model. Context efficiency should pervade system design the same way.

## How this connects to continuous learning

The chat model has no built-in learning mechanism — each session starts fresh. The "memory" features that various platforms offer treat memory as a supplement to the conversation rather than redesigning around it. A [comparative review of eleven agent memory systems](../../notes/related-systems/agentic-memory-systems-comparative-review.md) finds that the deepest design split is not storage format but the *agency model* — who decides what to remember. Most systems automate extraction but not synthesis or curation, and no system has combined high agency, high throughput, and high curation quality.

A system built around prompt limitations learns differently:

- **Session → distilled knowledge**: after a session, valuable insights are extracted and stored as structured notes, not conversation logs
- **Knowledge base grows**: each session potentially contributes to a persistent, curated knowledge base
- **Retrieval improves**: as the knowledge base grows, the selection function gets better at loading what's relevant
- **Quality is maintained**: curation processes keep the knowledge base useful as it grows (unlike conversation logs which just accumulate)

The bottleneck shifts from "how much can I fit in the prompt" to "how good is my knowledge base and how well can I select from it."

## Tensions and open questions

- **Assembly cost**: building a good prompt from a knowledge base is harder than just appending to a conversation. How much intelligence does the selection function need? Can it be learned?
- **Serendipity**: conversations surface unexpected connections. A pure selection-based system might miss things a wandering conversation would catch. Is there a role for exploratory loading?
- **The cold start**: a knowledge base starts empty. Chat history at least preserves everything. What's the minimum viable knowledge base that beats transcript inheritance?
- **Curation scaling**: knowledge bases degrade without curation. Conversations don't need curation (they're disposable). Is the curation cost worth the retrieval benefit?
- **Middle ground**: is there a hybrid where short-term interaction uses conversation naturally, but the system distills and stores at session boundaries? (This is roughly what "memory" features try to do, but without redesigning the core architecture around it.)
- **Who does the selection?** In the chat model, the selection function is trivial: load everything. In a prompt-limited system, selection is the critical path. This is where the real engineering challenge lives, and it's barely discussed.

## Notes for mining later

Potential claims hiding in this exploration:

- "The prompt is an assembly target, not a transcript"
- "Continuous learning requires external structured storage, not bigger context windows"
- "Context engineering understates the architectural implications of prompt limitations"
- "The chat-history model trades prompt efficiency for implementation simplicity"
- "Selection is the critical path in prompt-limited systems"

---

Related KB notes (for context, not formal links):

- [context efficiency is the central design concern](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md)
- [session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md)
- [distillation](../../notes/distillation.md)
- [instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md)
- [frontloading spares execution context](../../notes/frontloading-spares-execution-context.md)
- [agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md)
- [agent runtimes decompose into scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md)
- [three-space memory separation predicts measurable failure modes](../../notes/three-space-memory-separation-predicts-measurable-failure-modes.md)
- [agentic memory systems comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md)
