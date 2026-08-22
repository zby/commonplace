---
description: When the agent scheduler lives inside an LLM conversation it becomes bounded and degrades; three recovery strategies — compaction, externalisation, factoring into code — restore the clean separation to increasing degrees
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# LLM-mediated schedulers are a degraded variant of the clean model

The [symbolic scheduling model](./bounded-context-orchestration-model.md) requires transition-relevant state to be explicit outside each bounded call and inter-call execution to be symbolic. It does not require physically unbounded state. In practice, many current systems (Claude Code, Codex, chat-based agent loops) carry part of the transition state and progression decision in an LLM conversation. The LLM then serves as both scheduler and executor — it decides what to do next from its accumulated conversation history.

This puts part of scheduling inside a bounded call, where it can suffer the same attention dilution and compositional overhead as the work it is trying to orchestrate. The separation between explicit external state and bounded calls is then incomplete.

The framework-design consequence is developed in [tool loop](./tool-loop-README.md): a framework can expose control surfaces that let an application move selected progression decisions out of chat. Whether that is worthwhile still requires a stated comparison criterion.

## Three recovery strategies

Three responses move different parts of scheduling out of conversational context:

1. **Compaction.** Keep summaries and conclusions rather than raw results in the conversation, condensing the scheduler's own state around what later steps need. This can reduce context burden, but progression is still LLM-mediated.

2. **Externalisation.** Write intermediate state to files and re-read selectively. This makes scheduler state explicit outside the LLM context, but it does not by itself make the later transition logic symbolic.

    The [Ralph Loop](https://x.com/Vtrivedy10/status/2031408954517971368) is a concrete pattern combining externalisation with extreme compaction: a hook intercepts the model's exit attempt and reinjects the original prompt in a clean context window, while the filesystem bridges iterations. Each loop cycle starts with zero accumulated context but reads state from the previous iteration — externalisation provides continuity, compaction (taken to its logical extreme of full context reset) prevents degradation.

3. **Factoring into code.** Encode the bookkeeping and recursion as a program that runs outside the LLM conversation entirely. When code owns the transition logic and state is explicit, the workflow meets the normal form's conditions. The LLM is then called only for judgment steps; this does not by itself establish that the architecture is best for every objective.

These are different placements of bookkeeping, recursion, and state management. They can be compared only against stated objectives and constraints, such as context cost, latency, reliability, or auditability.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the closed-world symbolic-scheduling form that LLM-mediated scheduling falls outside
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — mechanism: compaction reshapes conversation state into a handoff artifact for the next stage
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: the degradation is a context-efficiency problem within the scheduler itself
- [The Anatomy of an Agent Harness (Vtrivedy10, 2026)](https://x.com/Vtrivedy10/status/2031408954517971368) — exemplifies: the Ralph Loop pattern combines externalisation and compaction to sustain long-horizon agent work across multiple clean context windows
