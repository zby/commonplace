---
description: "Compares fixed, query-time, and crafted retrieval pointers across specificity, cost, availability, accuracy, and authoring dependence"
type: types/note.md
traits: [has-external-sources]
tags: [links, context-engineering]
---

# Pointer design tradeoffs in progressive disclosure

A **pointer** is any lower-resolution representation that helps decide whether to load a knowledge item — a description, an abstract, a search result snippet, a re-ranker score, even a title. The concept is substrate-independent: a **link** (markdown reference with context phrase) is a pointer in our substrate; OpenViking's `.abstract.md` is a pointer in their virtual filesystem; a re-ranker output is a pointer in a retrieval pipeline.

Progressive disclosure works by giving agents pointers at increasing resolution — scan cheap ones first, load expensive content only when needed. But not all pointers are alike. They vary on four axes: **context-specificity**, **cost**, **availability**, and **accuracy**.

## Context-specificity: when does the pointer learn about the consumer?

The most obvious axis. A pointer can know nothing about why the consumer is looking (a fixed description), something about the query (a re-ranker score), or everything about the surrounding argument (a crafted link phrase).

**Fixed at write time.** Descriptions, OpenViking's L0 abstracts. One precomputed summary per note, amortized over all reads. The same summary regardless of who's reading or why — context-free. This is enough for global operations (search, comparative reading, index building) where there's no surrounding argument to leverage.

**Produced at query time.** Search result snippets, retrieval scores, re-rankers, query-specific summaries. Some are cheap retrieval artifacts; some require inference. The common property is that they are produced for this query rather than stored ahead of time. That makes them more query-specific than fixed abstracts: "how does this system handle memory dedup?" can produce a ranking or snippet that fixed abstracts cannot. Cost and reliability vary by mechanism.

Tombros and Sanderson supply a bounded human-IR instance of this branch. They compared query-biased summaries with static title-plus-leading-lines summaries and found significantly better relevance judgments with the query-biased condition. Their same-length follow-up attributed the performance difference to query bias rather than the amount of displayed text. [The experiment](../sources/tombros-sanderson-query-biased-summaries.ingest.md) supports the possibility that query-conditioned pointer content can improve human relevance judgment. It does not establish LLM-agent performance, the cost of producing such pointers, or this note's three-way pointer taxonomy.

**Crafted at link-authoring time.** Link phrases in our system. The same note gets a different characterization at every link site:

- From a compression note: `[constraining](./definitions/constraining.md) — orthogonal to compression; narrows interpretation rather than shortening`
- From a codification note: `[constraining](./definitions/constraining.md) — codification is the far end of constraining`
- From an architecture note: `[constraining](./definitions/constraining.md) — narrows the set of valid interpretations an agent can make`

Each phrase leverages the surrounding argument the agent already has loaded — not just "what is this item" but "why does it matter *here*." This is the densest pointer type, but it requires human judgment and only exists where someone authored a link.

## Availability and accuracy fail differently

If context-specificity were the only axis, the answer would be simple: compute the most specific pointer you can afford. As inference gets cheaper, query-time computation replaces fixed pointers. Problem solved.

A query-specific snippet does no work if the search service is down. That removes one route, not necessarily the document: even [an agent starting without memory of an earlier lookup](./agent-statelessness-makes-routing-architectural-not-learned.md) may find it through an index or a link. To test whether the missing route matters, start with the task description and check whether the agent still finds the document before it acts.

Fixed pointers are highly available. They are retained with the artifact, have the same content on every read, and need no query-time pipeline. That does not make them accurate: a fixed description can remain confidently available after its target changes. Query-time pointers have the opposite exposure. Their existence depends on retrieval or inference running, and their accuracy depends on those mechanisms selecting and characterizing the target well. Crafted link phrases are available only where an author supplied them; when present, their accuracy still depends on the author's judgment and on later target drift.

The four axes therefore pull in different directions:

| Pointer type | Specificity | Cost | Availability | Accuracy |
|-------------|------------|------|--------------|----------|
| Fixed (write-time) | Low — context-free | Cheapest per read | High — retained with the artifact | Variable — generic and can go stale |
| Query-time | Medium — query-specific | Per-query retrieval/inference cost | Conditional — pipeline must run | Variable — depends on retrieval and inference quality |
| Crafted (authoring-time) | Highest — argument-specific | Human judgment | Sparse — only at authored link sites | Variable — depends on judgment and target drift |

No single type wins all four. A system needs a mix.

## One system can mix pointer types

OpenViking illustrates why the categories are not competing architectures. Its [historical review](../agent-memory-systems/reviews/openviking.md) records generated L0 abstracts and L1 overviews over L2 content. Those are fixed views once retained. In the [current analysis of session search](../agentic-system-analyses/retained/volcengine--openviking/runtime.md#rt-rte-session-search), the retriever searches the vector index for each query and can rerank candidate abstracts. It does not descend the directory tree. Direct `find` skips model reranking. Those are query-time pointers under this note's definition.

Commonplace's titles and descriptions illustrate fixed pointers, while its link phrases illustrate crafted pointers. The comparison establishes that a system can combine categories at different stages. It does not establish which mix produces better navigation outcomes, nor does the OpenViking review establish a per-link prose equivalent to Commonplace's context phrases.

## Design implications

| Property | Fixed | Query-time | Crafted |
|----------|-------|-----------|---------|
| Availability | Retained with artifact | Only if pipeline runs | Only at authored link sites |
| Quality ceiling | Generic | Query-specific | Argument-specific |
| Scales to global ops | Yes | Yes (at cost) | No |
| Failure mode | Stale if source changes | Missing result or misleading ranking | Absent or weak |

For local navigation, put the reason to follow a link where the reader encounters it. For search across the collection, check that fixed descriptions exist and still describe their targets. If a task depends on a query-time pointer, test the fallback with that service unavailable.

---

Relevant Notes:

- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — grounds: navigation repeatedly presents follow-or-skip decisions that pointers help an agent make
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the cost spectrum is a context efficiency trade-off
- [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — exemplifies: fixed and query-time pointers instantiate its broader split between a precomputed fast path and live work for the current case
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: the tier structure defines the resolution gradient; query-time computation could fill gaps dynamically
- [Advantages of Query Biased Summaries in Information Retrieval](../sources/tombros-sanderson-query-biased-summaries.ingest.md) — evidenced-by: query-biased summaries improved human relevance judgments against a static-summary baseline, without establishing the agent-facing taxonomy or cost model
