---
description: Queries impose distinct access and transformation burdens that can vary separately even when retrieval and reasoning interact
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model]
---

# Access burden and transformation burden are distinct query dimensions

Question-answering systems face two different burdens: finding the right inputs and turning those inputs into the requested output. These burdens can vary separately even when they interact during execution. Treating query difficulty as one score obscures where the work remains and which mechanism could reduce it.

## The two burdens

**Access burden** is the difficulty of locating the inputs needed to answer a query. "Who is the HR head?" has low access burden when an org chart directly identifies the role, but high access burden when the answer must be reconstructed from email threads. Search, indexes, navigation, and link-following all reduce access burden.

**Transformation burden** is the difficulty of deriving the requested output from the available inputs. The HR question has near-zero transformation burden once the answer is found. "What were last year's expenses?" can have low access burden when the records are in a known table, yet still require selection and aggregation. "Why did expenses increase?" requires causal reasoning even after the relevant records are available.

These examples establish separability, not isolation. Either burden can be high while the other is low, so reducing one does not necessarily reduce the other.

The burdens nevertheless interact during execution. A transformation can expose missing evidence and trigger another access step. Conversely, retrieval may return raw evidence or a precomputed result, changing the transformation that remains. Access and transformation can therefore alternate as stages of a pipeline while remaining distinct diagnostic dimensions.

## Transformation routing depends on specification

Distinguishing transformation burden enables a second routing question: is the next operation specified well enough for mechanical execution? This separates three responsibilities that the original query may combine: specifying the intended operation, executing it, and validating that its result answers the query.

**Formally specified transformations** have explicit procedures and acceptance conditions. Filtering, counting, aggregating, sorting, joining, or sampling can be executed by a symbolic substrate once predicates, numeric rules, tie handling, distributions, and other semantics are fixed. A formally specified procedure need not produce one literal output: a sampling operation can permit multiple results while remaining fully defined.

**Semantic transformations** still depend on interpretation, relevance judgment, explanation, synthesis, or conjecture that the system has not reduced to a formal procedure. The causal expense question remains semantic when the query and evidence do not specify how to infer or rank plausible causes.

When a trustworthy symbolic implementation exists, it should execute a fully specified operation. An LLM may still help specify the operation, decompose the query, or validate whether the formal result answers the user's intent. Symbolic execution guarantees neither a correct specification nor a correct implementation. It confines model uncertainty to the stages that require interpretation instead of reintroducing it into mechanical execution. The [scheduler-LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) argument supports this preference on reliability and cost grounds; deciding whether an operation is fully specified remains a matter of judgment.

## Routing is iterative

Because transformation can expose missing inputs, routing is a loop rather than a fixed two-stage pipeline. The [bounded-context orchestration model](./bounded-context-orchestration-model.md) suggests this sequence:

1. Acquire the inputs currently required.
2. Identify the next transformation and specify its acceptance conditions as far as the evidence permits.
3. Execute fully specified operations symbolically; route unresolved judgment to a bounded semantic call; split mixed work across both.
4. Validate the result against the original query. If validation changes the required evidence or operation, return to the relevant step.

Text-to-SQL, filter construction, and API-call assembly fit this pattern. A model translates natural language into an operation, symbolic code executes it, and validation checks whether the operation represented the intended request.

## Open questions

- Can access burden and transformation burden be estimated from a query before execution, or only recognised after the fact?
- What taxonomy within transformation burden is more useful than a symbolic/semantic binary?
- Where should a mixed query hand off between formal execution and semantic judgment?
- How can a system detect formally specified transformations that natural-language phrasing makes appear semantic?

---

Relevant Notes:

- [charting the knowledge-access problem beyond RAG](./charting-the-knowledge-access-problem-beyond-rag.md) — this distinction emerged from its broader map of knowledge access
- [soft degradation often binds before the hard cap when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — its account of task-dependent context costs bounds how both burdens appear within a model call
