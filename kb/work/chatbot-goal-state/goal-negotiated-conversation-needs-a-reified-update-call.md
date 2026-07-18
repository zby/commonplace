---
description: When a human turn revises the goal rather than supplying tool output, the select/call model stays clean only if that revision is reified as an explicit LLM call updating K.goal — not left to implicit re-derivation from raw history, and not silently folded in as ordinary tool output
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model]
---

# Goal-negotiated conversation needs a reified update call

[Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) types its loop as symbolic computation over `K` alternating with bounded calls `r = call(P)`. [Any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) claims this covers the full space of such architectures, but its own Scope section carves out an exception: "external mutable state not represented in `K`." An unsolicited human turn that revises the goal itself is exactly that — not symbolic computation, and not a `call(P)` the scheduler asked for.

The model stays clean only if that revision is reified as its own call: `K.goal' = call(interpret_goal_revision, K.goal, turn)`, inserted after every human turn. `select` stays symbolic; the one genuinely semantic operation — does this turn modify the goal, replace it, or leave it untouched — goes to the LLM side, where [scheduler-LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) says it belongs: free-text interpretation "resists cheap error correction" and can't be done as bookkeeping. This is a pattern inside the existing model, the same status as the ContextProvider pattern the orchestration note already names — not a new theory.

## Two failure modes this avoids

Without an explicit `K.goal`, two things go wrong. **Raw history** ([the chat-history model](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md)) re-derives the goal from the full transcript every call; with no scoping boundary between the current and abandoned goal ([LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md)), it leaks — [context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) is direct evidence that even an explicitly superseded stance keeps pulling at fine grain. **Silent tool-loop defaults** ([agent-is-a-tool-loop](../../notes/agent-is-a-tool-loop.md)) fold a goal-revising turn into `K` like any other result, with nothing that notices the goal moved at all — the opposite failure, understating the revision instead of drowning in it. The reified update call sits between: it doesn't carry the full deliberation forward, but it doesn't let a change pass unmarked either.

## Precedent, and what's actually novel

Task-oriented dialogue systems already run this recursion for a closed schema: dialogue state tracking updates a belief state each turn from that turn's evidence and the prior state ([Mrkšić et al., 2017](https://arxiv.org/abs/1606.03777)), and [MultiWOZ](https://arxiv.org/abs/1810.00278) (Budzianowski et al., 2018) covers exactly this across multi-domain goal switches. What DST doesn't need to solve is the open-ended case — its slots are fixed, so "did the goal change" is a classification problem. A general chat agent's goal has no fixed schema; recognizing modify-versus-replace is a judgment call, which is why the update has to be an LLM call rather than a trained classifier. The recursion isn't new; generalizing its target from closed slots to an open-ended goal is.

## One thing this rules out

[LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) treats LLM-mediated bookkeeping as a state to escape by factoring it into code. That doesn't apply here: there's no symbolic endpoint to recover, because the party whose judgment is being tracked — a human — isn't part of the system that could be rewritten. `interpret_goal_revision` is essential, not a placeholder for code not yet written.

## Open Question

Does distinguishing "modifies" from "replaces" need more than `K.goal` plus the new turn, or can an implicit shift only be caught with a window of recent history? And the pattern's own new failure mode: the update call can misclassify a turn, where raw history at least preserves the ambiguity for a human to notice — is there a cheap confidence check that doesn't reintroduce the cost this pattern is meant to avoid?

---

Sources:
- Mrkšić et al. (2017). [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777) — belief state updated per turn from current-turn and prior-turn evidence, the update recursion this note's pattern generalizes.
- Budzianowski et al. (2018). [MultiWOZ: A Large-Scale Multi-Domain Wizard-of-Oz Dataset for Task-Oriented Dialogue Modelling](https://arxiv.org/abs/1810.00278) — multi-domain conversations with goal switches at scale, the closed-schema precedent for tracked goal replacement.

Relevant Notes:

- [Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — extends: names a second concrete pattern within the select/call model, alongside ContextProvider
- [Any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — grounds: its own Scope section names the boundary case this note resolves
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: why goal interpretation must be an LLM call, not symbolic bookkeeping
- [The chat-history model trades context efficiency for implementation simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) — contrasts: names the raw-accumulation default this pattern replaces with an explicit update
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) — mechanism: explains why the raw-history default has no boundary between current and abandoned goal
- [Context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — evidence: the fine-grained leakage signature the raw-history failure mode predicts
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrasts: its factor-into-code trajectory doesn't apply when the external party is irreducibly semantic
- ["Agent" is a useful technical convention, not a definition](../../notes/agent-is-a-tool-loop.md) — contrasts: the tool-loop shape whose silent-ignore gap this note's second failure mode names
