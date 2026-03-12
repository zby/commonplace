---
description: Analyses the tradeoff between conversational Q&A, prompt refinement, and context forking for sub-agent coordination — each shifts costs differently between caller and callee, and the right choice depends on architecture and how much intermediate work the sub-agent has done
type: note
traits: []
areas: [computational-model]
status: seedling
---

# Conversation vs prompt refinement in agent-to-agent coordination

When a sub-agent returns with a question instead of an answer, the calling agent has at least three options:

1. **Conversational Q&A** — answer the question and let the sub-agent continue with its accumulated context.
2. **Prompt refinement** — incorporate the answer into a revised, self-contained prompt and re-dispatch with a clean context.
3. **Hybrid** — answer the question to continue the current invocation, but also capture the answer to refine the prompt template for future similar invocations.

Conversation feels natural because humans can't rewind. Once we've said something, we can only append corrections. Agents have no such constraint — they can cheaply re-invoke with a better prompt, effectively rewinding to before the misunderstanding.

## The tradeoff

**Conversation is cheaper for the caller.** The caller just passes the answer string. The sub-agent continues with its existing context, including whatever useful work it did before asking the question.

**Prompt refinement is cleaner for the callee.** Each invocation gets a fresh [lexically scoped frame](./llm-context-is-composed-without-scoping.md) without the accumulated debris of the initial misframing, the question, and the correction. The refined prompt is more compact than the conversation transcript that includes the misunderstanding and its resolution.

**Prompt refinement is more work for the caller.** The caller must: parse the sub-agent's question, formulate the answer, integrate it into a revised self-contained prompt, and re-dispatch. This is genuine coordination work that conversation avoids.

**Conversation preserves intermediate results.** If the sub-agent has done significant work before asking the question — 80% through a long-running task, say — refinement discards all of it. Conversation preserves it. The later in the task a question arises, the stronger the case for continuing rather than restarting.

## Where should complexity live?

The tradeoff resolves differently depending on the architecture. In the [bounded-context orchestration model](./bounded-context-orchestration-model.md), the scheduler is already the coordination layer — it holds unbounded symbolic state, assembles prompts, and orchestrates the workflow. Adding prompt-refinement logic to the scheduler is incremental complexity in the right place. Adding conversation history to the sub-agent's context is wasted tokens in the [scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).

When the caller is also an LLM (the [degraded variant](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) of the clean model), prompt refinement requires the caller to do integration work within its own bounded context. The "right place for complexity" argument weakens — both sides are context-constrained.

This suggests a tentative design heuristic rather than a hard principle: **conversation is the natural interface for human-agent interaction; prompt refinement has advantages for agent-agent interaction when the caller is a symbolic scheduler.** The qualifier matters — the heuristic depends on the caller having unbounded state to work with.

## Onboarding and forking

The [voooooogel multi-agent prediction](../sources/voooooogel-multi-agent-future.md) proposes onboarding interviews — spawned instances ask questions back to their parent in an interactive conversation to gather context before starting. The argument: "it's just too difficult to ask a model to reliably spawn a subagent with a single prompt."

One reading through the refinement lens: the onboarding interview is useful not because conversation is the right interface, but because the caller's initial prompt was underspecified. The interview surfaces what the caller should have said. A refinement-oriented caller could capture those answers and build a better single-shot prompt — possibly for re-use across many similar sub-agent invocations, which a pure conversation model cannot reuse.

But voooooogel's forking pattern complicates this reading. The pattern is: spawn one sub-agent, onboard it via conversation, then fork into N instances that each carry "the whole onboarding conversation in context." This is neither pure conversation (the forked instances don't continue the dialogue) nor pure refinement (the accumulated conversation is preserved, not distilled into a clean prompt). Forking is a third pattern — **context cloning** — that gets conversation's benefit (preserving the full onboarding exchange) without conversation's cost (no further accumulation in the forked instances). With KV-cache sharing, the cloned prefix is also computationally cheap.

## Open Questions

- When does the sub-agent's partial work (before asking the question) outweigh the cost of re-doing it from a clean prompt? Is there a useful heuristic based on task progress?
- Can the refinement loop be made cheaper by having the caller maintain prompt templates that get progressively refined across multiple sub-agent invocations?
- Does the conversation/refinement distinction collapse with KV-cache sharing? If forked instances share cached prefixes, clean context may be achievable even within a conversational interface.
- Is context cloning (forking) the pattern that subsumes both, or does it have its own failure modes?

---

Relevant Notes:

- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — foundation: sub-agents as lexically scoped frames is what makes prompt refinement produce cleaner context than conversation
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the scheduler already holds the coordination state that prompt refinement requires
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: conversation adds volume (misframing and correction transcript) to the scarce context resource
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — complicates: when the caller is also an LLM, the "push complexity to the scheduler" argument weakens
- [distillation](./distillation.md) — foundation: prompt refinement is distillation — targeted extraction of the caller's knowledge into a focused artifact shaped by the sub-agent's task
- [active-campaign understanding needs a single coherent narrative](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — parallel: campaign narratives are the same operation (distillation via holistic rewrite) applied to a different target

Topics:

- [computational-model](./computational-model.md)
