---
description: Worst-case lower bound for opaque retrieval — without a pre-built pointer layer, exact discovery of all relevant items requires linear semantic inspection
type: structured-claim
traits: []
tags: [computational-model, context-engineering]
status: seedling
---

# Exact retrieval over semantically opaque items requires linear inspection

In the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md), symbolic code can store, sort, and batch arbitrary state, but only bounded LLM calls can produce new semantic judgments. That yields a simple worst-case lower bound. If a collection of `N` items is **semantically opaque** to symbolic code — no title, description, embedding, metadata field, graph edge, or other pre-built pointer is correlated with relevance — then an orchestrator that must return the **complete set** of relevant items cannot asymptotically beat semantic inspection of the items themselves. Let `m` be the maximum number of opaque items one bounded call can judge for relevance. Then any correct algorithm needs `Omega(N)` total inspections, `Omega(N/m)` sequential calls, and with parallel width `p`, `Omega(N/(mp))` rounds.

## Evidence

- The orchestration model separates exact symbolic state from bounded semantic calls. File listing, sorting, deduplication, batching, and control flow are symbolic; relevance judgments enter `K` only through `call(P)`.
- Existing pointer notes already identify the escape hatch. [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) defines descriptions, abstracts, reranker scores, and link phrases as lower-resolution representations that let the scheduler decide what to load before full inspection. Those are precisely the kinds of pre-built information this lower bound excludes.
- The claim is about **exact worst-case retrieval**. The task is: given `N` candidate items, output exactly the subset relevant to a query or objective. Approximate recall, top-`k`, or distributional assumptions are out of scope.
- The bound can be parameterized by per-call capacity. If one bounded call can semantically inspect at most `m` opaque items, then each call contributes at most `m` new relevance facts.

## Reasoning

Fix any algorithm in the [select/call class](../../notes/any-symbolic-program-with-bounded-calls-is-a-select-call-program.md). Suppose it halts after semantically inspecting fewer than `N` items. Then there exists at least one uninspected item `x`.

Because `x` is semantically opaque to symbolic code, the scheduler has no relevance-correlated information about `x` beyond its bare identity as an uninspected item. Therefore the algorithm's entire execution trace up to halt is compatible with at least two worlds:

- `W0`, where `x` is not relevant
- `W1`, where `x` is relevant

All other inspected items and all prior call results are identical in the two worlds. Since `x` was never semantically inspected, nothing in the symbolic state distinguishes `W0` from `W1`.

So the algorithm must produce the same output in both worlds. But exact retrieval requires different outputs: `x` must be absent in `W0` and present in `W1`. The algorithm is therefore wrong in at least one of the two worlds. Contradiction.

So every correct worst-case algorithm must semantically inspect every item at least once. That yields `Omega(N)` total semantic work. If each call can inspect at most `m` items, at least `ceil(N/m)` calls are required, hence `Omega(N/m)` sequential call complexity. If at most `p` calls run in parallel per round, each round inspects at most `mp` items, so at least `ceil(N/(mp))` rounds are required, hence `Omega(N/(mp))` round complexity.

The practical consequence is narrow but important. Orchestration can change **how** the semantic work is scheduled — batching, framing, decomposition, caching, arbitration, parallel fan-out — but not eliminate the need for semantic inspection itself. To beat linear scan asymptotically, the system must introduce a pointer layer that is already correlated with relevance: descriptions, summaries, typed metadata, embeddings, graph structure, learned indexes, or prior semantic labels. Those artifacts are not free wins from orchestration; they are accumulated semantic work stored in symbolic form.

## Caveats

- The opacity assumption is load-bearing. If filenames, frontmatter, links, embeddings, or any other symbolic features are correlated with relevance, the scheduler can prune without inspecting every full item, and the lower bound no longer applies.
- The result is worst-case and exact. Practical systems often accept approximate recall, probabilistic guarantees, or domain-specific priors; those weaker objectives can beat linear scan on average.
- A compressed representation does not refute the bound if it was itself produced by semantic work. A summary, abstract, or embedding index is precisely the pre-built pointer layer that changes the problem.
- The theorem only lower-bounds retrieval. Once the relevant set is found, synthesis or aggregation may add further call costs.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — foundation: the lower bound applies inside the select/call architecture because new relevance facts enter only through bounded semantic calls
- [any symbolic program with bounded calls is a select/call program](../../notes/any-symbolic-program-with-bounded-calls-is-a-select-call-program.md) — scope: lifts the lower bound from one orchestration style to the full class of symbolic programs with bounded LLM calls
- [pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — boundary: descriptions, abstracts, rerankers, and link phrases are exactly the pointer layer that invalidates semantic opacity
- [two context boundaries govern collection operations](../../notes/two-context-boundaries-govern-collection-operations.md) — consequence: index-level operation only exists because titles and descriptions provide a cheaper pointer layer than full semantic reading
- [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — consequence: the result identifies one place where context cost is irreducible unless semantic work is prepaid into an index
- [information value is observer-relative](../../notes/information-value-is-observer-relative.md) — mechanism: whether an item is opaque depends on what structure the observer can extract without a semantic read
- [semantic sub-goals that exceed one context window become scheduling problems](../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) — instance: large-scale relevance filtering is one semantic sub-goal whose cost cannot be avoided by orchestration alone
