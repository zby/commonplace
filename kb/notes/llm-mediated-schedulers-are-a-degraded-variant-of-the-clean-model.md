---
description: When the agent scheduler lives inside an LLM conversation it becomes bounded and degrades; three recovery strategies — compaction, externalisation, factoring into code — restore the clean separation to increasing degrees
type: note
traits: []
tags: [computational-model]
status: seedling
---

# LLM-mediated schedulers are a degraded variant of the clean model

The [symbolic scheduling model](./bounded-context-orchestration-model.md) assumes the scheduler is a program with unbounded exact state. In practice, many current systems (Claude Code, Codex, chat-based agent loops) carry orchestration state partly in an LLM conversation. The LLM serves as both scheduler and executor — it decides what to do next based on its accumulated conversation history.

This makes the scheduler effectively bounded: it suffers the same attention dilution and compositional overhead as the sub-agent calls it is trying to orchestrate. The clean separation between unbounded scheduler and bounded LLM calls collapses.

## Three recovery strategies

Three responses restore the separation to increasing degrees:

1. **Compaction.** Keep summaries and conclusions rather than raw results in the conversation, applying [distillation](./distillation.md) to the scheduler's own state. This reduces degradation but does not eliminate it.

2. **Externalisation.** Write intermediate state to files and re-read selectively. This moves scheduler state out of the conversation and into exact symbolic state outside the LLM context — partially recovering the clean model.

    The [Ralph Loop](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) is a concrete pattern combining externalisation with extreme compaction: a hook intercepts the model's exit attempt and reinjects the original prompt in a clean context window, while the filesystem bridges iterations. Each loop cycle starts with zero accumulated context but reads state from the previous iteration — externalisation provides continuity, compaction (taken to its logical extreme of full context reset) prevents degradation.

3. **Factoring into code.** Encode the bookkeeping and recursion as a program that runs outside the LLM conversation entirely. This fully recovers the clean model. The LLM is called only for judgment steps; the scheduler is code.

Each recovery moves the system closer to the clean model — bookkeeping, recursion, and exact state management in the symbolic layer; bounded LLM calls reserved for the semantic judgments they are uniquely needed for — and the architectural direction is toward the third option.

---

Relevant Notes:

- [symbolic scheduling over bounded LLM calls is the right model for agent orchestration](./bounded-context-orchestration-model.md) — foundation: the clean model that LLM-mediated scheduling degrades from
- [distillation](./distillation.md) — mechanism: compaction is distillation applied to the scheduler's own conversation state
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: the degradation is a context-efficiency problem within the scheduler itself
- [The Anatomy of an Agent Harness (Vtrivedy10, 2026)](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) — exemplifies: the Ralph Loop pattern combines externalisation and compaction to sustain long-horizon agent work across multiple clean context windows
