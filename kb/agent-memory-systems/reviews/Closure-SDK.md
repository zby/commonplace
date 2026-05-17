---
description: "Closure-SDK review: geometric integrity SDK plus Closure DNA and a runtime brain whose genome learns from ordered experience and feedback traces"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Closure-SDK

Closure-SDK, by Walter Henrique Alves da Silva, is a monorepo for a quaternion/S3 "geometric computer." For this review, the relevant memory surfaces are three different systems sharing the same geometry: `closure_sdk` composes ordered byte streams for integrity checks, `closure_dna` stores typed local tables with geometric identity and resonance search, and `closure_ea` implements a runtime brain with transient buffer state, persistent genome entries, prediction feedback, consolidation, and serializable `BrainState`. It is closer to a geometric runtime and database substrate than to a prose knowledge base.

**Repository:** https://github.com/faltz009/Closure-SDK

**Reviewed commit:** [dbb6fc337560336220d424aa06382fe3e4e76daf](https://github.com/faltz009/Closure-SDK/commit/dbb6fc337560336220d424aa06382fe3e4e76daf)

**Last checked:** 2026-05-16

## Core Ideas

**Ordered state is represented as a point on S3.** The SDK's primitive surface embeds bytes through SHA-256 into an S3 element, composes elements with quaternion multiplication, inverts them, measures distance from identity with `sigma`, and compares two composed states by their geometric gap ([closure_sdk/ops.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_sdk/ops.py), [README.md](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/README.md)). The retained artifact here is opaque numeric runtime state: a `ClosureState` is a quaternion snapshot with verification authority, not a readable knowledge artifact ([closure_sdk/state.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_sdk/state.py)).

**The integrity layer deliberately separates cheap monitoring from retained evidence.** `Seer` holds only one running product and can detect drift but cannot localize it; `Oracle` stores the raw record list plus a geometric path so it can recover embedded positions and localize divergence; `Witness` stores reference elements for later checks ([closure_sdk/lenses.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_sdk/lenses.py)). `RetentionWindow` is the evidence archive: a bounded deque of raw byte blocks kept so a later localization pass can investigate what the aggregate state reported ([closure_sdk/canon.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_sdk/canon.py)). Those raw records are knowledge artifacts when read as evidence; the quaternion summaries are symbolic/numeric system-definition artifacts when consumed to verify or classify stream coherence.

**Closure DNA is a local database with geometric sidecars, history, and snapshots.** `closure_dna` defines a `.cdb` directory containing `.cdna` tables, typed columns, SQL support, table integrity checks, resonance search, append-only history, named snapshots, and exact restore ([closure_dna/README.md](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_dna/README.md), [closure_dna/table.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_dna/table.py), [closure_dna/database.py](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_dna/database.py)). Its storage substrate is filesystem-backed columnar tables plus Rust engine state; its behavioral authority is database authority: rows answer queries, identities validate table state, and snapshots/history support restore and audit.

**The runtime brain has separate transient, persistent, and corrective memory.** `closure_ea` describes a stack of substrate, buffer, genome, field, hierarchy, consolidation, and three-cell runtime modules ([closure_ea/src/lib.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/lib.rs)). The buffer is transient working memory whose entries age out unless closure evidence promotes them; the genome has `Dna`, `Epigenetic`, and `Response` layers; and prediction feedback writes corrections to the Response layer rather than contaminating perceptual memory with labels ([closure_ea/src/buffer.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/buffer.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/genome.rs), [closure_ea/src/teach.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/teach.rs)). This is learned runtime state, not prose memory.

**Consolidation is implemented as merge, prune, and promotion over learned geometric entries.** `consolidate()` merges nearby non-DNA entries, prunes BKT-dead entries, preserves coalition-alive Response entries, remaps sequential edges, and collects promotion candidates before co-resonance evidence is lost by merge/prune ([closure_ea/src/consolidation.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/consolidation.rs)). `ThreeCell::consolidate_level()` can then promote qualifying Response clusters into higher-level genomes when activation, co-resonance, salience, and coherence gates pass ([closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs)). The operative representational form is mixed symbolic and distributed-parametric-like numeric state: Rust structs, counters, graph edges, quaternions, coupling statistics, and thresholded promotion rules.

**Full brain state is serializable, but some modulation remains deliberately ephemeral.** `BrainState` captures Cell A, Cell C, buffer, per-level genomes, closure levels, cycle count, consolidation pressure, pending prediction, and event log; `save_state_to_file()` writes JSON atomically via a temporary file and rename ([closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs)). `NeuromodState` records recent arousal and coherence but is explicitly not persisted; it resets on restore and only affects promotion through accumulated coherence history in genome entries ([closure_ea/src/neuromodulation.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/neuromodulation.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/genome.rs)).

## Comparison with Our System

| Dimension | Closure-SDK | Commonplace |
|---|---|---|
| Primary purpose | Geometric verification, local database, and runtime learning substrate | Agent-operated methodology KB with durable typed artifacts |
| Storage substrate | Quaternions, Rust/Python runtime structs, `.cdb` directories, table history/snapshots, JSON `BrainState` | Git-tracked Markdown notes, sources, instructions, type specs, generated indexes, validation reports |
| Representational form | Mostly symbolic code plus opaque numeric S3 state; some prose docs | Mostly prose with structured frontmatter, links, schemas, scripts, and validation code |
| Main learned state | Genome entries, Response corrections, co-resonance statistics, consolidation reports, promoted categories | Authored notes, instructions, reviews, skills, indexes, ADRs, and review findings |
| Lineage | Strong for database history/snapshots and curriculum reports; weaker for individual promoted geometric memories unless traced externally | Source snapshots, commit-pinned reviews, frontmatter status, authored links, archive/replacement lifecycle |
| Behavioral authority | Numeric state verifies, searches, predicts, corrects, consolidates, and restores runtime/database behavior | Artifacts advise agents, instruct workflows, validate structure, and guide retrieval/promotion |

The strongest alignment is the retained-artifact discipline. Closure-SDK does not treat every stored object as the same kind of "memory." A `RetentionWindow` block is evidence, a `ClosureState` is a compact verification state, a DNA genome entry is a permanent structural anchor, a Response entry is corrective learned state, and a `BrainState` JSON is a resumable runtime snapshot. That matches commonplace's need to classify artifacts by substrate, form, lineage, and behavioral authority.

The sharpest divergence is inspectability. Commonplace's durable memory is meant to be read, reviewed, linked, validated, and retired by agents and maintainers. Closure-SDK's behavior-shaping memory is mostly opaque geometric state. A future runtime can consume it directly, but a human or LLM reviewer cannot audit the meaning of one promoted quaternion the way they can audit a note, instruction, or source-pinned review.

Closure-SDK is stronger on continuous runtime memory. It has mechanisms commonplace does not have: transient working memory with lifetime, prediction staging, eligibility traces, salience-weighted correction, pairwise co-resonance, pressure-triggered consolidation, BKT pruning, category promotion, and exact runtime serialization. Commonplace is stronger on long-term governance: artifact contracts, link vocabulary, semantic review, validation, source citation, and lifecycle management.

The knowledge-artifact/system-definition-artifact split is unusual here. Many Closure artifacts are neither readable knowledge artifacts nor textual instructions. They are system-definition artifacts because the runtime consumes them with prediction, correction, verification, search, or consolidation authority. The readable knowledge artifacts are mostly docs, database rows, retained raw records, table histories, curriculum reports, and saved event logs; the decisive learned artifacts are numeric state inside the runtime.

## Trace-derived learning placement

**Trace source.** Closure-SDK qualifies as trace-derived learning through `closure_ea`, not through the byte-stream integrity SDK alone. Raw traces are ordered carrier windows, input/target curriculum examples, staged predictions, prediction feedback, eligibility sets, self-difference histories, closure events, and database/table histories. `CurriculumTrace` is explicitly a deterministic sequence of experience windows replayed through a brain, and `teach()` stages a prediction then evaluates it against a target ([closure_ea/src/teach.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/teach.rs), [closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs)).

**Extraction.** Extraction is geometric and code-mediated, not LLM-mediated. `ingest()` tags buffer entries when prediction error or verification closure fires, drains expired entries into `Genome::ingest`, records ZREAD couplings, and computes semantic residuals. `commit_prediction()` records the Response coalition and stages a pending prediction; `evaluate_prediction()` consumes reality feedback, credits causally active Response entries, writes a new Response association, and adds consolidation pressure ([closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/genome.rs)).

**Storage substrate.** Raw and intermediate traces live in runtime structs: `Buffer`, `PendingPrediction`, `ClosureEvent`, `CurriculumTrace`, `CurriculumReport`, `EvaluationReport`, and table history. Distilled state lives in `GenomeEntry` values, edges, activation counts, ZREAD coupling statistics, co-resonance lists, salience/coherence accumulators, promoted higher-level genome entries, and serialized `BrainState` JSON ([closure_ea/src/buffer.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/buffer.rs), [closure_ea/src/genome.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/genome.rs), [closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs)).

**Representational form.** Raw traces are symbolic structs containing labels, counters, carrier arrays, and reports. Distilled learned state is numeric S3 carriers plus symbolic metadata and code-enforced thresholds. There is no natural-language lesson, instruction, embedding vector store, fine-tuned model, or learned LLM policy in the inspected implementation.

**Lineage.** Lineage is strongest at runtime-report level: curriculum windows produce window reports, prediction feedback records predicted/actual/context/correction/sigma, and `BrainState` persists event logs and pending prediction state. Lineage is weaker after consolidation: promoted category carriers retain activation, closure, salience, coherence, and co-resonance summary statistics, but not a readable backlink to each source carrier window or feedback event ([closure_ea/src/consolidation.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/consolidation.rs), [closure_ea/src/three_cell.rs](https://github.com/faltz009/Closure-SDK/blob/dbb6fc337560336220d424aa06382fe3e4e76daf/closure_ea/src/three_cell.rs)).

**Behavioral authority.** Raw traces and reports are knowledge artifacts when they are inspected as evidence. Genome entries, response corrections, co-resonance statistics, consolidation pressure, table identities, snapshots, and restored `BrainState` are system-definition artifacts because they directly change prediction, retrieval, verification, pruning, promotion, restore, and database behavior.

**Scope and timing.** Learning is runtime-local and offline/online depending on caller use. `ingest()` and prediction feedback can update state online during experience; `force_consolidate()` and curriculum passes provide staged consolidation/evaluation paths. Cross-project or cross-agent reuse would require exporting or sharing `BrainState`, table directories, or source data; the repo does not provide a prose promotion path from learned geometric state into agent instructions.

**Survey placement.** Closure-SDK belongs on the trace-to-runtime-state side of the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md). It splits the survey's usual trace-to-prose pattern: traces become behavior-shaping numeric/symbolic state, not notes or skills. That strengthens the distinction between readable knowledge artifacts and non-readable system-definition artifacts.

## Borrowable Ideas

**Use compact state as an alarm, not as the evidence.** Ready to borrow for trace workflows. Closure-SDK's `Seer`/`Oracle` split is a clean pattern: cheap aggregate state can say "something changed," but localization and audit require retained source records.

**Treat runtime snapshots as first-class retained artifacts.** Worth borrowing for workshops and long-running agents. A saved state file should document which behavior-changing fields are durable, which are regenerated, and which are intentionally ephemeral.

**Separate perceptual memory from corrective memory.** Useful as vocabulary even if the geometry is not borrowed. Closure-SDK keeps Epigenetic entries and Response entries distinct, which maps to a broader KB rule: observations, corrections, and promoted rules should not share one undifferentiated storage class.

**Borrow consolidation gates only with explanation layers.** The activation/co-resonance/salience/coherence gates are interesting, but commonplace would need readable provenance and reviewable promotion records before similar gates could move durable KB artifacts.

**Do not borrow opaque carriers as KB notes.** Numeric learned state can be behaviorally powerful, but it is not a substitute for claims, sources, link semantics, or validation.

## Takeaways

**Opaque runtime state still needs artifact analysis.** Closure-SDK is a useful counterexample to prose-first KB assumptions. Its most behavior-changing retained artifacts are quaternions, counters, graph edges, table identities, and serialized Rust structs. The artifact-analysis vocabulary still applies, but review has to classify operative parts rather than read the artifact as text.

**Evidence and authority are cleanly separated in the integrity layer.** A `Seer` can detect drift cheaply, but localization requires retained raw evidence in `Oracle` or `RetentionWindow`. Commonplace should preserve the same discipline in trace workflows: compact summaries can activate investigation, but raw evidence must remain available when claims need audit.

**The database layer offers a concrete versioned substrate pattern.** Closure DNA's table history, named snapshots, exact restore, audit, repair, and resonance search are not directly a KB model, but they are relevant to any future structured-memory store that wants both query behavior and integrity checks.

**The learning layer is powerful but hard to govern.** The runtime has serious machinery for feedback, eligibility, co-resonance, consolidation, and promotion. The missing KB affordance is explanation: a promoted carrier can shape behavior without carrying a human-readable claim, source citation, retirement rule, or validation narrative.

**Do not collapse learned runtime state into "knowledge."** Some Closure artifacts are knowledge artifacts when inspected as evidence, but the operative memory is system-definition state. It predicts, validates, searches, and consolidates; it does not explain itself.

## Curiosity Pass

The most interesting mechanism is not the integrity SDK marketed as "a hash you can do algebra on." For agent-memory comparison, the deeper mechanism is the three-cell runtime's separation of transient buffer evidence, genome layers, Response feedback, and pressure-triggered consolidation.

The system has unusually strong internal semantics for state but weak external semantics for review. A promoted carrier can be mathematically meaningful to the runtime while still being opaque to an agent asked to decide whether that retained behavior should be trusted.

The database layer may be more immediately borrowable than the brain layer. Table history, snapshots, audit, repair, and resonance search are concrete storage affordances; the learning brain is a larger bet on an unfamiliar representational substrate.

## Open Questions

- Can individual promoted genome entries be explained or audited back to source curriculum windows, prediction feedback, and closure events?
- Will saved `BrainState` JSON become a stable interchange format, or is it primarily an internal checkpoint for experiments?
- How much of the learning path has been exercised outside synthetic carrier curricula and examples?
- Can Closure DNA's versioned table substrate preserve semantic lineage strongly enough for agent-memory use, or only database restore lineage?
- What governance mechanism prevents noisy or adversarial traces from producing misleading Response entries or promoted categories?
- Would a prose/export layer over genome entries be useful, or would it misrepresent numeric state as more interpretable than it is?

## What to Watch

- Whether `closure_ea` adds first-class provenance fields for promoted categories and consolidated entries.
- Whether Closure DNA exposes richer lineage for resonance hits and repaired table identities.
- Whether runtime checkpoints gain compatibility/version metadata for long-lived use.
- Whether examples move from synthetic curricula into agent task traces, tool traces, or real interaction histories.
- Whether the docs distinguish more sharply between the integrity SDK, Closure DNA, and the learning brain as separate memory systems.

## Bottom Line

Closure-SDK is best read as a geometric memory substrate: ordered evidence becomes S3 state, local tables gain geometric identity and history, and runtime experience can become learned genome state through feedback and consolidation. Its main lesson for commonplace is not a new note format, but a warning and an opportunity: behavior-shaping memory may be non-readable numeric state, so the system must still name its substrate, form, lineage, and authority before trusting it.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Closure-SDK turns ordered experience and prediction-feedback traces into behavior-shaping runtime state rather than prose artifacts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Closure-SDK requires separating raw records, quaternion summaries, database tables, genome entries, and serialized runtime snapshots by substrate, form, lineage, and authority.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - grounds: Closure-SDK's state matters when later verification, prediction, retrieval, restore, or consolidation behavior changes.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw records, histories, reports, and docs can serve as evidence, unlike opaque learned carriers consumed directly by runtime code.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: genome entries, table identities, consolidation rules, and restored brain state carry direct behavioral authority.
