---
description: Queries have two independent difficulty axes — finding inputs (access) and producing the answer (transformation) — conflating them misroutes symbolic transformations through semantic processing
type: note
traits: []
tags: [foundations, computational-model]
status: seedling
---

# Access burden and transformation burden are independent query dimensions

Systems that answer questions face two distinct problems: finding the right inputs, and turning those inputs into the requested output. These are independent axes of difficulty, not stages of a single pipeline. Conflating them produces architectural mistakes — most consequentially, routing symbolic transformations through semantic processing.

## The two axes

**Access burden** is the difficulty of locating the right inputs in the first place. "Who is the HR head?" has low access burden if there is an org chart, high access burden if the answer is buried across email threads. The access problem is what retrieval systems address: search, indexes, navigation, link-following.

**Transformation burden** is the difficulty of producing the requested output once the inputs are in hand. "Who is the HR head?" has near-zero transformation burden — the answer is the retrieved value. "What were last year's expenses?" may have low access burden (the records are in a known table) but real transformation burden (select the right records and sum them). "Why did expenses increase?" has high transformation burden even after the records are found — the answer requires causal reasoning across multiple data points.

These axes vary independently, and treating "how hard is this query?" as a single dimension hides that structure. A system that retrieves expense records perfectly still cannot sum them reliably through semantic processing — that failure is in the transformation, not the access. A code search that lands on the right module still cannot answer "is this code thread-safe?" without reasoning over concurrency patterns — again, access succeeded but transformation is where the difficulty lies. Better retrieval cannot fix a transformation problem, and more powerful reasoning cannot fix an access problem. Conflating the two leads to systems designed as if improving one axis automatically improves the other.

## Corollary: symbolic transformations routed through semantic processing are a category error

Once transformation burden is visible as its own axis, the most consequential question about it is whether the work is symbolic or semantic.

**Symbolic transformations** — filtering, counting, aggregating, sorting, joining, deriving — have a unique correct answer given the inputs. "What were last year's expenses?" requires selecting records by date range and summing amounts. This is a database query wearing natural language clothes. The transformation is mechanically deterministic: given the same inputs, every correct execution produces the same output.

**Semantic transformations** — explaining, synthesising, comparing, conjecturing — do not have unique correct answers. "Why did expenses increase?" requires causal reasoning, relevance judgment, and narrative construction. Different valid answers exist.

Routing a symbolic transformation through an LLM is a category error. It trades deterministic correctness for stochastic approximation, spending context and inference budget on work that a symbolic substrate handles perfectly. The [scheduler-LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) argument gives the formal reason: symbolic substrates eliminate underspecification, indeterminism, and bias simultaneously — properties an LLM cannot match for bookkeeping operations.

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) states the resulting design principle: symbolic steps outside context, bounded agent calls for semantic work. Some queries should stay symbolic end-to-end — access via structured query, transformation via aggregation. Others need a symbolic retrieval stage that prepares inputs for a bounded semantic call. Which queries need an LLM at all for the transformation step is the architectural question this decomposition reveals.

## The common architecture this implies

This decomposition implies a two-stage routing pattern:

1. **Classify the transformation**: is the post-retrieval work symbolic, semantic, or a mix?
2. **Route accordingly**: symbolic transformations go through structured queries and computation. Semantic transformations go through LLM calls. Mixed queries use symbolic pre-processing to prepare inputs for a bounded semantic call.

The LLM's role in a symbolic query is limited to the front end: translating natural language into the right symbolic operation (text-to-SQL, filter construction, API call assembly). Once the operation is specified, execution should be symbolic. This is a well-known pattern (text-to-SQL, tool use), but the two-axis framing explains *why* it works: it routes each axis through the substrate that handles it best.

## Open questions

- Can access burden and transformation burden be estimated from a query before execution, or only recognised after the fact?
- What is the right taxonomy within transformation burden beyond symbolic/semantic? Derivation, aggregation, synthesis, conjecture — are these cleanly separable?
- Where does the boundary fall for mixed queries? "Which code changes most likely caused this regression?" is partly symbolic (diff, bisect, filter) and partly semantic (judge causation).
- How should a system handle queries that look semantic but are actually symbolic? Natural language disguises the transformation type.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds: states the symbolic-outside-semantic-inside principle this note applies to query routing
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: the formal argument for why symbolic work should stay on symbolic substrates
- [charting the knowledge-access problem beyond RAG](./charting-the-knowledge-access-problem-beyond-rag.md) — extracted from: the transformation-burden and symbolic/semantic sections of this brainstorming note
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — clarifies: access and transformation consume context differently, reinforcing their independence
