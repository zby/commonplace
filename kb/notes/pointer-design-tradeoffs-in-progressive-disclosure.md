---
description: Design tradeoffs for progressive disclosure pointers — context-specificity vs precomputation cost vs reliability; fixed pointers (descriptions, abstracts) trade specificity for reliability and cheap reads, query-time pointers (re-rankers) trade cost for specificity, crafted pointers (link phrases) achieve highest density but depend on authoring discipline
type: note
traits: []
tags: [links, computational-model]
status: seedling
---

# Pointer design tradeoffs in progressive disclosure

A **pointer** is any lower-resolution representation that helps decide whether to load a knowledge item — a description, an abstract, a search result snippet, a re-ranker score, even a title. The concept is substrate-independent: a **link** (markdown reference with context phrase) is a pointer in our substrate; OpenViking's `.abstract.md` is a pointer in their virtual filesystem; a re-ranker output is a pointer in a retrieval pipeline.

Progressive disclosure works by giving agents pointers at increasing resolution — scan cheap ones first, load expensive content only when needed. But not all pointers are alike. They vary on three axes: **context-specificity**, **cost**, and **reliability**.

## Context-specificity: when does the pointer learn about the consumer?

The most obvious axis. A pointer can know nothing about why the consumer is looking (a fixed description), something about the query (a re-ranker score), or everything about the surrounding argument (a crafted link phrase).

**Fixed at write time.** Descriptions, OpenViking's L0 abstracts. One distillation per note, amortized over all reads. The same summary regardless of who's reading or why — context-free. This is enough for global operations (search, comparative reading, index building) where there's no surrounding argument to leverage.

**Produced at query time.** Search result snippets, retrieval scores, re-rankers, query-specific summaries. Some are cheap retrieval artifacts; some require inference. The common property is that they are produced for this query rather than stored ahead of time. That makes them more query-specific than fixed abstracts: "how does this system handle memory dedup?" can produce a ranking or snippet that fixed abstracts cannot. Cost and reliability vary by mechanism.

**Crafted at link-authoring time.** Link phrases in our system. The same note gets a different characterization at every link site:

- From a distillation note: `[constraining](./constraining.md) — orthogonal to distillation; narrows interpretation rather than compressing`
- From a codification note: `[constraining](./constraining.md) — codification is the far end of constraining`
- From an architecture note: `[constraining](./constraining.md) — narrows the set of valid interpretations an agent can make`

Each phrase leverages the surrounding argument the agent already has loaded — not just "what is this item" but "why does it matter *here*." This is the densest pointer type, but it requires human judgment and only exists where someone authored a link.

## Reliability: the axis you forget until it breaks

If context-specificity were the only axis, the answer would be simple: compute the most specific pointer you can afford. As inference gets cheaper, query-time computation replaces fixed pointers. Problem solved.

But [agent statelessness](./agent-statelessness-makes-routing-architectural-not-learned.md) complicates this. Agents start cold every session. Routing is permanent architecture, not scaffolding they outgrow. And the [degradation cliff](./agent-statelessness-makes-routing-architectural-not-learned.md) is unforgiving: when routing fails, the agent doesn't slow down — it falls into generic LLM behavior, confidently executing without the KB's methodology.

Fixed pointers are reliable. They're there every time, same content, no query-time dependency. A query-time pipeline introduces new failure modes: poor retrieval, poor reranking, or poor inference can send the agent off the cliff. Crafted link phrases introduce another: if the author skipped the context phrase, the pointer is simply absent.

This means the three axes pull in different directions:

| Pointer type | Specificity | Cost | Reliability |
|-------------|------------|------|-------------|
| Fixed (write-time) | Low — context-free | Cheapest per read | Highest — always present, deterministic |
| Query-time | Medium — query-specific | Per-query retrieval/inference cost | Medium — depends on retrieval/inference quality |
| Crafted (authoring-time) | Highest — argument-specific | Human judgment | Variable — depends on discipline |

No single type wins all three. A system needs a mix.

## What this looks like in practice

Comparing OpenViking's tiers with ours makes the tradeoffs concrete:

| Role | OpenViking | Commonplace |
|------|-----------|-------------|
| Identity pointer | URI/name (~5-10 tok) | Title-as-claim (~10 tok) |
| Fixed filter | L0 abstract (~100 tok) | Description (~50 tok) |
| Intermediate overview | L1 overview (~2000 tok) | *No equivalent* |
| Relation-specific pointer | `.relations.json` reason string (weaker, relation-level) | Link phrase (~20 tok), varies per link site |
| Full content | L2 original files | Note body |

Each system has a tier the other emphasizes. OpenViking invests in L1 — a 2000-token overview between the fixed filter and full content, useful for scoping before committing to a full read. We invest in crafted link phrases — 20-token characterizations that tell the agent why a target matters in the current argument. OpenViking does have relation annotations via `.relations.json` reason strings, but its main retrieval path still centers fixed pointers (`uri` + `abstract`) rather than per-link argumentative characterizations. Neither system uses query-time computation for navigation pointers yet.

## Design implications

| Property | Fixed | Query-time | Crafted |
|----------|-------|-----------|---------|
| Guaranteed to exist | Yes | Per-query | Authoring discipline |
| Quality ceiling | Generic | Query-specific | Argument-specific |
| Scales to global ops | Yes | Yes (at cost) | No |
| Failure mode | Stale if source changes | Bad retrieval/rerank/inference → cliff | Absent or weak |

The practical path: invest in crafted link phrases for local navigation (the common agent case), use `/validate` to pressure notes toward reliable fixed descriptions for global operations, and watch query-time computation as inference costs drop — but treat it as supplementary to architectural routing, not a replacement.

---

Relevant Notes:

- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds: the navigation decision is what pointers optimize for; link phrases are the most context-specific pointer type for that decision
- [agent statelessness makes routing architectural, not learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — grounds: the reliability axis; fixed pointers are architectural routing that stateless agents depend on, and query-time computation introduces the degradation cliff
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the cost spectrum is a context efficiency trade-off
- [distillation](./distillation.md) — exemplifies: each pointer type is a distillation at different cost/quality/reliability trade-offs
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: the tier structure defines the resolution gradient; query-time computation could fill gaps dynamically
- [OpenViking](./related-systems/openviking.md) — contrasts: their L0/L1/L2 emphasizes fixed pointers, with weaker relation-level reason strings rather than crafted per-link argument pointers; the comparison crystallized this note
