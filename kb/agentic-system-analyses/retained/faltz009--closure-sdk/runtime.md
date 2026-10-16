---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Closure-SDK current Rust Closure EA runtime: ingestion, corrective feedback, direct memory access, inference and state restoration."
run-id: AAS-2026-10-13-closure-sdk-294e6865ca51-01
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
---

# Closure-SDK runtime report

## Runtime account

The selected subsystem is a synchronous Rust geometric memory runtime, not an enclosing language-model agent. Its consequential work is to turn supplied quaternion carriers and target feedback into a mutable memory field, read that field, consolidate it and optionally save it. The public `ThreeCell` API and shipped curricula own this work; the caller owns input scheduling, targets and save/load timing. This report uses SRC-1 at the boundary's frozen commit. All findings below concern implementation or attributed design. No target code was executed, and no observed-run or causal-experiment evidence was supplied. Implemented changes and reads do not establish effective learning, activation in a deployed consumer, or measured benefit.

### Ordinary invocation and ownership

The shipped `run_learning_episode` in `closure_ea/examples/exp_neuromodulated_learning.rs` constructs a configured `ThreeCell`, repeatedly ingests context carriers, ingests a pattern, reads the last `Step.field_read`, commits that prediction and evaluates it against `true_label`. The example chooses bounded rounds and performs a final forced consolidation; it reports body tones and category-promotion counts. `teach`, `teach_batch` and `run_curriculum_passes` supply another shipped driver for the same ingest/commit/evaluate pattern (SRC-1, `closure_ea/src/teach.rs`). The literal target supplied by these drivers is the answer oracle, not an independent judge inferred from the runtime's geometric score. Who authored a caller's labels is unresolved outside the explicit example constants.

[RT-RTE-carrier-ingest](#rt-rte-carrier-ingest) follows the perceptual stage. The caller provides `[f64; 4]`; `ThreeCell::ingest` owns the next step after invocation. It pushes and ages the buffer, computes prediction error against Cell C, selects a W or RGB channel from input geometry, and computes query-conditioned ZREAD over genome plus buffer. ZREAD composes interpolated values from eligible entries rather than building text context. RESONATE then returns the closest address in that channel, carrying source population and index alongside the value. LOAD obtains a genome-only comparison value and VERIFY measures a round-trip gap. Surprise and non-self matching verification can tag buffer entries for later admission. Cell A composes raw inputs, localizes supported identity or balance closures, and emits hierarchy events; Cell C composes emitted closure carriers. Expired tagged entries enter `Genome::ingest`. Self-difference events and consolidation pressure can cause further writes. The returned `Step` exposes field read, verification, error, closure/hierarchy events, semantic signals, body tones and consolidation reports (SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/field.rs`).

[RT-RTE-prediction-feedback](#rt-rte-prediction-feedback) follows the corrective stage. Commit captures current Cell C, collects raw and inhibited Response eligibility, records co-resonance, and stages one pending prediction. Evaluation consumes that pending object, computes target discrepancy, changes eligible Response values, writes a context/target association, adjusts sequential edges, adds consolidation pressure and returns an `EvaluationReport`. The executor is ordinary Rust code in the caller process. Decisions are fixed symbolic control rules over numerical state; the distributed numerical component is [RT-CMP-three-cell](#rt-cmp-three-cell). There is no inference-provider endpoint in these inspected paths.

The teaching module's introductory prose says to ingest the target, but the actual `teach` function and its adjacent API comment instead call `evaluate_prediction(target)`. The example does likewise. Therefore this account follows the implemented corrective path, not the older top-of-file description. Explicit target ingestion remains a caller option when the target is also a sensory event, not an automatic step (SRC-1, `closure_ea/src/teach.rs`).

### Forcing cases and enforcement coverage

Three alternate cases bound the ordinary-path claims:

1. **Direct writes and forced maintenance.** `hierarchy_mut`, public genomes/entries, `Genome::learn_response`, `seed_orbit_dna`, and forced consolidation expose paths that do not pass through expired tagged-buffer promotion. Even `ingest` directly writes partial orbit positions and supported balance packets; its self-difference detector writes level 1. Thus comments calling chunk drain the only normal growth path do not describe a global enforcement boundary. [RT-RTE-direct-maintenance](#rt-rte-direct-maintenance) records the alternate mechanism. The associative-memory evaluator directly writes input/target pairs, as quoted in the boundary. These are shipped callers, not excluded hosts.
2. **Read-only inference and execution.** `evaluate` composes the input sequence and calls full-sphere RESONATE without ingest or query-channel restriction. It can read the still-live buffer, not just retained genome. `generate` instead starts from genome nearest-neighbor and follows highest-count edges. `OrbitRuntime` seeds DNA and uses `evaluate`/`evaluate_product` for orbit stepping; these deterministic consumers demonstrate why inference is not interchangeable with the teaching field read. [RT-RTE-readonly-consumption](#rt-rte-readonly-consumption) traces the path. Source-native code for Minsky/Fractran execution is present, but this report does not establish unrestricted computational correctness or absence of finite-period effects.
3. **Durable reconstruction.** Save/load reconstructs genomes, buffer, pending prediction and closure histories, bypassing ordinary admission by deserializing a `BrainState`. It resets neuromodulation, previous self-free-energy and transient salience rather than preserving every operational variable. [RT-RTE-state-restoration](#rt-rte-state-restoration) bounds the persistence claim. The target code returns errors for file/JSON failures; crash recovery and filesystem durability were not tested.

**Scoped guarantees.** The read-only inference owner is the `ThreeCell` implementation; enforcement is Rust `&self` plus the inspected body of `evaluate`/`generate`. Guarantee strength: invariant for those methods' lack of explicit state writes, not for adjacent `ingest`, commit, mutable access or reconstruction. Implementation conclusion status: wired. Operation conclusion status: uninspected. Its external contract is ordinary safe-Rust reference semantics and valid caller state; it is not a claim of semantic correctness.

The tagged-expiry gate's owner is `ingest`/`idle`; its enforcement point is the `entry.closures > 0` branch after `drain_expired`. Guarantee strength: invariant for that admission branch only. Implementation conclusion status: wired. Operation conclusion status: uninspected. It requires callers to use these methods and does not cover direct `Genome` methods, structural writes, seeding or loaded state. The VERIFY non-self-match test is similarly local; surprise can independently tag the same entry. There is no support here for a global promise that every retained carrier passed independent validation.

DNA protection is implemented by layer-sensitive write/merge/prune paths, including the explicit early return in `teach_response_at` and the skips in consolidation. Guarantee strength: protocol across these inspected methods, not a security boundary against a caller holding mutable genomes or supplying serialized state. Implementation conclusion status: wired. Operation conclusion status: uninspected. This report does not equate 'immutable DNA' with immutable Rust storage (SRC-1, `closure_ea/src/genome.rs`, `closure_ea/src/consolidation.rs`, `closure_ea/src/three_cell.rs`).

The state-save owner is `save_state_to_file`; its enforcement point is write-to-temporary followed by rename. Guarantee strength: best effort for replacement, not a demonstrated deployment guarantee. Implementation conclusion status: wired. Operation conclusion status: uninspected. It depends on OS/filesystem rename behavior and access permissions. There is no inspected sync, version migration or automatic rollback in this method; a caller retaining an earlier state can explicitly reconstruct it.

The capability surface in these paths includes numerical state mutation and caller-selected file I/O. The current grant set depends on which mutable references the enclosing program hands out; the examples grant their own code mutation authority. No deployed isolation envelope, per-content human approval or external-tool permission system is established by these APIs. The host process's filesystem credentials are external. Likewise no target-owned remote worker, shell, callback-based execution or provider-native tool appears in the selected loops; those alternatives are not asserted absent across the whole monorepo.

### Added source coverage and limits

Beyond the boundary's initial entry-point inspection, this member inspected SRC-1 `closure_ea/src/three_cell.rs` feedback, ingestion, self-observation, consolidation, inference, mutable access and persistence bodies; `closure_ea/src/teach.rs` curriculum and teaching/evaluation bodies; `closure_ea/src/field.rs` channel-aware RESONATE/ZREAD bodies; `closure_ea/src/genome.rs` admission, correction and Response credit bodies; `closure_ea/src/buffer.rs` lifetime/drain API; `closure_ea/src/consolidation.rs` entry conditions and merge eligibility; `closure_ea/src/execution.rs` orbit construction and stepping; and the learning-episode portion of `closure_ea/examples/exp_neuromodulated_learning.rs`. All are implementation evidence; their comments supply attributed design, not observed behavior. Full promotion/pruning details, all evaluator variants and every finite-state execution branch were not audited here. Their uninspected details prevent a universal correctness or completeness claim, not the bounded traces above. Memory-specific revision and inventory conclusions remain for the memory analyst.

## Shared records

### Components

#### RT-CMP-three-cell
Label: ThreeCell geometric runtime

Source-native identity: `ThreeCell`, including its hierarchy, Cell A/Cell C products, buffer, pending prediction and slow body state. Storage is in-process Rust fields and vectors; an explicit `BrainState` serializes selected fields to JSON. The operative learned field is distributed-parametric: dense quaternion addresses/values and evolving coupling/activation statistics shape reads across entries. Layer tags, indices, control thresholds and edge counts are symbolic controls, not language-model instructions. This is not an assertion of neural weights or an opaque provider.

Parameters change during operation: yes, ingest/corrective/consolidation methods change values, membership and statistics. Exact version pinned: implementation at SRC-1's commit, but caller-selected initialization and learned numerical state are not fixed by that pin. Mutable endpoint resolving to another model: inapplicable — these inspected routes call local Rust methods, not a provider endpoint. Caller replacement and `from_brain_state` can replace numerical state explicitly. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/genome.rs`.

> let rate = (t * rate_scale).clamp(0.0, 1.0);
> self.entries[idx].value = slerp(&self.entries[idx].value, actual, rate);
> --- `closure_ea/src/genome.rs`

### Operative objects

#### RT-OBJ-pending-prediction
Label: PendingPrediction corrective handoff

Source-native identity: `PendingPrediction` held in `ThreeCell.pending_prediction`. It mixes numerical predicted/context carriers and salience with symbolic source, cycle and index-bearing eligibility. Storage is an in-process `Option` copied into the serializable `BrainState`. Commit replaces the pending slot; target evaluation takes it. The object coordinates delayed feedback, not a queue or delegated worker. SRC-1, `closure_ea/src/three_cell.rs`.

> let pending = self.pending_prediction.take()?;
> let correction = compose(actual, &inverse(&pending.predicted));
> let sigma_gap = sigma(&correction);
> let correct = sigma_gap <= self.cell_a_threshold;
> --- `closure_ea/src/three_cell.rs`

### Routes

#### RT-RTE-carrier-ingest
Label: Carrier ingestion and pressure consolidation

Endpoints and owner: caller carrier → `ThreeCell::ingest` → `Step`, with local Rust rules owning all internal progression. Numeric input is supplied, not proposed by an autonomous planner. Symbolic threshold checks admit changes to a distributed numerical field. Context is genome plus live buffer and accumulated Cell A/Cell C histories. Actions stay within the owned state; hierarchy emission and local pressure-based consolidation are synchronous.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `Step` with input, field read, verification, closure/hierarchy events, error and consolidation/body-state signals.
- Later read-back: changed genome values and retained carriers enter later ZREAD/RESONATE calls; saved state can extend this horizon across processes.
- Delegated visibility: inapplicable — the selected path has no delegated execution; the caller receives the returned Step.
- Selection predicate: input geometry chooses W/RGB; address gap determines coupling, ZREAD excludes coupling below `ZREAD_T_MIN`, and RESONATE selects the closest eligible address. Admission uses surprise, verification, closure support, expiry tags and pressure.
- Invalidation or expiry: buffer ages drain at lifetime; untagged expired entries disappear; identity closure removes the resolved history window while retaining/rebuilding its prefix; consolidation can reorganize numerical memory.
- Activation or effect: implementation writes memory and reads it on later calls; no supplied run establishes exercised behavioral effect or benefit.
- Evidence limits: SRC-1 static implementation only, principally `closure_ea/src/three_cell.rs`, `closure_ea/src/field.rs`, `closure_ea/src/buffer.rs`; not a proof of convergence or all promotion/pruning conditions.

Admission roles: caller supplies carriers; runtime computes tags and structural candidates; software decides writes using fixed thresholds. There is no per-carrier human approval in the method. This is continuous perception mode or a bounded `CurriculumTrace`, depending on its caller. There is no expected-answer oracle in this perceptual stage; self-gap and verification are geometric references. Rejection is branch-level nonadmission/expiry, not content judgment. Guidance is compiled geometric rules; what persists is carriers, values, metadata and history, not a revised written theory. Recovery is explicit snapshot replacement, not automatic undo.

> let expired = self.buffer.drain_expired();
> for entry in expired {
>     if entry.closures > 0 {
>         self.hierarchy.genomes[0].ingest(
>             &entry.carrier,
>             entry.support,
>             entry.closure_sigma,
>             entry.excursion_peak,
>         );
>     }
> }
> --- `closure_ea/src/three_cell.rs:1300-1310`

A source-supported counterexample to global expiry-only admission occurs earlier in the same method:

> if sigma(&partial) > 1e-6 {
>     self.hierarchy.genomes[0].ingest(
>         &partial,
>         event.support,
>         event.sigma,
>         event.excursion_peak,
>     );
> }
> --- `closure_ea/src/three_cell.rs`

#### RT-RTE-prediction-feedback
Label: Committed prediction and target correction

Endpoints and owner: the shipped teacher/learning episode calls commit → evaluate with a target → report. Commit captures Cell C and eligibility into [RT-OBJ-pending-prediction](#rt-obj-pending-prediction). Evaluation takes that object, computes correction, credits eligible Response entries, writes the context/target association, updates edges and may consolidate. Internal policy is compiled numerical correction and layer-specific write rules. All effects occur synchronously inside the caller's `ThreeCell`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `teach` returns geometric gap; direct evaluation returns `Option<EvaluationReport>`, including feedback and consolidation summaries.
- Later read-back: updated Response values and associations participate in later field reads; sequential edges can affect generation.
- Delegated visibility: inapplicable — no worker handoff; reports and any saved state are exposed to the caller.
- Selection predicate: commit computes raw/effective Response eligibility from Cell C; correction uses target gap, stored salience and coupling; Response association selection uses context proximity.
- Invalidation or expiry: a new commit replaces the one pending slot; evaluation takes it even before subsequent writes; without pending state it returns None. Consolidation can replace/prune entries; pending slot-index stability across intervening maintenance was not established.
- Activation or effect: code changes numerical values and edges consumed by later reads; effective learning and exercised later dependence are unobserved.
- Evidence limits: SRC-1 `closure_ea/src/three_cell.rs`, `closure_ea/src/teach.rs`, `closure_ea/src/genome.rs`, `closure_ea/examples/exp_neuromodulated_learning.rs`; no independent target-validation evidence.

Admission roles and mode: the bounded curriculum/example supplies the expected target; software computes and admits the numerical change without separate approval. A caller may withhold feedback or overwrite pending state. No 'wrong-target' veto is implemented in the inspected correction body: even a geometrically correct prediction proceeds to Response credit/association writes. The improvement trigger is target discrepancy and accumulated consolidation pressure, not criticism of a formulated explanatory claim. What persists is numerical association/credit and metadata; no method-theory revision is established. Recovery requires caller-held earlier state.

> brain.commit_prediction(predicted, source);
> brain.evaluate_prediction(target);
> --- `closure_ea/src/teach.rs`

> genome.credit_response(
>     &pending.eligibility,
>     actual,
>     sigma_gap,
>     pending.salience_x,
>     self.neuromod.coherence_tone,
> );
> --- `closure_ea/src/three_cell.rs`

An important provenance limit: both `teach` and the inspected example convert any last field hit to `PredictionSource::GenomeSlot(h.index)`, although RESONATE can return `PopulationSource::Buffer`. The corrective method treats `GenomeSlot(i)` as a genome index. Thus source-population/index consistency is not guaranteed by this caller; correct credit/edge attribution for buffer-sourced predictions is not established. This does not erase the separate context/target Response write.

> source: PopulationSource::Buffer,
> index: i,
> carrier: entry.carrier,
> gap,
> --- `closure_ea/src/field.rs:125-128`

> .map(|h| PredictionSource::GenomeSlot(h.index))
> .unwrap_or(PredictionSource::GeometricFallback(predicted));
> --- `closure_ea/src/teach.rs`

#### RT-RTE-direct-maintenance
Label: Caller-directed seeding and maintenance

Endpoints and owner: caller → mutable hierarchy/genome APIs, direct DNA seeding or forced consolidation → changed field/reports. The caller chooses operands and timing. `force_consolidate` operates level 0; `sleep` forces all existing levels. Pressure-triggered calls use the same `consolidate_level` implementation without force. Consolidation takes pre-merge category candidates, merges eligible same-layer entries and can promote uncovered level-1 carriers; a full maintenance algorithm audit is left open. SRC-1, `closure_ea/src/three_cell.rs`, `closure_ea/src/consolidation.rs`, `closure_ea/src/genome.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: direct seeding returns unit; `learn_response` writes an association; forced consolidation returns per-level reports.
- Later read-back: seeded DNA, associations and consolidated/promoted state feed subsequent inference and feedback.
- Delegated visibility: inapplicable — ordinary caller-owned mutable access, no child executor.
- Selection predicate: caller chooses direct operands; seeding enumerates generator powers; learned associations select nearby Response addresses; consolidation uses numerical/layer eligibility and coverage checks.
- Invalidation or expiry: compiled merge/prune rules can remove mutable entries; direct caller mutation and state replacement can replace state outside those rules.
- Activation or effect: wiring bypasses tagged-buffer admission and changes later readable state; deployed use and benefit are unobserved.
- Evidence limits: direct write capacity is established, not universal safety or semantic correctness of caller-supplied carriers.

Admission roles: caller proposes seeding/association, fixed code admits it; caller can refuse to call a method. With `hierarchy_mut`, caller can also manipulate public genomes directly. No human identity or per-change approval follows from caller identity. Mode is explicit initialization/maintenance or a bounded evaluator, rather than autonomous improvement. Any target oracle belongs to the caller's associations, not consolidation. Force bypasses the pressure threshold, not necessarily consolidation's internal selection checks. No automatic rollback is shown; compiled geometry/configuration guides transformations and numerical field state persists.

> pub fn hierarchy_mut(&mut self) -> &mut Hierarchy {
>     &mut self.hierarchy
> }
> --- `closure_ea/src/three_cell.rs`

> let pressure_before = self.consolidation_pressure[level];
> let consolidation_threshold = SIGMA_BALANCE;
> if !force && pressure_before < consolidation_threshold {
>     return None;
> }
> --- `closure_ea/src/three_cell.rs`

> if self.entries[idx].layer == Layer::Dna {
>     return;
> }
> --- `closure_ea/src/genome.rs`

#### RT-RTE-readonly-consumption
Label: Inference generation and orbit consumption

Endpoints and owner: caller supplies sequence/seed; `evaluate`/`generate` return field hits or carrier sequences. `OrbitRuntime` supplies preseeded orbit state and consumes evaluate/product results for stepping. Selection is local deterministic numerical computation, not a model choosing a tool. It uses [RT-CMP-three-cell](#rt-cmp-three-cell) without invoking its write methods.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: optional `ResonanceHit`, bounded vector of generated carriers, or optional orbit-step carrier/slot.
- Later read-back: this is itself a consumer of previously seeded/changed genome and live buffer; it creates no retained update in the inspected methods.
- Delegated visibility: inapplicable — results return to the invoking Rust caller.
- Selection predicate: evaluate composes sequence then full-sphere nearest-address RESONATE; generation uses genome nearest seed then maximal edge count; orbit slot decoding validates hit index against orbit range.
- Invalidation or expiry: inapplicable — these methods do not expire or invalidate state; concurrent caller sequencing and earlier maintenance determine their inputs.
- Activation or effect: numerical results can determine orbit execution state; only static wiring, not a supplied execution, establishes this path.
- Evidence limits: SRC-1 `closure_ea/src/three_cell.rs`, `closure_ea/src/field.rs`, `closure_ea/src/execution.rs`; evaluated accuracy is not equivalent to the ingest-channel path, and no runtime correctness/performance measurement was made.

> pub fn evaluate(&self, seq: &[[f64; 4]]) -> Option<ResonanceHit> {
>     let mut q = IDENTITY;
>     for c in seq {
>         q = compose(&q, c);
>     }
>     crate::field::resonate(&q, &self.hierarchy.genomes[0], &self.buffer)
> }
> --- `closure_ea/src/three_cell.rs`

> self.brain
>     .evaluate_product(carrier, &self.orbits[orbit].generator)
>     .map(|hit| hit.carrier)
> --- `closure_ea/src/execution.rs`

#### RT-RTE-state-restoration
Label: BrainState save and reconstruction

Endpoints and owner: caller selects a path; `to_brain_state`/save serialize state; load/`from_brain_state` reconstruct a new runtime. Symbolic JSON structure encodes dense numerical fields, indices and histories. The filesystem is the persistent substrate; caller-chosen scheduling is outside the runtime's policy.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: save returns Result; load returns Result containing reconstructed `ThreeCell`; direct reconstruction returns the instance.
- Later read-back: restored genomes, live buffer, histories, pressure and pending prediction can enter later ingestion, read and corrective calls.
- Delegated visibility: inapplicable — no delegated process is supplied by the method; a caller may explicitly transfer its saved file.
- Selection predicate: caller supplies the complete state/path; serde parses JSON and reconstruction uses its fields rather than applying ordinary carrier-admission predicates.
- Invalidation or expiry: snapshot replacement supersedes a file; restoration resets neuromodulation and transient previous-SFE/salience; retained buffer age still participates in later expiry.
- Activation or effect: reconstruction installs behavior-shaping state into a new object; exercised use after restore and behavioral equivalence to uninterrupted operation are unobserved.
- Evidence limits: SRC-1 `closure_ea/src/three_cell.rs`; external filesystem durability, state trustworthiness, concurrent saves and migration compatibility are not established.

Admission roles: caller chooses saved/replacement content, parser checks representation, constructor installs fields. This is an explicit persistence/recovery mode, not automatic trace-driven improvement. No answer oracle or semantic acceptance gate is established. Failure propagates file/parse errors; an earlier caller-held snapshot can be reloaded, but the method does not maintain a rollback journal. Restoring runtime organization is distinct from editing product code or production machinery.

> let json = serde_json::to_string_pretty(&state)?;
> let tmp = format!("{}.tmp", path);
> std::fs::write(&tmp, &json)?;
> std::fs::rename(&tmp, path)?;
> --- `closure_ea/src/three_cell.rs`

> neuromod: NeuromodState::new(state.buffer.lifetime()),  // session-ephemeral
> --- `closure_ea/src/three_cell.rs`

### Claims

#### RT-CLM-teaching-convergence
Label: Declared curriculum convergence

The source claims repeated input/target presentation produces convergence through reinforcement rather than gradients. This is a source-native design assertion, not an observed result here. The actual corrective implementation writes numerical Response state; neither a return value nor that write establishes improved future performance. SRC-1, `closure_ea/src/teach.rs`.

> //! The brain converges when repeated presentation of (input, target) pairs
> //! causes the genome to reinforce the target slot's weight until it
> //! becomes the argmax in RESONATE. No gradient descent, no backprop —
> //! convergence is driven by the geometry of repeated closure.
> --- `closure_ea/src/teach.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-field-consumption
Label: Numerical field to runtime decisions

Consumer: channel-aware ZREAD/RESONATE in ingestion, full-sphere RESONATE in inference, and genome edge traversal in generation. Channel: numerical addresses/values and symbolic edge counts in owned runtime state. Force: compiled rules directly compute returned carriers and influence closure/credit/consolidation inputs; this is executable numerical influence, not advisory language. Horizon: later calls on the same object; across sessions only when state is explicitly saved/restored. Activation in supplied executions remains unobserved. Supported by [RT-RTE-carrier-ingest](#rt-rte-carrier-ingest), [RT-RTE-readonly-consumption](#rt-rte-readonly-consumption) and [RT-RTE-state-restoration](#rt-rte-state-restoration), whose passages establish the consumers and return channels.

## Annotations

none
