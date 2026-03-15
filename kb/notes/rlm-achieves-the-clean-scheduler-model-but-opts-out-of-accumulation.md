---
description: RLM externalises the scheduler into ephemeral code, achieving the clean bounded-call architecture without accumulation — a boundary case separating loop externalisation from loop persistence
type: note
traits: []
tags: [computational-model]
status: seedling
---

# RLM achieves the clean scheduler model but opts out of accumulation

Recursive Language Models (RLMs) have the LLM write and execute code in a REPL, with a `recursive_llm(query, context)` primitive that spawns fresh LLM calls. The pattern maps directly onto the [symbolic scheduler model](./bounded-context-orchestration-model.md):

| Model component | RLM implementation |
|---|---|
| Symbolic state K | Python REPL namespace (variables) |
| Bounded LLM call | `recursive_llm(query, context)` |
| Scheduler | The code the LLM writes |
| `select` + prompt constructor | The LLM's decomposition logic expressed as code |

## What RLM gets right

RLM achieves the clean separation the model prescribes: bookkeeping happens in code (the REPL), semantic judgment happens in bounded LLM calls. The LLM doesn't track processed items in its conversation history or assemble prompts by remembering prior steps — the code does that. This avoids the [degraded scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) failure mode where bounded context is wasted on bookkeeping.

The key move is that the LLM *writes* the scheduler rather than *being* the scheduler. A standard agent loop consults the LLM at each `select` step: "given what you know, what should we do next?" RLM has the LLM emit the plan as code — `results = [recursive_llm("summarize", chunk) for chunk in chunks]` — so dispatch decisions are authored by the model but executed on a symbolic substrate. The orchestration logic is visible in one place, not spread across sequential tool calls.

In the model's terms: the LLM produces the `select` function for the sub-problem, and the REPL executes it symbolically. The important boundary is that recursion depth, call-stack progression, and intermediate state live in code even if some dispatching decisions originated in the model. This is more context-efficient than iterative consultation because intermediate results live first in Python variables and the REPL stack, and only re-enter later LLM calls when the scheduler explicitly selects them into a fresh prompt.

This makes RLM an important boundary case for [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md). That note is not really about hand-written `while` loops; it is about preserving an application-level control surface rather than burying progression inside a framework runtime. RLM shows a subtler point within the same picture: the decisive property is that the loop runs on an exact substrate outside the conversation. In RLM, the model may decide dispatch by writing code, but recursion depth is still maintained by the REPL rather than by the model's conversational state. The power comes from moving the loop out of chat, not from requiring a human-written imperative driver.

## Elegance without accumulation

RLM's architecture is genuinely elegant — it achieves the clean model naturally, without the engineering overhead of managed reentrancy or lifecycle hooks. The LLM writes a program, the program runs, results come back.

Some of RLM's further simplicity comes from an additional constraint, not from the clean model by itself: the REPL is restricted to pure computation with no side effects or persistent state. That makes the approval problem trivial because sandboxed code that only computes and returns values needs no gating. This is a separate property from scheduler placement. A system could externalise the loop into code while still facing approval and lifecycle complexity if that code were allowed to act on the world or persist artifacts.

But the scheduler is [ephemeral](./ephemeral-computation-prevents-accumulation.md). A brilliant decomposition strategy discovered for one query is gone before the next query arrives. In the framework this KB develops elsewhere — [deploy-time learning](./deploy-time-learning-the-missing-middle.md), [codification](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), [spec mining](./spec-mining-as-codification.md) — learning happens through the repo: generated artifacts enter version control, get tested, and become reusable infrastructure. RLM opts out of this entire mechanism by discarding its artifacts.

This is a genuine trade-off, not a deficiency. The repo-as-learning-substrate approach carries real costs (approval complexity, maintenance burden, the risk of [codifying vision features](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)). RLM avoids all of that. And it's possible that accumulation will come through other paths — improved model capabilities that make re-derivation cheap enough to not matter, or learned decomposition strategies encoded in weights rather than in repo artifacts. The bitter lesson suggests that if general-purpose models get good enough at writing schedulers on the fly, the accumulation advantage of versioned code may narrow.

This note does not try to map the full orchestration design space. That broader synthesis now lives in [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md). RLM matters there as one boundary case: the loop is externalised into code, but the resulting scheduler remains ephemeral rather than becoming persistent infrastructure.

---

Relevant Notes:

- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the select/call/absorb loop that RLM's code expresses
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrast: what happens when the LLM is the scheduler instead of writing it
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — explains: why RLM's scheduler code is discarded and what that costs
- [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — boundary case: RLM shows that externalising the loop matters more than whether a human or model authors the scheduler
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — context: situates RLM as one combination of scheduler placement and persistence rather than as one point on a single ladder
