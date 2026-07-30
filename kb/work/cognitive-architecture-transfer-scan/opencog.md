# OpenCog: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high on the longstanding design, medium on current project boundaries

## Remembered model

OpenCog is a broad AGI framework organized historically around AtomSpace, a typed hypergraph of Atoms representing concepts, predicates, relations, procedures, and other structures. Different cognitive processes operate over that shared representation: pattern matching, rule-based and probabilistic inference such as PLN, attentional allocation such as ECAN, evolutionary program learning such as MOSES, language components, and action systems. The hoped-for architectural property is cognitive synergy—specialized processes improve one another by exchanging structures through a common substrate.

Current OpenCog Hyperon and MeTTa may alter this picture substantially; this scan should not be read as current project documentation.

## Provisional ontology

- **Atom:** a typed node or link in a shared knowledge representation.
- **Hypergraph:** the common substrate connecting nested relational structures.
- **Truth value:** epistemic support or confidence associated with a proposition.
- **Attention value:** resource-allocation priority, separate from truth.
- **Pattern/query:** a structure matched against the graph.
- **Inference rule:** a transformation deriving or revising structures and values.
- **Procedure/schema:** executable knowledge represented within or referenced by the graph.
- **Cognitive process:** a specialized algorithm that reads and writes shared structures.
- **Cognitive synergy:** complementary processes making one another more effective through exchange.

The cleanest transfer is the separation among **what is believed, what is attended, what is useful, and what is behaviorally binding**. These are often collapsed into one rank in agent-memory systems.

## Transfer candidates

- **`OPENCOG-1` — maintain orthogonal artifact signals.** Epistemic confidence, retrieval priority, task utility, freshness, and [behavioral authority](../../notes/definitions/behavioral-authority.md) should be separately inspectable even if a selector later combines them.
- **`OPENCOG-2` — define operations over the graph, not only graph storage.** A knowledge graph earns architectural value through queries, transformations, validation, activation, and maintenance workflows. Nodes and edges alone are inert inventory.
- **`OPENCOG-3` — evaluate cognitive synergy as reduced translation cost.** Search, review, inference, and planning sharing a substrate is valuable only if one process's output becomes another's usable input with less loss or duplication.
- **`OPENCOG-4` — allow several reasoning regimes over one artifact corpus.** Deterministic validators, lexical search, semantic judgment, and probabilistic ranking can contribute without pretending to have identical semantics.
- **`OPENCOG-5` — resist universal representation until interoperability pays.** Use adapters and typed views before forcing prose, code, evidence, workflow state, and uncertainty into one maximal schema.

## Method worth borrowing

Test claimed synergy with cross-process tasks. Compare a shared-substrate workflow against isolated components plus explicit translations. Measure not only outcome quality but information loss, duplicated state, stale copies, debugging visibility, and the cost of adding a new cognitive process. "Unified" should predict observable coordination gains.

## Non-transfer and failure modes

- A universal graph can become an ontology project that delays useful operations.
- Shared representation increases coupling and blast radius when semantics change.
- Numeric truth or attention values can create false precision and hide source disagreement.
- The longstanding OpenCog module inventory may not describe Hyperon's current commitments.
- Cognitive synergy is a hypothesis requiring comparative evidence, not a benefit guaranteed by co-location.

## Grounding questions

1. Which distinctions among truth, attention, utility, and execution are canonical in the relevant OpenCog version?
2. What evidence demonstrates synergy among named components rather than theoretical compatibility?
3. How do AtomSpace/Atomese relate to Hyperon/MeTTa now?
4. Which mechanisms have complete, inspectable end-to-end demonstrations?
