---
description: Separates the system-relative cost of finding required inputs from producing an answer, so query systems can diagnose which work remains as retrieval and reasoning interact
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model]
---

# Access burden and transformation burden are distinct query dimensions

Question-answering systems face two different burdens: finding the right inputs and turning those inputs into the requested output. These burdens can vary separately even when they interact during execution. When either burden is material, treating query difficulty as one score obscures where the work remains and which mechanism could reduce it.

Neither burden is intrinsic to the query text. For a particular system at a particular moment, their values depend on which evidence and intermediate results the execution state already holds; how the information is represented; which artifacts, such as indexes or precomputed results, are available; which operators, such as search, SQL, code, or model inference, can act on it; and which outputs the answer semantics accept. A materialized answer can make transformation trivial; a poor representation can make the same underlying information difficult to access or transform. The distinction therefore compares burdens within a specified query-system situation rather than assigning a permanent score to a query.

## The two burdens

**Access burden** is the difficulty of locating the inputs needed to answer a query. "Who is the HR head?" has low access burden when an org chart directly identifies the role, but high access burden when the answer must be reconstructed from email threads. Search, indexes, navigation, and link-following all reduce access burden.

**Transformation burden** is the difficulty of deriving the requested output from the available inputs. The HR question has near-zero transformation burden once the answer is found. "What were last year's expenses?" can have low access burden when the records are in a known table, yet still require selection and aggregation. "Why did expenses increase?" requires causal reasoning even after the relevant records are available.

These examples establish separability, not isolation. Either burden can be high while the other is low, so reducing one does not necessarily reduce the other.

The distinction adds little to a direct lookup when the needed input is already explicit and returning it satisfies the answer semantics: both burdens are negligible. It becomes diagnostic when at least one burden is material.

The burdens nevertheless interact during execution. A transformation can expose missing evidence and trigger another access step. Conversely, retrieval may return raw evidence or a precomputed result, changing the transformation that remains. Access and transformation can therefore alternate as stages of a pipeline while remaining distinct diagnostic dimensions.

## A routing corollary

Distinguishing transformation burden permits a narrower routing question: is the next operation specified well enough for mechanical execution? A transformation is fully specified when its procedure and acceptance conditions fix which outputs are valid. Filtering, counting, aggregating, sorting, joining, and sampling can meet this condition once their predicates, numeric rules, tie handling, distributions, and other semantics are fixed. A sampling procedure may permit several literal results while remaining fully specified.

Unresolved interpretation, relevance judgment, explanation, synthesis, or conjecture remains semantic work. When a trustworthy symbolic implementation exists, it should execute the fully specified portion. A bounded semantic call—a model call limited to the context and unresolved judgment needed for one step—can specify or decompose the remaining work. Checking whether the result answers the query is not inherently a third responsibility distinct from specification: it is mechanical when the acceptance conditions settle the check and semantic when they do not.

A deterministically decoded model that has been exhaustively verified for a finite input domain can also be trustworthy for one fixed operation. This local exception defeats a categorical ban on model execution, but it does not erase the distinction between access and transformation burden.

Execution changes the state against which both burdens are measured, so routing can alternate: acquire the inputs needed now, specify and execute one transformation, compare its result with the answer semantics, and repeat if the result exposes missing evidence or unresolved judgment. The [scheduler-LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) argument supplies the reliability-and-cost reason for the symbolic preference, while the [bounded-context orchestration model](./bounded-context-orchestration-model.md) supplies this one-step loop shape. This is a consequence of the two-burden diagnosis, not a second classification of query difficulty.

## Open questions

- Can access burden and transformation burden be estimated from the query plus its system-relative variables before execution, or only recognised after the fact?
- What taxonomy within transformation burden is more useful than a symbolic/semantic binary?
- Where should a mixed query hand off between formal execution and semantic judgment?
- How can a system detect formally specified transformations that natural-language phrasing makes appear semantic?

---

Relevant Notes:

- [charting the knowledge-access problem beyond RAG](./knowledge-access-architecture-must-be-evaluated-end-to-end.md) — this distinction emerged from its broader map of knowledge access
- [soft degradation often binds before the hard cap when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — its account of task-dependent context costs bounds how both burdens appear within a model call
