---
description: RLM achieves the clean symbolic-scheduler model by having the LLM write the scheduler as code, but its ephemeral design opts out of deploy-time learning — the tension between architectural elegance and accumulation is a genuine open question
type: note
traits: []
areas: [computational-model]
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

The key move is that the LLM *writes* the scheduler rather than *being* the scheduler. A standard agent loop consults the LLM at each `select` step: "given what you know, what should we do next?" RLM has the LLM emit the full plan as code — `results = [recursive_llm("summarize", chunk) for chunk in chunks]` — expressing multiple iterations' worth of `select` decisions in one act. The orchestration logic is visible in one place, not spread across sequential tool calls.

In the model's terms: the LLM produces the `select` function for the entire sub-problem at once, and the REPL executes it symbolically. This is more context-efficient than iterative consultation because intermediate results flow through Python variables, never re-entering any LLM's context.

## Elegance without accumulation

RLM's architecture is genuinely elegant — it achieves the clean model naturally, without the engineering overhead of managed reentrancy, approval gates, or lifecycle hooks. The LLM writes a program, the program runs, results come back. Restricting the REPL to pure computation (no side effects, no persistent state) makes the approval problem trivial — sandboxed code needs no gating.

But the scheduler is [ephemeral](./ephemeral-computation-prevents-accumulation.md). A brilliant decomposition strategy discovered for one query is gone before the next query arrives. In the framework this KB develops elsewhere — [deploy-time learning](./deploy-time-learning-the-missing-middle.md), [codification](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), [spec mining](./spec-mining-as-codification.md) — learning happens through the repo: generated artifacts enter version control, get tested, and become reusable infrastructure. RLM opts out of this entire mechanism by discarding its artifacts.

This is a genuine trade-off, not a deficiency. The repo-as-learning-substrate approach carries real costs (approval complexity, maintenance burden, the risk of [codifying vision features](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)). RLM avoids all of that. And it's possible that accumulation will come through other paths — improved model capabilities that make re-derivation cheap enough to not matter, or learned decomposition strategies encoded in weights rather than in repo artifacts. The bitter lesson suggests that if general-purpose models get good enough at writing schedulers on the fly, the accumulation advantage of versioned code may narrow.

## The design space this reveals

RLM and standard agent loops represent two points in a design space:

- **Standard agent loop**: LLM *is* the scheduler, consulted at each step, bookkeeping in context. Flexible but context-inefficient.
- **RLM**: LLM *writes* the scheduler as ephemeral code. Context-efficient but non-accumulating.
- **Versioned scheduler code**: LLM writes scheduler logic that persists, is tested, and improves across runs. Context-efficient and accumulating, but requires the full software lifecycle (approval, versioning, maintenance).

The third point is what [codification](./deploy-time-learning-the-missing-middle.md) looks like applied to orchestration: the LLM's decomposition strategies become versioned infrastructure rather than being re-derived each time.

---

Relevant Notes:

- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the select/call/absorb loop that RLM's code expresses
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrast: what happens when the LLM is the scheduler instead of writing it
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — explains: why RLM's scheduler code is discarded and what that costs

Topics:

- [computational-model](./computational-model.md)
