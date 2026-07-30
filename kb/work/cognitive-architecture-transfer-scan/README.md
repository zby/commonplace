# Workshop: Cognitive Architecture Transfer Scan

## Question

What concepts, distinctions, mechanisms, and research methods from cognitive architectures might improve Commonplace's account of agent memory, context engineering, learning, orchestration, and knowledge-base operation?

The immediate purpose is breadth-first conjecture generation. The architecture names come from the Wikipedia [comparison of cognitive architectures](https://en.wikipedia.org/wiki/Comparison_of_cognitive_architectures) that triggered the discussion. Every listed item gets its own scan, including entries that may turn out not to be cognitive architectures at the same level of analysis.

## Epistemic boundary

This pass is deliberately **memory-first and source-ungrounded**. It records what appears worth investigating before paying the cost of reading original papers, manuals, or code. Statements under "Remembered model" are recollections, not established descriptions. Transfer candidates are conjectures, not recommendations.

Each scan carries a recall-confidence label:

- **High** — the main components and mechanisms are stable enough in memory to generate fairly specific questions, but details still require checking.
- **Medium** — the broad orientation is remembered, while terminology or component boundaries may be wrong.
- **Low** — only a theme, reputation, or name is remembered; the document mainly records questions and guards against invented detail.

Confidence concerns fidelity to the source architecture, not the merit of the transfer idea. A useful conjecture can survive after its alleged precedent is corrected, but it must then be presented as Commonplace's own argument rather than attributed to the architecture.

No claim from this workshop should be promoted with an external attribution until it has been checked against a primary source. Grounding should be selective: first identify a claim that would materially change a Commonplace design or evaluation, then read the most direct paper or manual for that claim.

## Comparison boundary

The triggering table mixes at least four levels:

1. general cognitive architectures;
2. narrower cognitive models or processing strategies;
3. implementation frameworks and libraries;
4. architectures specialized for robotics, affect, teams, or social simulation.

That mismatch is itself useful. Any future comparison should type its subjects before comparing features; otherwise a library can appear to "lack" a theory of cognition and a processing principle can appear to "lack" a software ecosystem merely because unlike things occupy the same rows.

## Scan index

| Item | Recall confidence | Strongest provisional transfer |
|---|---:|---|
| [4CAPS](./4caps.md) | medium | model capacity per cooperating component and treat overload as redistribution |
| [ACT-R](./act-r.md) | high | distinguish stored chunks, cue-driven activation, retrieval, and compiled procedures |
| [ASMO](./asmo.md) | low | make attention selection an inspectable arbitration process |
| [CHREST](./chrest.md) | high | learn indexes by discriminating cases and treat expertise as retrieval structure |
| [CLARION](./clarion.md) | high | govern explicit and implicit competence as interacting but non-identical paths |
| [Copycat](./copycat.md) | high | construct representations and analogies through competing micro-hypotheses |
| [Deeplearning4j](./deeplearning4j.md) | high | type substrate, framework, model, and architecture separately |
| [DUAL](./dual.md) | medium | distinguish the durable graph from the transient coalition that becomes active context |
| [EPAM](./epam.md) | high | turn retrieval failures into new discriminations rather than adding undirected content |
| [EPIC](./epic.md) | medium-high | model tool and reasoning resources separately and study scheduling bottlenecks |
| [GLAIR](./glair.md) | medium | require knowledge-level actions to have an explicit grounding path to execution |
| [Hierarchical Temporal Memory](./hierarchical-temporal-memory.md) | high | use violated sequence expectations, not only similarity, to detect novelty |
| [LIDA](./lida.md) | high | separate availability, attentional selection, broadcast, action, and learning |
| [MAMID](./mamid.md) | low-medium | represent global control state as threshold and priority modulation rather than content |
| [Mibe](./mibe.md) | low | make abstention and source-confidence first-class outputs of broad scans |
| [OpenCog](./opencog.md) | high | separate epistemic confidence, attentional priority, utility, and behavioral authority |
| [Parallel terraced scan](./parallel-terraced-scan.md) | high | allocate deeper reading progressively while preserving exploration |
| [Procedural Reasoning System](./procedural-reasoning-system.md) | high | separate goals, applicable plans, commitments, and reconsideration conditions |
| [R-CAST](./r-cast.md) | medium | model teammates' information needs and push only decision-relevant context |
| [Soar](./soar.md) | high | use impasses to open subproblems and compile verified resolutions into fast paths |
| [Sigma](./sigma.md) | medium-high | test whether a shared inferential substrate removes real translation costs |
| [SOSIEL](./sosiel.md) | medium | evaluate methodology across heterogeneous actors and social adoption dynamics |
| [TinyCog](./tinycog.md) | low | use a minimal executable architecture as an adequacy probe, not a completeness claim |

See [working synthesis](./synthesis.md) for cross-architecture patterns and the initial grounding queue.

## Shared extraction frame

Every item is scanned for the same kinds of reusable material:

- **Ontology:** what kinds of state or entity the architecture says must be distinguished.
- **Dynamics:** how those entities become active, compete, cooperate, learn, or cause action.
- **Method:** how the architecture turns a verbal idea into a model that can be inspected or tested.
- **Transfer candidates:** concrete changes the idea might motivate in Commonplace or in agent-memory evaluation.
- **Non-transfer and failure modes:** where the analogy is likely to break or create needless machinery.
- **Grounding questions:** the smallest primary-source checks needed before attribution or adoption.

Candidate identifiers such as `ACTR-1` are workshop-local handles. They do not assert stable vocabulary or graph relations.

## What would close this workshop

The workshop closes when:

1. the promising cross-architecture candidates have been deduplicated against the existing KB;
2. candidates that could materially alter a design or evaluation have either been grounded in primary sources or rejected without that expense;
3. durable conclusions have been extracted into the appropriate notes, references, instructions, or proposals; and
4. the remaining architecture summaries no longer carry live work.

At closure this directory should be deleted, as normal for the workshop layer.

## Existing Commonplace anchors

- [Designing a memory system for LLM-based agents](../../notes/designing-agent-memory-systems.md) — working target for memory distinctions and requirements
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — existing stored/read-back/activated distinction
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — existing ACT-R/Soar proceduralization analogy
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — resource boundary against which capacity ideas should be tested
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — target for learning-loop decompositions
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — current retained-artifact ontology that cognitive-architecture distinctions may refine
