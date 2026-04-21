---
description: "Geometric S3 memory and integrity runtime where ordered carrier streams promote into quaternion genome state, not readable notes or model weights"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-20"
---

# Closure-SDK

Closure-SDK is a geometric computation and memory monorepo by Walter Henrique Alves da Silva. The main product surface is a Python/Rust SDK for ordered-data verification over unit quaternions, but the repo also contains Closure DNA, a local geometric database, and `closure_ea`, a Rust "digital brain" that stores learned carrier patterns in a mutable genome. It is relevant to agent-memory review less as a ready agent memory layer than as an extreme substrate experiment: memory, integrity, retrieval, prediction, and consolidation are all expressed as operations on S3 carriers rather than prose artifacts, vector rows, or model weights. Repository: <https://github.com/faltz009/Closure-SDK>.

**Repository:** https://github.com/faltz009/Closure-SDK

**Reviewed commit:** https://github.com/faltz009/Closure-SDK/commit/818158b93c96b33cb27159ad1f4c45b07e0f9034

## Core Ideas

**Ordered data becomes a constant-size geometric identity.** The root [README](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/README.md) and [CLOSURE_SDK.md](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/CLOSURE_SDK.md) frame the system around one primitive: serialize records to bytes, embed them as unit-quaternion carriers, compose them with Hamilton products, and compare the resulting state by geodesic distance. The implemented Python API in [`closure_sdk/ops.py`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_sdk/ops.py) exposes this as `embed`, `compose`, `invert`, `sigma`, `diff`, and `compare`, backed by the Rust `closure_rs` module. This is not a semantic memory system yet; it is an integrity substrate with order sensitivity as the core affordance.

**The SDK has three observation lenses over the same carrier stream.** [`closure_sdk/lenses.py`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_sdk/lenses.py) implements `Seer`, `Oracle`, and `Witness`. `Seer` is a constant-memory running product for drift detection, `Oracle` keeps the full path so it can localize divergence, and `Witness` compares test data against a reference template through a hierarchical closure tree. This is the cleanest borrowable interface in the repo: one substrate, three memory budgets, different answers.

**Incident classification is procedural, not just algebraic.** The docs claim missing records and reorders are the two exhaustive incident types. The actual classifier in [`closure_sdk/canon.py`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_sdk/canon.py) implements two concrete modes: `gilgamesh(...)` for complete streams and `Enkidu` for online streams. `gilgamesh` localizes the first divergence with geometric paths, then walks byte records with counters and position maps. `Enkidu` keeps unmatched payload pools across cycles and reclassifies a previously missing record as a reorder if its counterpart arrives later. The geometry motivates the categories, but the classification logic still depends on ordinary byte equality, counters, retention windows, and grace-period policy.

**Closure DNA is an embedded database plus geometric identity, not an agent KB.** [Closure DNA's README](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_dna/README.md) describes a local columnar database with typed tables, SQL, version history, snapshots, audit, repair, and resonance search. The Python wrappers in [`closure_dna/table.py`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_dna/table.py) and [`closure_dna/database.py`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_dna/database.py) expose normal database operations over a Rust table engine. This makes Closure DNA closer to Binder or Atomic's infrastructure side than to a note system: durable rows and histories exist, but no code turns conversations, tool traces, or documents into durable knowledge artifacts.

**The brain layer stores learned state as quaternion genome entries.** [`closure_ea/README.md`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/README.md) and [`closure_ea/docs/CLOSURE_EA.md`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/docs/CLOSURE_EA.md) document a stack of substrate, memory, execution, brain, and learning. The implemented memory center is [`closure_ea/src/genome.rs`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/src/genome.rs): `GenomeEntry` records carry an address, value, layer, support, sequential edges, activation counters, co-resonance statistics, salience, and coherence. Layers are `Dna`, `Epigenetic`, and `Response`; DNA entries are seeded and read-only, epigenetic entries come from perception, and response entries are written by delayed evaluation.

**Learning is implemented as runtime mutation and consolidation, not as prose extraction.** [`closure_ea/src/three_cell.rs`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/src/three_cell.rs) wires the hot path: `ingest` pushes a carrier into a transient buffer, reads `genome + buffer` through ZREAD/RESONATE, records prediction error and self-free-energy, tags closure events, drains expired buffer entries into `Genome::ingest`, and accumulates consolidation pressure. [`closure_ea/src/consolidation.rs`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/src/consolidation.rs) then merges close live entries, prunes weak ones, and promotes response clusters. [`closure_ea/src/teach.rs`](https://github.com/faltz009/Closure-SDK/blob/818158b93c96b33cb27159ad1f4c45b07e0f9034/closure_ea/src/teach.rs) wraps this in curriculum traces and a supervised `teach` path. This is a real learning loop, but its artifact is opaque geometric state.

## Comparison with Our System

| Dimension | Closure-SDK | Commonplace |
|---|---|---|
| Primary substrate | Unit-quaternion carriers, Rust path/tree engines, local table directories | Markdown artifacts in git |
| Main memory unit | `GenomeEntry`, table row, stream product, or path element | Typed note/instruction/review with frontmatter and prose |
| Retrieval model | Geodesic nearest neighbor, ZREAD coalition read, RESONATE hard selection, SQL/resonance search | Search, descriptions, indexes, and authored links |
| Learning source | Ordered carriers, curriculum windows, delayed prediction feedback | Human/agent authored notes, sources, review artifacts, workshop outputs |
| Promotion target | Opaque quaternion genome entries and table state | Inspectable prose and symbolic files |
| Governance | Numeric thresholds, Rust/Python tests, database audit/repair | Deterministic validation plus semantic review and human curation |
| Best fit | Integrity checking, stream reconciliation, experimental cognitive runtime | Agent-operated knowledge work and reusable methodology |

Closure-SDK is most useful to us as a boundary case. It rejects the usual memory-system question, "what facts should we store?", and asks instead, "what if memory is a compositional state in a geometry that preserves order?" That makes it unlike Mem0-style fact stores, Binder-style typed state, or commonplace-style authored notes.

Where Closure-SDK is stronger: it has a precise treatment of ordered streams, integrity drift, localization, and constant-size summaries. `Seer` versus `Oracle` versus `Witness` is a concrete memory-budget split, and `Enkidu`'s bounded grace period is a pragmatic answer to online ambiguity. Closure DNA also shows how geometric identity can sit under a familiar SQL/table interface without exposing every caller to the math.

Where commonplace is stronger: the learned artifacts are inspectable, revisable, and meaningful to an agent without running the original program. A `GenomeEntry` can carry support, edges, salience, and coherence, but those fields do not explain themselves as portable knowledge. They are runtime state. Commonplace optimizes for durable interpretation; Closure-SDK optimizes for algebraic behavior.

The deepest divergence is substrate class. Closure-SDK's `closure_ea` is neither readable artifact learning nor weight learning. It is opaque runtime-state learning: traces mutate a hand-designed symbolic/numeric memory structure whose interpretation depends on the runtime's geometry.

## Borrowable Ideas

**Memory-budgeted lenses over one trace.** Ready to borrow conceptually. `Seer`, `Oracle`, and `Witness` name a useful design pattern: a cheap always-on monitor, an expensive recorder for localization, and a reference template for verification. In commonplace, the analogue would be lightweight workshop status, richer audit traces, and frozen reference artifacts, all explicitly separated.

**Bounded ambiguity before promotion.** Ready to borrow as a workshop principle. `Enkidu` does not immediately decide whether an unmatched online record is absent or late; it holds it for a bounded cycle and then either promotes or reclassifies. Our workshop layer could use the same posture for incomplete agent observations: hold provisional state briefly, then promote only when the uncertainty boundary closes.

**Durable state should expose identity and repair operations.** Needs a concrete use case first. Closure DNA's table `audit`, `repair`, history, snapshots, and identity operations are a strong operational package. For commonplace, this belongs under generated indexes, review-run state, or future task/workshop ledgers, not under library notes.

**Keep trace-derived state separate from authored knowledge.** Ready to borrow as a warning. Closure-SDK cleanly demonstrates a powerful trace-derived substrate that is not self-explanatory. If we ever add automated memory mining, the promoted artifact should either be readable or explicitly marked as runtime state that requires a tool to interpret.

**Use typed mutation reports at the living/reading boundary.** Ready to borrow conceptually. `ThreeCell::update` returns `UpdateReport`, while read-only methods do not. That is a useful API discipline for agent tooling: mutation paths should return structured evidence of what changed, not just success.

## Trace-derived learning placement

**Trace source.** Ordered carrier streams and curriculum windows. The source is not an assistant transcript or tool log; it is a sequence of S3 carriers produced from domain data, plus delayed target feedback in the teaching path. The trigger boundary is one `ingest` call, one sequence, or one `CurriculumWindow`.

**Extraction.** No LLM extractor. The runtime computes prediction error, ZREAD/RESONATE hits, closure tags, eligibility, salience, and co-resonance directly from carrier geometry. Buffer entries with closure evidence promote through `Genome::ingest`; delayed prediction feedback routes through `evaluate_prediction` and `credit_response`.

**Substrate class.** Opaque runtime state. The durable learned unit is a `GenomeEntry` with quaternion address/value plus metadata, or a higher-level promoted category in another genome level. It is symbolic in the broad sense that the runtime has typed fields and deterministic update rules, but it is not a readable artifact like a rule, note, or skill.

**Role.** System-definition state. The genome is not merely factual recall; reading it through ZREAD/RESONATE changes the runtime's future predictions and updates. The artifact is part of the agent's disposition, but only inside the Closure runtime.

**Scope.** Per-runtime and per-curriculum. The code supports serializable brain state and deterministic curriculum traces, but there is no implemented cross-project knowledge curation layer, no natural-language explanation layer, and no model-weight export.

**Timing.** Online during runtime ingestion, with pressure-triggered or explicit consolidation. Teaching adds staged delayed feedback, but it still mutates the same runtime memory rather than creating a separate training dataset.

**Survey placement.** Closure-SDK extends the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md) by adding an opaque runtime-state case. It is closest to trajectory-run systems in ingestion shape, but its promotion target is neither readable artifact nor weights. This strengthens the substrate-axis claim: trace-derived learning can end in a hand-designed state machine that is inspectable as code but not meaningfully inspectable as knowledge.

## Curiosity Pass

**The strongest implemented mechanism is not the grand cognitive architecture.** The repo's most stable, inspectable contribution is ordered-stream identity and localization: `ops.py`, `lenses.py`, `canon.py`, and the Rust path/tree core. The `closure_ea` brain layer is much more ambitious and internally coherent, but also harder to evaluate as an agent-memory system because success criteria are geometric rather than task- or knowledge-level.

**Memory changes meaning across the repo.** In the SDK it means a running product or retained raw block. In Closure DNA it means typed rows with identity and snapshots. In `closure_ea` it means mutable carrier attractors in a genome. Those are all real persistence mechanisms, but only the last one is trace-derived learning, and none is a human-readable KB.

**The algebraic story sometimes outruns the procedural implementation.** Missing-versus-reorder classification is presented as a geometric consequence, but `gilgamesh` still uses counters, byte equality, position lists, consumed sets, and tie-breaking heuristics. That does not make it weak; it makes the implementation more ordinary and easier to reason about than the theory language suggests.

**The simpler account is a strongly typed geometric state machine.** The code does not need to be treated as a general brain to be useful. It can be understood as a state machine where records map to carriers, distances drive thresholds, and repeated exposure updates a typed memory array. That account explains most implemented behavior with fewer metaphysical commitments.

**What could it achieve if it worked perfectly?** It could provide a compact runtime memory substrate for ordered experience, with strong integrity checks and deterministic update reports. It would still not solve knowledge curation, explanation, or cross-domain transfer unless another layer turns opaque carrier state into inspectable claims or procedures.

## What to Watch

- Whether `closure_ea` gains task-level evaluations that show the genome improves behavior beyond geometric self-consistency metrics.
- Whether Closure DNA's resonance search becomes useful for agent memory retrieval, or remains a database/integrity demonstration.
- Whether the project adds a readable explanation layer over genome entries, because that would move it closer to commonplace's artifact-centered design space.
- Whether incident classification keeps relying on byte-level side structures as examples become messier, especially duplicate-heavy or semantically equivalent streams.
- Whether the cognitive-runtime layer and the practical SDK/database layer stay aligned, or split into separate projects with different users.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Closure-SDK adds an opaque runtime-state endpoint for trace-derived learning, distinct from readable artifacts and model weights
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - sharpens: Closure-SDK separates code inspectability from knowledge inspectability; the runtime is inspectable, but the learned substrate is not human-readable knowledge
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contrasts: Closure DNA is a database-first local memory substrate with file-level persistence, but not a file-native KB
- [The fundamental split in agent memory is not storage format but who decides what to remember](../agentic-memory-systems-comparative-review.md) - extends: Closure-SDK shows a third agency pattern where deterministic geometry and thresholds decide what persists
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - contrasts: Closure-SDK has learned runtime state, but its promotion oracle is geometric closure/feedback rather than an external task-success judge
- [Binder](./binder.md) - contrasts: both expose structured operational memory, but Binder keeps typed semantic entities while Closure-SDK keeps geometric state and table identities
- [Atomic](./atomic.md) - contrasts: Atomic derives searchable semantic structures from markdown atoms; Closure-SDK derives algebraic identities and carrier memories from ordered data
