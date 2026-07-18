# Chatbot goal state

## Question

The computational-model note family models one shape well: **the goal is fixed once, folded into scheduler state, and every later message is tool or code feedback.** [Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) builds the `select/call` loop this way — `K` accumulates "outputs from earlier LLM calls," not independent goal-setting acts from an outside party — and [agent-is-a-tool-loop](../../notes/agent-is-a-tool-loop.md) makes it explicit: the tool-loop convention "says nothing about autonomy, planning, or goals." This is the right model for extracting maximum power when the goal *can* be fully specified in the first message.

But a lot of real chat usage isn't that shape: the human's later messages aren't tool output, they're feedback that revises the goal itself, in response to seeing what the model produced. The question this workshop owns: **do the computational-model notes need a second, distinct shape for goal-negotiated conversation, and if so, what does its clean model look like** — not just for benchmark construction (the original framing below), but for the orchestration model itself?

## Two shapes

- **Shape A — goal-fixed loop.** The goal is set once (first message / call-time prompt), everything after is `K + r` from tool/call results. This is `bounded-context-orchestration-model.md`'s native shape, and it's optimal exactly when the goal is knowable upfront.
- **Shape B — goal-negotiated conversation.** Later turns are semantic input from a human, not symbolic tool output, and can modify or replace the goal based on what the model just produced. [The chat-history model trades context efficiency for implementation simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) already names the raw-transcript pattern, but frames it purely as an *implementation-convenience default* that mature systems should engineer away toward Shape A ("mature orchestration drifts away from pure chat history"). That may be right for the cases the note discusses, but it doesn't distinguish "chat history kept because no one designed better selection yet" from "chat history because the goal is genuinely not fixed until the human reacts to an attempt" — the latter isn't an implementation shortcut, it's what the task requires.

[Conversation vs. prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is the closest existing treatment of a turn that isn't a tool result, but it's scoped to a sub-agent asking its caller a question — the caller is still a symbolic scheduler that could in principle refine and re-dispatch. A human user at the top of the stack is not a component the architecture can compile away: their evolving judgment is exactly the semantic content Shape A's `K` can't hold before it's expressed.

## Audit findings (crux resolved)

Checked whether [any symbolic program with LLM calls is a select/call program](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md)'s universality claim already subsumes Shape B, making it a dead end. **It doesn't, but Shape B also isn't a wholly new model — it's a missing pattern inside the existing one.** The lemma types its two step kinds explicitly as symbolic computation over `K` and `call(P)`; an unsolicited human goal-revising turn is neither — it's exactly the "external mutable state not represented in `K`" case the note's own Scope section already names as out of bounds. Once the turn has arrived, `select` can stay symbolic only if goal-interpretation is *reified as an explicit LLM call* — "what does this turn do to `K.goal`?" — always inserted after a human turn. That reification is structurally identical to DST's belief-update step (above). [Scheduler-LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) grounds why this step can't be pushed onto the symbolic side: interpreting free-text goal revision is semantic judgment, which "resists cheap error correction."

Per-note audit of the rest of the candidate set:

| Note | Assumes Shape A? | Load-bearing? |
|---|---|---|
| `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` | Yes — prescribes fully factoring LLM-mediated turn-handling into code | **Real tension**: a human's judgment can't be factored into code even in the limit; the note's "degraded → recover the clean model" trajectory doesn't fit a case where negotiating with an external party is the point |
| `tool-loop-README.md` | Yes — pseudocode loop is model-vs-tools only | Incidental — silent on human mid-loop turns, not contradicted |
| `agentic-systems-interpret-underspecified-instructions.md` | No — agnostic to turn source | Orthogonal |
| `decomposition-heuristics-for-bounded-context-scheduling.md` | Implicit — optimizes decomposition of an already-given task | Incidental |
| `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` | Implicit — three-component taxonomy has no slot for a human as an active mid-loop party | Not contradicted, but a candidate site to note the gap |
| `topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` | No | Orthogonal |

(`theory-and-methodology-form-a-two-layer-execution-system.md` was a false-positive tag hit — actually `learning-theory, constraining`, not `computational-model`; excluded.)

**Recommendation: genuine gap, narrowly scoped.** Not a new K/select/call theory — a named pattern extending `bounded-context-orchestration-model.md`, parallel to how that note already names the ContextProvider pattern: goal state as an explicit, LLM-updated field of `K`, distinct from (a) raw chat-history's implicit re-derivation every call and (b) ignoring goal revision entirely (today's default in `bounded-context-orchestration-model.md` / `agent-is-a-tool-loop.md` / `tool-loop-README.md`). Plus a caveat on `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` that its factor-into-code trajectory doesn't apply when the external party is irreducibly semantic.

## Source Context

Grew out of a conversation about chat-model training and attention, not a source ingest. Working threads so far:

- Base LLM pretraining is next-token prediction over unstructured text; deployed chat models are further trained (SFT/RLHF) on role-tagged, turn-structured conversations.
- Users plausibly expect the model to follow the *goal* implied by the last user message — strongest exactly when that message replaces (not modifies) the prior goal, a case not cleanly separated from ordinary positional recency (lost-in-the-middle-style effects).
- Prior art, checked: dialogue state tracking (DST) maintains a **joint belief state updated recursively per turn** — "current joint belief relies on the generated current-turn belief and last joint belief" ([survey](https://www.emergentmind.com/topics/dialogue-state-tracking)) — structurally close to `K = K + r`, except `r` comes from parsing a human utterance, not a tool/code result. [MultiWOZ](https://arxiv.org/pdf/1810.00278) explicitly covers multi-domain goal switches at scale, and is the de facto DST benchmark. The gap: DST operates over a closed, predefined slot schema (restaurant/hotel/train fields); it doesn't need to detect an *open-ended* goal replacement the way a general-purpose chat agent would. So DST is a formal skeleton for Shape B's turn-update recursion, not a drop-in answer — the open-domain generalization is the part that's actually novel.
- [Context contamination operates below an agent's compliance reasoning](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — evidence that an explicitly superseded/refused stance still leaks at fine grain. A Shape-B goal switch may show the same signature: residual pull toward an abandoned goal, using the agent's own earlier turns as the contaminant instead of an injected artifact.
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) — names role markers and ordering as weak, unenforced scoping conventions; open question whether last-user-turn recency functions as an effective quasi-scope-reset for goal identification specifically.

**Downstream, narrower thread — benchmark construction.** [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) cites a benchmark family (lost-in-the-middle, GSM-DC, MECW, ConvexBench) that all measure retrieval of a *static* target buried in context — a Shape-A assumption. If Shape B needs its own model, those benchmarks may be testing the wrong failure mode for it: not "can you retrieve a buried fact" but "do you correctly track which goal is currently operative, and cleanly drop the superseded one," which needs a turn history, not a single needle.

## What Would Close This Workshop

A new note naming the goal-tracking pattern (explicit, LLM-reified `K.goal` update after human turns, DST-belief-update-shaped), linked from `bounded-context-orchestration-model.md`, plus a caveat added to `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` scoping its factor-into-code trajectory away from irreducibly semantic external parties. The benchmark-construction thread (needle-in-haystack-family benchmarks assume Shape A's static target) can fold into that note as a consequence, or spin out separately if it needs its own evidence base.

## Next Useful Step

Draft written: [goal-negotiated conversation needs a reified update call](./goal-negotiated-conversation-needs-a-reified-update-call.md). Pending: review for accuracy and fit, then promote to `kb/notes/` (via `cp-skill-write`/`cp-skill-validate`/`cp-skill-connect`) and delete this workshop.
