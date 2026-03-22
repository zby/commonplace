---
description: RLM packs orchestration over sub-agents into the tool-loop model by having the model write orchestrators in a REPL — elegant but ephemeral because the orchestrators are discarded after each run
type: note
traits: []
tags: [computational-model]
status: seedling
---

# RLM has the model write ephemeral orchestrators over sub-agents

Recursive Language Models (RLMs) have the LLM write and execute code in a REPL, with a `recursive_llm(query, context)` primitive that spawns fresh LLM calls. The pattern maps directly onto the [symbolic scheduler model](./bounded-context-orchestration-model.md):

| Model component | RLM implementation |
|---|---|
| Symbolic state K | Python REPL namespace (variables) |
| Bounded LLM call | `recursive_llm(query, context)` |
| Inner scheduler | The code the LLM writes |
| `select` + prompt constructor | The LLM's decomposition logic expressed as code |

## What RLM gets right

RLM has two layers of symbolic orchestration. The outer layer is a traditional tool loop: it calls the model, the model requests code execution, the loop runs it in the REPL and feeds the result back. Inside the REPL, the model writes its own orchestrators — symbolic compositions of [agents](./agent-is-a-tool-loop.md) via `recursive_llm()`.

The key move is that the model *writes* the orchestrator rather than *being* it. A standard tool loop consults the model at each step: "what should we do next?" RLM has the model emit the plan as code — `results = [recursive_llm("summarize", chunk) for chunk in chunks]` — so dispatch decisions are authored by the model but executed on a symbolic substrate. Bookkeeping for the inner orchestration lives in Python variables and the REPL stack, not in the conversation. This avoids the [degraded scheduler](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) failure mode where bounded context is wasted on bookkeeping.

The model-authored orchestrators are structurally the same thing a programmer would write by hand — exactly the symbolic orchestration over sub-agents that the [tool loop](./tool-loop-index.md) argument calls for. The elegance of RLM is how it packs this into the tool-loop model: the REPL tool gives the model a substrate for writing orchestrators without anyone having to write reentrant framework code.

## Ephemerality

The orchestrators are [ephemeral](./ephemeral-computation-prevents-accumulation.md). A brilliant decomposition strategy discovered for one query is gone before the next query arrives. In the framework this KB develops elsewhere — [deploy-time learning](./deploy-time-learning-the-missing-middle.md), [codification](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), [spec mining](./spec-mining-as-codification.md) — learning happens through the repo: generated artifacts enter version control, get tested, and become reusable infrastructure. RLM opts out of this entire mechanism by discarding its artifacts.

This is a genuine trade-off, not a deficiency. The repo-as-learning-substrate approach carries real costs (approval complexity, maintenance burden, the risk of [codifying vision features](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)). RLM avoids much of that burden. If the REPL is restricted to pure computation with no side effects, the approval problem becomes much simpler because the generated code is not directly changing the world; the remaining concerns are mostly about cost, resource use, and output quality rather than side effects. And it's possible that accumulation will come through other paths: improved model capabilities that make re-derivation cheap, decomposition strategies learned in weights rather than repo artifacts, or mining the ephemeral code from execution logs — an out-of-band process could gather the generated orchestrators together with their prompts and results, and distill recurring patterns into reusable knowledge.

---

Relevant Notes:

- [@neural_avb: Recursive Language Models — what finally gave me the 'aha' moment](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment-2035040781074145412.md) — grounds: concrete practitioner walkthrough of the REPL mechanism, symbolic variable return, and scaffold-level truncation that this note abstracts ([ingest](../sources/recursive-language-models-what-finally-gave-me-the-aha-moment-2035040781074145412.ingest.md))
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the select/call/absorb loop that RLM's code expresses
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — contrast: what happens when the LLM is the scheduler instead of writing it
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — explains: why RLM's scheduler code is discarded and what that costs
- [tool loop](./tool-loop-index.md) — boundary case: RLM implements the full solution (symbolic orchestration over sub-agents) by having the model author it in a REPL tool
- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — context: situates RLM as one combination of scheduler placement and persistence rather than as one point on a single ladder
