---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Closure-SDK Rust Closure EA memory: layered carriers, trace-conditioned consolidation, alternate checkpoints and bounded later consumers."
run-id: AAS-2026-10-13-closure-sdk-294e6865ca51-01
source-identity: "https://github.com/faltz009/Closure-SDK"
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
---

# Closure-SDK memory report

## Boundary and evidence

This report covers the current Rust Closure EA subsystem fixed by [boundary](boundary.md): quaternion admission, transient context, layered genomes, feedback, consolidation, hierarchy, explicit persistence and shipped consumers. It does not cover the sibling integrity SDK or database, archived Python runtime, homeostasis demo or browser implementation. Those exclusions prevent monorepo-wide memory conclusions. SRC-1 supplies static implementation and attributed design only; no target execution, measured learning result or causal experiment was performed. There is no established source-access gap.

The supplied [runtime](runtime.md) orders the investigation but is provisional. Direct reads below extend its coverage, especially higher-level writes, pruning, vocabulary and genome-only checkpoints. Source-native terms such as semantic, reality and category name numerical operations; they do not authenticate input truth, preserve an explanatory theory or establish semantic understanding.

| Operation or included part | SRC-1 path | Inspection and covering records / limit |
|---|---|---|
| Public Rust surface; umbrella CLI | `closure_ea/src/lib.rs`; `closure_ea/__main__.py` | Export search and complete CLI read. CLI prints paths, not a memory driver. [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell); no registered provider-tool or hook interface was identified in these entry points. |
| Ingest, update, curriculum, bootstrap, idle | `closure_ea/src/three_cell.rs` | Direct selective body reads and full memory-operation/history search; supplied [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest). [MEM-OBJ-buffer](#mem-obj-buffer), [MEM-OBJ-closure-histories](#mem-obj-closure-histories). Bootstrap's full loop and every ingest branch were not independently audited; universal admission correctness is prevented. |
| DNA, Epigenetic and Response writes; mutable access | `closure_ea/src/genome.rs`; `closure_ea/src/three_cell.rs` | Direct admission, correction, credit and seeding bodies; supplied direct-maintenance route. Separate layer objects below. Caller mutation and deserialization bypass local layer protection. |
| Read statistics, edges and co-resonance | `closure_ea/src/genome.rs`; `closure_ea/src/three_cell.rs`; `closure_ea/src/field.rs` | Direct reads; [MEM-OBJ-genome-statistics](#mem-obj-genome-statistics), feedback annotation. |
| Merge, prune, remap and promotion | `closure_ea/src/consolidation.rs`; `closure_ea/src/three_cell.rs` | Complete consolidation body and promotion consumer read; [MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation). |
| Higher-level emission and memory reads | `closure_ea/src/hierarchy.rs` | Direct ClosureLevel, cascade and level-read bodies; [MEM-RTE-hierarchy-retention](#mem-rte-hierarchy-retention). No automatic level-1-to-primary-inference delivery established. |
| ZREAD, RESONATE, Response-only reads and eligibility | `closure_ea/src/field.rs` | Direct query ZREAD, Response and inhibition bodies; supplied ordinary resonance findings. Response-only read APIs establish capabilities, not a shipped learning caller using them. |
| Evaluate, generate, solve, self-observation | `closure_ea/src/three_cell.rs` | Direct bodies; [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption) annotation. Orbit diagnostic classification bodies not inspected; no correctness assessment of their labels. |
| BrainState and genome-only reconstruction | `closure_ea/src/three_cell.rs`; `closure_ea/src/genome.rs` | Direct serializers, loaders and constructors; [MEM-OBJ-brain-state](#mem-obj-brain-state), [MEM-RTE-genome-reconstruction](#mem-rte-genome-reconstruction). |
| Vocabulary and MusicEncoder; byte/domain embedding | `closure_ea/src/embed.rs` | Direct vocabulary, role-cache and boundary functions; [MEM-OBJ-vocabulary](#mem-obj-vocabulary), [MEM-OBJ-music-encoder](#mem-obj-music-encoder). Hash/numeric encoder internals not comprehensively read; locality and uniqueness claims not established. |
| Curriculum replay and reports | `closure_ea/src/teach.rs` | Direct trace/run bodies; supplied teaching route; [MEM-OBJ-curriculum-trace](#mem-obj-curriculum-trace). Serialized trace/report reuse not established. |
| Associative and neuromodulated learning evaluators | `closure_ea/examples/exp_associative_memory.rs`; `closure_ea/examples/exp_neuromodulated_learning.rs`; `closure_ea/src/lib.rs` | Associative write/recall/interference bodies read directly; neuromodulated path supplied by runtime plus consumer search. Inline test locations searched, not executed or fully audited. No observed accuracy, promotion or round-trip result. |
| Orbit execution and other examples | `closure_ea/src/execution.rs`; `closure_ea/examples/` | Direct OrbitRuntime seed/slot/step bodies; bounded memory-consumer search across examples. Full Minsky/Fractran machines, live demos and numerical experiments not audited; prevents exhaustive consumer/correctness claims. |
| Geometry, localization, verification, body state, zeta | `closure_ea/src/carrier.rs`; `closure_ea/src/hopf.rs`; `closure_ea/src/localization.rs`; `closure_ea/src/verify.rs`; `closure_ea/src/neuromodulation.rs`; `closure_ea/src/sphere.rs`; `closure_ea/src/zeta.rs` | Public-operation searches plus their invocations in memory bodies; supplied runtime evidence. Detailed internal numerical behavior remains uninspected; no proof audit or exhaustive independent state inventory for these helpers. |
| Manifest and subsystem doctrine | `closure_ea/Cargo.toml`; `closure_ea/README.md`; `closure_ea/docs/` | Boundary-supplied dependency/design evidence; docs not independently audited here. Prevents comprehensive doctrine-to-code equivalence. |

## Core ideas

1. **Address and value have different jobs.** Numerical addresses select entries; mutable values determine returned carriers. DNA anchors, learned event carriers and context/target responses have different write rules. A response value need not resemble its address. Their later force is executable geometry, not interpreted instructions ([MEM-OBJ-response](#mem-obj-response), [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption)).
2. **Use changes both content and access statistics.** Queries record coupling; commits record coalitions; target evaluation changes Response values and correction-history statistics. Consolidation reads those traces, changes membership and can retain level-1 carriers. This is an implemented raw-to-derived-to-later-read chain, not evidence of improved future capacity ([MEM-OBJ-genome-statistics](#mem-obj-genome-statistics), [MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation)).
3. **There is no single admission boundary.** Tagged expiry, supported closure packets, higher-level cascade, feedback, direct associations, DNA seeding, mutable references and checkpoint installation all admit state under different rules. Geometric verification does not establish input trust ([MEM-RTE-hierarchy-retention](#mem-rte-hierarchy-retention), [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance), [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration)).
4. **Persistence has alternative horizons.** BrainState retains operational history and pending feedback; a genome-only checkpoint starts fresh transient context. Vocabulary persistence is separate again. Saving a numerical genome does not retain the original token labels or every reason for its transformations ([MEM-OBJ-brain-state](#mem-obj-brain-state), [MEM-RTE-genome-reconstruction](#mem-rte-genome-reconstruction), [MEM-OBJ-vocabulary](#mem-obj-vocabulary)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-buffer
Label: Buffer retained observations

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

This material state part is `Buffer`/`BufferEntry`, not another runtime component. Numerical carrier arrays are copied observations, not reconstructed source bytes; symbolic age, closure count and strongest-closure support/gap metadata govern expiry and promotion. In-process vectors are optionally serialized inside BrainState. The caller supplies carriers; ingestion pushes them, software tags them and ingestion/idle advances their age. Buffer carriers reach subsequent field reads while live. Expiry removes them and admits only tagged carriers to the genome; direct mutable access or clear can replace/remove them. Lifetime is measured in explicit ticks, not elapsed wall time. No separate content-authentication gate is shown. SRC-1, `closure_ea/src/buffer.rs`, `closure_ea/src/three_cell.rs`; comparison: a part of the runtime's combined field, not a duplicate of its route.

> if entry.age >= lifetime {
>     expired.push(entry);
> } else {
>     keep.push(entry);
> }
> --- `closure_ea/src/buffer.rs`

#### MEM-OBJ-dna
Label: DNA structural entries

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

Material numerical memory part: `GenomeEntry` with `Layer::Dna`, stored in per-level `Genome.entries`, optionally JSON. Initial ThreeCell seeds and caller-directed orbit powers supply lineage. Compiled layer checks prevent value correction in `teach_response_at` and omit DNA from merge/prune, but public entries, `seed_dna` and reconstruction permit caller replacement. This is local update protection, not immutable storage. Addresses/values feed field reads and OrbitRuntime; edges are separately operative metadata. Exact learned/seeded state is caller-dependent despite the implementation pin. SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/three_cell.rs`, `closure_ea/src/execution.rs`; [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance) supplies protection evidence.

> let nonzero_start = brain.hierarchy().genomes[0].len();
> brain.seed_orbit_dna(&generator, seed.period);
> let nonzero_end = brain.hierarchy().genomes[0].len();
> --- `closure_ea/src/execution.rs`

#### MEM-OBJ-epigenetic
Label: Epigenetic event and closure entries

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

`Layer::Epigenetic` entries contain numerical address/value geometry, with symbolic layer and index-bearing metadata. Rust vectors and optional JSON are the substrate. Origins include tagged observations, partial orbit products, balance packets, fallback materialization, higher-level closure products, self-difference packets and promoted Response values. Genome ingestion searches Epigenetic entries first: reinforce changes metadata, correct SLERPs value while leaving address fixed, otherwise create appends a learned entry. `RefusedDna` still creates Epigenetic memory; its name does not mean rejected content. Primary entries reach later field reads/generation; higher-level entries have distinct explicit level-read capabilities. Consolidation can merge/prune them. SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/three_cell.rs`, `closure_ea/src/hierarchy.rs`; this separates a material part of the combined runtime rather than duplicating [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest).

> self.create(*carrier, support, closure_sigma, excursion_peak);
> StoreOutcome::RefusedDna(self.entries.len() - 1)
> --- `closure_ea/src/genome.rs`

#### MEM-OBJ-response
Label: Response context target associations

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

`Layer::Response` stores numerical context addresses and response values in `Genome.entries`, optionally JSON. Caller-provided labels are admitted by `learn_response`; near-context writes adjust a previous value, otherwise append. Delayed feedback additionally adjusts eligible Response values. Admission is software geometry, not proof that the target is reality. The caller may withhold/replace targets; its human authorship is unresolved unless the shipped source defines literal labels. Primary field reads and the associative evaluator consume these entries; Response-only APIs offer narrower reads without establishing their use by the teacher. Merge/prune and lateral inhibition distinguish this part from Epigenetic entries. SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/field.rs`, `closure_ea/examples/exp_associative_memory.rs`; [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback) is the closest supplied route, not the same object.

> address: VerificationCell::from_geometry_or_default(context),
> value: *response,
> --- `closure_ea/src/genome.rs`

#### MEM-OBJ-genome-statistics
Label: Genome access and correction statistics

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

This part comprises GenomeEntry edges, activation/support, coupling/read counts, birth/activity cycles, co-resonance, salience and coherence aggregates. Symbolic indices/counts and numerical aggregates are stored beside content in vectors and JSON. They are not the original prediction/outcome transcript or a prose rationale. Sequential ingestion and feedback create edges; generate consumes highest-count transitions. Ingest records query-channel coupling, including below-cutoff entries even though query ZREAD omits their values. Commit records raw coalition products, while target evaluation uses inhibited eligibility and adds absolute salience/current coherence. Consolidation consumes these aggregates for merge, survival and promotion; reorganize remaps survivor indices and drops references to removed entries. Metadata therefore has behavioral force independently of carrier content. SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/field.rs`, `closure_ea/src/three_cell.rs`, `closure_ea/src/consolidation.rs`; part comparison to [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell), not a new component.

> entry.zread_t_sum += t;
> entry.zread_read_count += 1;
> --- `closure_ea/src/genome.rs:817-842`

#### MEM-OBJ-closure-histories
Label: Closure histories and emitted events

Part of: [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell)

Raw carrier histories (`cell_a_history`, ClosureLevel history) differ from derived self-difference history and `ClosureEvent` products/interval metadata. All are Rust arrays/vectors with symbolic counts, role, level and intervals; BrainState serializes them. Later localization consumes histories, Cell C composes emitted products, and higher-level cascade consumes Carry events. Cell A/ClosureLevel identity closure keeps an unresolved prefix and rebuilds its running product, discarding the closed window; balance observation does not drain Cell A. Self-difference history in the inspected detector accumulates derived differences without a corresponding drain. Emitted event records remain in hierarchy events. No fixed history-size budget or automatic textual summary was established. These are numerical working-state reductions and retained traces, not model-visible context compaction. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/hierarchy.rs`; separate material part of the runtime's accumulated context.

> let prefix = self.history[..prefix_end].to_vec();
> let (new_product, new_peak) = rebuild_from_prefix(&prefix);
> self.running_product = new_product;
> self.count = prefix.len();
> self.excursion_peak = new_peak;
> self.history = prefix;
> --- `closure_ea/src/hierarchy.rs`

#### MEM-OBJ-brain-state
Label: BrainState checkpoint payload

`BrainState` is a serialized copy/reconstruction payload, not the live [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) or a duplicate of [RT-OBJ-pending-prediction](runtime.md#rt-obj-pending-prediction), which it contains. JSON encodes numerical genomes/products/histories and symbolic organization, buffer ages, pressure, events and pending eligibility. `to_brain_state` copies fields; save persists via temporary-file rename. `from_brain_state` installs them, but starts new neuromodulation and resets previous-SFE/transient salience. Subsequent feedback can still receive saved pending salience; new commits after reload default to reset transient salience until ingestion. No schema-version migration, semantic state validation, trusted origin or atomic cross-file vocabulary coupling is established in these bodies. SRC-1, `closure_ea/src/three_cell.rs`; persistence route evidence is supplied by [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration).

> pending_prediction: state.pending_prediction,
> prev_sfe: None,
> last_salience_x: 0.0,  // transient — reset on next ingest
> --- `closure_ea/src/three_cell.rs`

#### MEM-OBJ-vocabulary
Label: Vocabulary token display mappings

No supplied object counterpart after comparison with [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell): `Vocabulary` is an external-to-ThreeCell Rust helper, not a genome field. String-to-carrier mappings are mixed symbolic lookup keys/text labels and dense numerical carriers, with a reverse exact-bit map. Labels are decoded display strings, not instructions interpreted by the numerical runtime. Embed hashes token bytes to a semantic base and supplies phase zero; tokenization lowercases whitespace tokens and adds sequence phase. Register admits explicit caller geometry. JSON saves only the forward map; load rebuilds reverse lookup. No supplied shipped caller establishes later vocabulary use; lookup/decode/nearest-decode and save/load are capabilities. Nearest decode always chooses a known base if any, without a semantic confidence veto. SRC-1, `closure_ea/src/embed.rs`.

> let base = semantic_base_from_bytes(token.as_bytes());
> let carrier = carrier_from_hopf(base, 0.0);
> self.map.insert(token.to_string(), carrier);
> self.reverse
>     .insert(carrier_key(&carrier), token.to_string());
> --- `closure_ea/src/embed.rs`

#### MEM-OBJ-music-encoder
Label: MusicEncoder role cache

No supplied counterpart after comparison with [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell). `MusicEncoder.roles` is a separate HashMap of symbolic role strings to numerical S² bases. Calls deterministically hash unseen labels, keep their bases, and return carriers with caller-supplied beat phase; later role lookup/embedding reuses the cache. No serialization or shipped memory-consumer wiring is established for this helper. It is a memoized encoding surface, not retained correction learning or a copy of Vocabulary. SRC-1, `closure_ea/src/embed.rs`.

> let base = *self
>     .roles
>     .entry(role.to_string())
>     .or_insert_with(|| semantic_base_from_bytes(role.as_bytes()));
> --- `closure_ea/src/embed.rs:576-590`

#### MEM-OBJ-curriculum-trace
Label: CurriculumTrace replay input

`CurriculumTrace`/`CurriculumWindow` retains a caller-authored ordered carrier sequence with string labels and symbolic window indices. It is an in-process Clone/Debug structure, not learned memory. Its `run` replays every carrier through ingestion, returning aggregate/per-window reports of closures, growth and errors. That transforms supplied experience into genome state; the reports alone have no established automatic later update consumer. Source comments say the trace can be saved/shared, but these inspected definitions do not implement file serialization. Distinct from [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest): an input/replay object, not that route. SRC-1, `closure_ea/src/teach.rs`.

> for q in &window.carriers {
>     let step = brain.ingest(q);
>     total_error += step.prediction_error;
>     last_sfe = step.self_free_energy;
> --- `closure_ea/src/teach.rs`

### Routes

#### MEM-RTE-memory-consolidation
Label: Trace conditioned memory consolidation

Part of: [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance)

This maintenance subroute is also invoked automatically after pressure accumulation in ingestion/feedback. Owner: compiled Rust; trigger: per-level pressure reaches SIGMA_BALANCE, or explicit force/sleep. Proposal: closest same-layer BKT-alive pairs (Response additionally needs value proximity and optional co-resonance); software decides merge/prune/promotion, caller can withhold forced invocation or retain an older checkpoint. Mode: automatic numeric maintenance or explicit bounded-episode flush, not theory revision. No answer oracle is supplied by this pass. Guidance is compiled configuration/thresholds; retained output is altered numerical field and remapped statistics. No automatic undo or per-content human approval is established. SRC-1, `closure_ea/src/consolidation.rs`, `closure_ea/src/three_cell.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structural/runtime reports, including counts; level-0 consumer takes promotion candidates and returns promoted count rather than retaining the candidate list there.
- Later read-back: Merged/pruned primary state reaches subsequent field reads and generation; promoted values reach level-1 storage and explicit level-read capabilities, not an established primary-inference consumer.
- Delegated visibility: inapplicable — synchronous maintenance in the caller's object.
- Selection predicate: Same layer, BKT coupling and address proximity; Response value proximity and configurable coalition gate; promotion requires Response layer, BKT life, repeated activation, salience and coalition floor, and conditionally coherence. Level-1 novelty coverage vetoes duplicate promotion.
- Invalidation or expiry: Removes merged losers and pruned entries, drops references to removed indices, remaps survivors/last_entry and resets activation counts. Weak Response entries can survive through coalition membership when enabled.
- Activation or effect: Implemented changes can change later numerical reads; no exercised dependence or benefit was observed.
- Evidence limits: Static full pass and consumer inspection; no learning, stability or numerical-correctness experiment. Pending prediction indices are not remapped by this pass.

Raw queries/corrections → coupling/coalition/salience aggregates → merge/prune candidates and promoted values → later primary reads or higher-level API reads. Merge averages address and value, broadens coherence width, unions edges/co-resonance and combines selected support metadata; it does not combine every statistic from the removed entry. The promoted write preserves carrier, activation-derived support, closure sigma and excursion peak, not the full coalition, salience/coherence reasons or original context/target episodes.

> genome.entries[i].value = slerp(&genome.entries[i].value, &j_value, 0.5);
> genome.entries[i].support = genome.entries[i].support.max(j_support);
> genome.entries[i].closure_sigma = (genome.entries[i].closure_sigma + j_closure_sigma) * 0.5;
> --- `closure_ea/src/consolidation.rs`

> if entry.coherence_count >= PROMOTION_MIN_ACTIVATIONS
>     && mean_coherence < PROMOTION_MIN_COHERENCE
> {
>     continue;
> }
> --- `closure_ea/src/consolidation.rs`

#### MEM-RTE-hierarchy-retention
Label: Higher level closure retention

Part of: [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest)

Owner: Hierarchy code. Trigger: a Carry event invokes the next ClosureLevel; it composes carriers and localizes a supported identity closure. At level > 0, code directly admits its packet to that level's genome and recursively emits upward. FixedPoint passed to emit_closure records the event but does not initiate cascade. Admission/selection is geometric return, excursion, local minimum and support; there is no human approval or external answer oracle. Mode: synchronous numerical stream processing. Caller chooses input, thresholds and whether to invoke; recovery is explicit prior state, not automatic rollback. Distinct subroute within ingestion, not a replacement for the supplied route. SRC-1, `closure_ea/src/hierarchy.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Produced ClosureEvents plus changed per-level histories/genomes.
- Later read-back: Retained higher-level state reaches later closure processing/maintenance; zread_level and resonate_level offer explicit reads, with an inline test caller identified but no deployed primary-inference delivery established.
- Delegated visibility: inapplicable — recursive local calls, not separate agent contexts.
- Selection predicate: Carry routes upward; supported identity-return localization creates a higher-level packet; Genome::ingest applies layer/geometric admission.
- Invalidation or expiry: ClosureLevel retains unresolved prefix, replacing its closed history window; higher-level mutable memory can subsequently merge/prune.
- Activation or effect: Code installs higher-level carriers and makes them readable; automatic influence on level-0 inference is not established.
- Evidence limits: SRC-1 bodies and level-read API; identified inline test is source, not a passed execution.

> if level > 0 {
>     self.genome_at_mut(level).ingest(
>         &event.carrier,
>         event.support,
>         event.sigma,
>         event.excursion_peak,
>     );
> }
> --- `closure_ea/src/hierarchy.rs`

#### MEM-RTE-genome-reconstruction
Label: Genome only checkpoint reconstruction

Distinct alternative to [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration), not its part: `Genome::save_to_file`/load followed by `ThreeCell::with_genome` retains only the selected genome, then constructs fresh runtime state. Caller owns file/state choice and timing; serde accepts representation, not semantic trust. Mode: explicit checkpoint/initialization; no answer oracle or per-entry approval. This admits numerical organization outside ordinary stream gates. Caller can reject a file or reconstruct an earlier one; no automatic rollback journal or full BrainState equivalence is established. SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/three_cell.rs`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: File Results and a new ThreeCell containing supplied genome; constructor asserts lifetime >= 2.
- Later read-back: Documented resumed-training caller role can ingest/read retained entries, values, edges and statistics. No shipped save/load sequence was found in the bounded consumer search.
- Delegated visibility: inapplicable — explicit local file/state transfer only.
- Selection predicate: Caller chooses complete genome and fresh thresholds/lifetime; loader parses JSON; constructor does not reapply closure admission.
- Invalidation or expiry: File replacement uses temporary rename; runtime constructor resets products/histories, pressure, buffer, pending prediction and body state; other hierarchy levels are not restored by this single-genome route.
- Activation or effect: Afforded reconstruction installs later-readable memory; exercised reuse/behavioral equivalence is unobserved.
- Evidence limits: Documented intended consumer and inspected constructors, not deployed wiring; external filesystem durability and migration remain untested.

> /// Use this after `Genome::load_from_file` to resume a saved brain.
> --- `closure_ea/src/three_cell.rs`

> consolidation_pressure: vec![0.0],
> pending_prediction: None,
> prev_sfe: None,
> neuromod: NeuromodState::new(buffer_lifetime),
> last_salience_x: 0.0,
> --- `closure_ea/src/three_cell.rs:597-601`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest)

Memory selection is request-driven by the supplied carrier: numerical geometry selects W/RGB, mode Full; ZREAD filters address channel and coupling then composes selected values in insertion order (genome before buffer). No token budget, top-k or textual context window is supplied. Buffer lifetime limits live observations, not genome size. Later retained-memory reads occur at subsequent calls, not merely because the current input was just pushed. Local LOAD differs by population: genome hits load exact index, while buffer hits perform genome nearest-address fallback. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/field.rs`.

> PopulationSource::Genome => self.hierarchy.genomes[0].entries[hit.index].value,
> PopulationSource::Buffer => match self.hierarchy.genomes[0].nearest(&hit.carrier) {
>     Some((idx, _)) => self.hierarchy.genomes[0].entries[idx].value,
>     None => IDENTITY,
> },
> --- `closure_ea/src/three_cell.rs`

#### On [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)

The update consumer receives captured Cell C, caller prediction, inhibited Response eligibility and perception-time signed salience; coalition statistics use raw eligibility instead. They do not establish that eligible entries actually produced the caller's prediction, since commit accepts any supplied carrier. Later field reads consume corrected values and context/target associations; generate consumes edge changes. Saved pending state retains these fields, but intervening consolidation may invalidate indices. No retained prose reason or target-authentication evidence is present in these numerical writes. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/field.rs`, `closure_ea/src/genome.rs`.

> self.hierarchy.genomes[0].record_co_resonance(&raw); // structural: full coalition evidence
> self.stage_prediction(predicted, context, source, effective); // causal: winner-suppressed
> --- `closure_ea/src/three_cell.rs`

#### On [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption)

Evaluate selects nearest address over genome plus live buffer after composing the caller sequence; generate selects a genome seed then highest-count edges, bounded by caller steps. Neither returns a complete memory transcript. Solver additionally scans genome addresses, evaluates a caller expression and compares result/target nearest-slot identity, excluding buffer to avoid namespace confusion. OrbitRuntime seeds DNA and uses evaluate/product values for steps, while associative recall queries retained Response associations against caller-supplied expected targets. These are wired consumers, not merely storage APIs. Response-only and higher-level reads remain additional API capabilities unless an actual caller is identified. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/execution.rs`, `closure_ea/examples/exp_associative_memory.rs`.

> let (target_idx, _) = self.hierarchy.genomes[0].nearest(target)?;
> for (k, entry) in self.hierarchy.genomes[0].entries.iter().enumerate() {
>     let result = make_expr(&entry.address.geometry());
> --- `closure_ea/src/three_cell.rs`

> let pred = brain.evaluate(&[inputs[k]]).map(|h| h.carrier).unwrap_or(IDENTITY);
> if sigma(&compose(&pred, &inverse(&targets[k]))) < 0.05 { exact_0 += 1; }
> --- `closure_ea/examples/exp_associative_memory.rs`

#### On [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration)

The selected persistent payload includes raw and derived histories, events and pending correction, not just learned values. Loader/constructor accepts caller-chosen numerical state without ordinary admission. Vocabulary is not included. Restoring body state is partial: fresh neuromodulation can change future feedback/promotion despite restored carrier memory. BrainState save/load establishes a capability; no shipped deployed cross-process reuse was established. SRC-1, `closure_ea/src/three_cell.rs`; the supplied route retains the serializer and reset passages.

## Write side

Each control is kept separate from content origin and I/O:

| Mechanism | Authorship / proposal origin | Admission control | Retained result and later consumer |
|---|---|---|---|
| Tagged expiry in ingest/idle | Caller carriers; runtime closure/surprise/verification tags | Software requires expired age and closures > 0; untagged entries discarded | Learned event carrier → subsequent primary field reads; [MEM-OBJ-buffer](#mem-obj-buffer), [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest). |
| Partial orbit/balance writes | Derived Cell A history products | Code excludes trivial partials or requires balance support; not the expiry gate | Epigenetic addresses/values → later primary reads; [MEM-OBJ-epigenetic](#mem-obj-epigenetic). |
| Higher-level cascade / self-difference | Derived closure packets or numerical self-model/field discrepancy | Localized supported return or supported balance detection | Higher-level Epigenetic memory → explicit level-read API and maintenance, not demonstrated primary inference; [MEM-RTE-hierarchy-retention](#mem-rte-hierarchy-retention), [MEM-OBJ-closure-histories](#mem-obj-closure-histories). |
| Target correction and direct association | Caller target, captured context, eligibility/salience | Fixed credit/layer/near-context rules; no target truth veto | Response values, aggregates and edges → field reads/consolidation/generation; [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback), [MEM-OBJ-response](#mem-obj-response). |
| Seeding and public mutation | Source-native initial constants or arbitrary caller state | Local seed APIs append; public mutable fields let caller edit outside local gates | DNA or other edited state → numerical consumers; [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance), [MEM-OBJ-dna](#mem-obj-dna). |
| Consolidation | Query and correction traces summarized into statistics | Software merge/prune/promotion gates; forced invocation bypasses pressure only | Changed field / higher-level values → later reads; [MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation). |
| State installation | Caller checkpoint / deserialized fields | Parser representation acceptance and constructor; no ordinary stream gate | Restored operational field or genome-only field → later calls; [MEM-OBJ-brain-state](#mem-obj-brain-state), [MEM-RTE-genome-reconstruction](#mem-rte-genome-reconstruction). |
| Token/role caches | Caller strings, explicit registrations or deterministic hashes | Software caching; register replaces forward mapping without semantic approval | Encoding/display capability; [MEM-OBJ-vocabulary](#mem-obj-vocabulary), [MEM-OBJ-music-encoder](#mem-obj-music-encoder). |

Generic caller identity does not establish human per-content approval. Numerical memory stores a mixture of externally supplied inputs and runtime-derived products; original bytes, author identities and explicit supporting reasons are not reconstructed by these carrier writes. Maintenance withdraws entries according to coupling/coalition rules, not falsified-claim judgments. A weak Response entry can survive coalition pruning, so below-BKT does not universally imply withdrawal. Genome changes retain some metadata but not a full update audit. Saved earlier states afford manual replacement; no automatic rejection/rollback system was established. All rows are static SRC-1 implementation, not observed writes.

## Read-back

The primary later consumers are ingestion/self-observation field reads, corrective feedback, generation, associative recall and OrbitRuntime. Their selectors and delivery channels are in the annotations and supplied [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption). Invocation supplies the query/seed/target; code automatically selects from owned retained numerical state and returns a carrier/hit/report or updates state. This is a requested computation with internal selection, not unsolicited document injection into an LLM. Persistence is same-object by default and explicit checkpoint-mediated across instances.

Higher-level genomes are not pooled into the primary level-0 ZREAD/evaluate path. Their explicit `zread_level`/`resonate_level` operations use an empty buffer and caller-selected level, channel and address mode. Source searches identified inline test calls, not deployed consumption of promoted categories by primary prediction. Response-only reads exclude buffer, but the shipped teacher's last field read is not thereby a Response-only prediction. Vocabulary decode selects token display labels; its existence does not establish a runtime language consumer. These capability/consumer distinctions prevent overstating memory integration.

Working-context control is numerical, not model-visible: buffer tick/drain removes observations, identity closure keeps unresolved prefixes and derived products/events remain, and maintenance edits the retained field. There is no separate-agent frame in the inspected synchronous loops. History replacement resembles freeing a resolved software work segment, but the surviving quaternion is a derived value, not a pointer permitting lossless source reload. Only explicitly retained histories/checkpoints can restore discarded material, and genome-only checkpointing intentionally omits it ([MEM-OBJ-closure-histories](#mem-obj-closure-histories), [MEM-OBJ-brain-state](#mem-obj-brain-state)).

## Integration issues

- **Higher-level write correction:** The supplied runtime's perceptual account describes hierarchy emission without tracing the direct higher-level Genome::ingest branch. Inline comments even say the hierarchy never writes. The actual `ingest_at_level` writes at level > 0. Reconciliation should connect this additional subroute to [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest), not extend expiry-only admission to all levels ([MEM-RTE-hierarchy-retention](#mem-rte-hierarchy-retention)).
- **LOAD correction:** Runtime's ordinary account describes LOAD as genome nearest-to-hit lookup. Actual code uses exact index for genome hits and nearest-address fallback only for buffer hits. This matters when address/value drift diverges; see the annotation on [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest).
- **Statistics qualification:** `record_zread_contributions` records every same-channel entry, including low-coupling entries excluded from the actual query ZREAD. The source comment that these are only actual participants is too strong. Pruning aggregates measure eligible-channel coupling, not exclusively selected-value contributions ([MEM-OBJ-genome-statistics](#mem-obj-genome-statistics)).
- **Coherence gate qualification:** Promotion does not universally require nonnegative coherence: negative mean blocks only when coherence_count >= PROMOTION_MIN_ACTIVATIONS. This preserves supported promotion even with insufficient coherence history; blanket negative-coherence exclusion would be wrong ([MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation)).
- **Later consumer gap:** Promoted Response values and self-difference/higher-level closure packets are stored and exposed through level-read APIs, but automatic influence on primary prediction was not established by the bounded source/consumer search. It prevents a claim that promotion improves level-0 recall ([MEM-RTE-hierarchy-retention](#mem-rte-hierarchy-retention), [MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation)).
- **Feedback attribution/index gap:** Supplied runtime already identifies Buffer hit indices labelled GenomeSlot by teaching callers. Commit eligibility is derived from Cell C, not verified against the supplied prediction's actual producer. Maintenance remaps genome references but not the pending eligibility/source indices; feedback after intervening maintenance or state installation can therefore lack stable lineage. Correct-credit and edge-attribution guarantees are prevented, not the separate context/target write ([RT-OBJ-pending-prediction](runtime.md#rt-obj-pending-prediction), [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback), [MEM-RTE-memory-consolidation](#mem-rte-memory-consolidation)).
- **Vocabulary replacement issue:** Register overwrites the forward token mapping but does not remove its prior reverse key in the inspected body. Exact decode can therefore retain a stale alias until save/load rebuilds reverse lookup. Collision/alias handling and fresh-vs-reloaded display equivalence are unestablished ([MEM-OBJ-vocabulary](#mem-obj-vocabulary), SRC-1, `closure_ea/src/embed.rs`).
- **Checkpoint scope:** Genome-only reconstruction and full BrainState are different payload/horizon contracts. Vocabulary must be saved separately for token recovery; no coupled checkpoint transaction or shipped save/reload sequence was found in the bounded search. Cross-session effectiveness and uninterrupted-state equivalence remain unobserved ([MEM-RTE-genome-reconstruction](#mem-rte-genome-reconstruction), [MEM-OBJ-brain-state](#mem-obj-brain-state), [MEM-OBJ-vocabulary](#mem-obj-vocabulary)).
- **Record comparison:** All contained state parts and subroutes explicitly name their runtime parent. BrainState is a distinct payload, not another live runtime; genome reconstruction is a distinct alternative to full-state restoration. Vocabulary, MusicEncoder and CurriculumTrace have no supplied object counterparts. No possible duplicate is proposed for supersession.

## Limitations and checks

HEAD was rechecked as 9735f48a6ddd00b6f429a91443489531b3a115ef and checkout status was clean. Added findings use SRC-1 at that boundary; searches ran in its registered checkout. The invocation, supplied member types, boundary/runtime, worker rules, collection contract and complete record contract were read; no prior target analysis, other attempt or engine state was consulted. The collection's complete-artifact authority is not invoked: only assigned worker outputs are written.

The coverage table retains available but uninspected helper internals/evaluator variants separately from source-access gaps. No numerical proof, complete hook/consumer enumeration, filesystem crash experiment, measured learning, deployed activation or causally supported benefit follows from this source account. Checkpoint reasons/provenance and every opaque external compiler/filesystem responsibility remain bounded as stated. Model-visible context controls are inapplicable to the inspected numerical consumers, not asserted absent throughout the monorepo.

Deterministic validation: the required validate-output command passed after checking output structure, identity, citations and quotation occurrence. This establishes form, not analytical acceptance or claim support.
