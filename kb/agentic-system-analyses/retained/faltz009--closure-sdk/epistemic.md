---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Closure-SDK Closure EA: geometric checking, target-feedback authority, text encoding and bounded mathematical outputs."
run-id: AAS-2026-10-13-closure-sdk-294e6865ca51-01
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
---

# Closure-SDK epistemic report

## Source-and-claim boundary

This report asks what the current Rust Closure EA subsystem checks, what those checks license, and how their results reach later behavior. Scope, exclusions and frozen evidence are **see [boundary](boundary.md#boundary-and-evidence)**; sources are **see [Source register](boundary.md#source-register)**. SRC-1 supplies static implementation and attributed doctrine/design, not observed execution or causal comparison. The subsystem is not assessed as an enclosing language-model agent.

Geometric objects can carry caller-defined predictions, but arbitrary quaternion values do not individuate propositions about the world. Truth-apt content is identifiable locally for reported gap/threshold results, token strings where a statement is actually supplied, solver slot-equivalence results, and integer factor witnesses. Whether an arbitrary learned carrier expresses a true external claim is `not determinable` without its encoding, interpretation and label provenance. Imported labels are not independently authenticated by geometric agreement.

Consequential source claims are [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence), [EPI-CLM-closure-convergence](#epi-clm-closure-convergence), [EPI-CLM-semantic-type](#epi-clm-semantic-type) and [EPI-CLM-prime-zeros](#epi-clm-prime-zeros). They are heterogeneous claims, not one warrant for the system. Missing target traces prevent conclusions about exercised checking and improvement; missing interventions prevent attributing an outcome to correction, consolidation or geometry. Available but uninspected mathematical examples and proof arguments prevent a system-complete negative about derivation or checking.

| Entry point or operation | SRC-1 source path | Coverage and records | Limit or conclusion prevented |
|---|---|---|---|
| Python EA command | `closure_ea/__main__.py` | Direct complete read: prints orientation and returns zero | No Rust evaluation dispatched here; sibling SDK/database commands remain excluded by boundary |
| Carrier ingest, idle, seeding, feedback, inference, generation, save/restore | `closure_ea/src/three_cell.rs`; `closure_ea/src/field.rs`; `closure_ea/src/buffer.rs` | Supplied [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest), [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback), [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance), [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption), [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration); direct feedback, verification-tag, promotion and self-observation reads | No execution; supplied population/index ambiguity remains beside feedback |
| Public update and corpus wrappers | `closure_ea/src/three_cell.rs`; `closure_ea/src/teach.rs` | Direct reads: update/update_sequence/run_curriculum call ingest; CurriculumTrace aggregates reports; see [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest) | Reporting growth/error is not acceptance of a semantic claim |
| Corrective and held-out evaluation | `closure_ea/src/teach.rs`; `closure_ea/src/genome.rs` | Direct bodies; [EPI-RTE-feedback-check](#epi-rte-feedback-check), [EPI-RTE-response-write](#epi-rte-response-write), [EPI-RTE-accuracy-report](#epi-rte-accuracy-report) | Caller labels and chosen threshold bound license; held-out provenance is not enforced |
| VERIFY | `closure_ea/src/verify.rs`; `closure_ea/src/three_cell.rs` | Direct comparison and tag-consumer reads; [EPI-RTE-verify-check](#epi-rte-verify-check) | Checks carrier closure, not external source truth |
| Merge/prune/category promotion | `closure_ea/src/consolidation.rs`; `closure_ea/src/three_cell.rs` | Direct gates, removals/remapping and promotion consumer; [EPI-RTE-category-check](#epi-rte-category-check), [EPI-RTE-category-disposition](#epi-rte-category-disposition); supplied [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance) | Full numerical merge arithmetic and all hierarchy/localization branches not audited; semantic preservation unresolved |
| Token encoding, decoding, vocabulary save/load/register | `closure_ea/src/embed.rs` | Direct public bodies and hash-base rule; [EPI-RTE-vocabulary-codec](#epi-rte-vocabulary-codec) | No semantic entailment from proximity; byte-hash dependency internals uninspected |
| Solver, CP6 classification and witnesses | `closure_ea/src/three_cell.rs`; `closure_ea/src/zeta.rs`; `closure_ea/src/lib.rs` | Direct solver/classification/factor search and CP6 assertion reads; [EPI-RTE-slot-solver](#epi-rte-slot-solver), [EPI-RTE-factor-output](#epi-rte-factor-output) | No all-input integer/overflow audit; carrier-to-integer interpretation remains conditional |
| Associative recall/noise/interference evaluator | `closure_ea/examples/exp_associative_memory.rs` | Direct write/recall/noise/before-after reads; [EPI-RTE-accuracy-report](#epi-rte-accuracy-report) | Printed comparison code is not an observed or causally identified result |
| Orbit runtime and neuromodulated episode | `closure_ea/src/execution.rs`; `closure_ea/examples/exp_neuromodulated_learning.rs` | Supplied [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption), [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback) | Full execution correctness and every example assertion unassessed |
| Other mathematical/live examples, substrate transforms, remaining inline tests | `closure_ea/examples/`; `closure_ea/src/carrier.rs`; `closure_ea/src/sphere.rs`; `closure_ea/src/hopf.rs`; `closure_ea/src/localization.rs`; `closure_ea/src/hierarchy.rs`; `closure_ea/src/neuromodulation.rs`; `closure_ea/src/lib.rs` | Included, partly covered by supplied runtime; example file inventory and scoped evaluator search only for untraced examples | Arithmetic, prime-resonance, BKT, fiber-memory, FRACTRAN, Turing, Collatz, Riemann-zero, SU2 and live-game evaluator bodies not comprehensively traced; no subsystem-wide no-evaluator or correctness verdict |
| Design and mathematical documentation | `closure_ea/README.md`; `closure_ea/docs/CLOSURE_EA.md`; `closure_ea/docs/GeometricComputer.tex`; `closure_ea/src/zeta.rs` | Direct README opening and zeta doctrine; scoped convergence search in docs; claim records below | Paper/proof correspondence, PDF and external Lean proof not audited; no theorem-to-runtime guarantee established |

No registered tool or hook dispatcher was identified in the supplied runtime routes or inspected EA command. This is a coverage observation, not a searched whole-repository absence. Exported Rust operations are the consequential surface assessed here.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | Arbitrary carrier meaning not determinable | see record | SRC-1 `closure_ea/src/three_cell.rs` | Distributed numerical field, not an automatically individuated collection of propositions |
| [RT-OBJ-pending-prediction](runtime.md#rt-obj-pending-prediction) | Caller-interpreted predicted/context carriers; no intrinsic external proposition | see record | SRC-1 `closure_ea/src/three_cell.rs` | Caller supplies target; source/index consistency unresolved in supplied teaching record |
| [EPI-OBJ-prediction-feedback](#epi-obj-prediction-feedback) | Gap and threshold agreement between supplied carriers | see record | SRC-1 `closure_ea/src/three_cell.rs` | Boolean named correct is carrier agreement, not target authentication |
| [EPI-OBJ-promotion-candidate](#epi-obj-promotion-candidate) | Recurrence/coupling/salience/coherence statistics; carrier semantics unresolved | see record | SRC-1 `closure_ea/src/consolidation.rs` | Category promotion need not assert a new proposition |
| [EPI-OBJ-vocabulary](#epi-obj-vocabulary) | Token strings may form claims only with a supplied interpretation | see record | SRC-1 `closure_ea/src/embed.rs` | Numeric map and nearest decoder do not preserve unrestricted statement meaning |
| [EPI-RTE-slot-solver](#epi-rte-slot-solver) output | First slot with equal nearest-result index, or none | see route | SRC-1 `closure_ea/src/three_cell.rs` | Nearest-slot equivalence weaker than equality of operands/results |
| [EPI-RTE-factor-output](#epi-rte-factor-output) output | Integer factor witness or primality flag for enumerated positions | see route | SRC-1 `closure_ea/src/zeta.rs` | Enumeration label is not recovered from carrier content |

## Authority-route ledger

Fields owned by records below are referenced rather than reproduced. Every listed route is supported as implementation, not observed execution. The check rows and their distinct disposition/consumer rows must not be conflated.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-vocabulary-codec](#epi-rte-vocabulary-codec) | content transformation | implemented | [EPI-OBJ-vocabulary](#epi-obj-vocabulary) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Exact token lookup is bounded; nearest output is not warranted semantics | see route | see route | SRC-1 `closure_ea/src/embed.rs` | [EPI-CLM-semantic-type](#epi-clm-semantic-type) | Case and whitespace loss | Import source warrant unknown; full semantic preservation not established |
| [EPI-RTE-vocabulary-codec](#epi-rte-vocabulary-codec) | retention | implemented | [EPI-OBJ-vocabulary](#epi-obj-vocabulary) | no content change | see route | see route | see route | see route | see route | JSON map retention is not acceptance | see route | see route | SRC-1 `closure_ea/src/embed.rs` | none | Reverse-map alias risk | No atomic paired brain/vocabulary checkpoint established |
| [EPI-RTE-verify-check](#epi-rte-verify-check) | check/evidence production | implemented | [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Carrier closure under selected tolerance only | see route | see route | SRC-1 `closure_ea/src/verify.rs` | [EPI-CLM-closure-convergence](#epi-clm-closure-convergence) | none | No source-truth license |
| [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest) | operational admission/selection/consumption | implemented | [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | non-truth-apt policy/content update: carrier tags and field membership | see record | see record | see record | see record | see record | No semantic acceptance follows from admission | see record | see [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption) | SRC-1 `closure_ea/src/three_cell.rs` | [EPI-CLM-closure-convergence](#epi-clm-closure-convergence) | Global gate counterexamples | Surprise/direct writes can admit outside VERIFY |
| [EPI-RTE-feedback-check](#epi-rte-feedback-check) | check/evidence production | implemented | [EPI-OBJ-prediction-feedback](#epi-obj-prediction-feedback) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Agreement with supplied target within threshold, not reality authentication | see route | see route | SRC-1 `closure_ea/src/three_cell.rs` | [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence) | Truth-label overreach | Label correctness and population provenance unestablished |
| [EPI-RTE-response-write](#epi-rte-response-write) | behavior/policy adaptation | implemented | [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | non-truth-apt policy/content update: numerical Response values and transition edges | see route | see route | see route | see route | see route | No evidence-consuming acceptance of an ampliative claim established | see route | see [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption) | SRC-1 `closure_ea/src/genome.rs` | [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence) | Correct is not a write gate | Carrier semantics indeterminate, numerical adaptation established |
| [EPI-RTE-category-check](#epi-rte-category-check) | check/evidence production | implemented | [EPI-OBJ-promotion-candidate](#epi-obj-promotion-candidate) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Eligibility under geometric/statistical criteria only | see route | see route | SRC-1 `closure_ea/src/consolidation.rs` | [EPI-CLM-closure-convergence](#epi-clm-closure-convergence) | none | Repeated corrections not independently validated evidence |
| [EPI-RTE-category-disposition](#epi-rte-category-disposition) | operational admission/selection/consumption | implemented | [EPI-OBJ-promotion-candidate](#epi-obj-promotion-candidate) | non-truth-apt policy/content update: promote, remove and reindex field entries | see route | see route | see route | see route | see route | Promotion/withdrawal is operational, not lifecycle integration after acceptance | see route | see route | SRC-1 `closure_ea/src/three_cell.rs` | [EPI-CLM-closure-convergence](#epi-clm-closure-convergence) | none | Merge semantic relation remains indeterminate |
| [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration) | lineage/freshness/recovery | implemented | [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | no content change | see record | see record | see record | see record | see record | Parsing licenses representation, not endorsement | see record | see record | SRC-1 `closure_ea/src/three_cell.rs` | none | Ephemeral reset | Saved numerical state is not a provenance or acceptance ledger |
| [EPI-RTE-accuracy-report](#epi-rte-accuracy-report) | check/evidence production | implemented | [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Count/gap under selected test inputs and threshold only | see route | see route | SRC-1 `closure_ea/src/teach.rs` | [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence) | No automatic disposition | No measured success or causal component effect |
| [EPI-RTE-slot-solver](#epi-rte-slot-solver) | operational admission/selection/consumption | implemented | output described above | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Quantized nearest-slot equation only | see route | see route | SRC-1 `closure_ea/src/three_cell.rs` | none | Same slot need not mean exact equality | Caller expression and encoding bound mathematical meaning |
| [EPI-RTE-factor-output](#epi-rte-factor-output) | content transformation | implemented | output described above | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Integer witnesses within checked arithmetic domain; no general carrier irreducibility license | see route | see route | SRC-1 `closure_ea/src/zeta.rs` | none | Enumeration versus carrier content | Overflow, floating bounds and four-square completeness not fully audited |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence) | see record | SRC-1 `closure_ea/src/teach.rs`, doctrine/design | see record | [EPI-RTE-feedback-check](#epi-rte-feedback-check), [EPI-RTE-response-write](#epi-rte-response-write), [EPI-RTE-accuracy-report](#epi-rte-accuracy-report) | None supplied | No intervention or measured later improvement | Corrective capacity wired | Response interpolation/association is not proof of target argmax convergence; labels unvalidated |
| [EPI-CLM-closure-convergence](#epi-clm-closure-convergence) | see record | SRC-1 `closure_ea/README.md`, doctrine/design | see record | [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest), [EPI-RTE-category-disposition](#epi-rte-category-disposition) | None supplied | Theorem prerequisites/correspondence unassessed | Closure-related updates and numerical feedback exist | Shipped teacher uses separate corrective phase; universal fixed-point/convergence warrant unestablished |
| [EPI-CLM-semantic-type](#epi-clm-semantic-type) | see record | SRC-1 `closure_ea/src/embed.rs`, doctrine/design | see record | [EPI-RTE-vocabulary-codec](#epi-rte-vocabulary-codec) | None supplied | No meaning or downstream correctness comparison | Hash-derived token identity and nearest decoding implemented | Byte identity/proximity does not establish semantic similarity or proposition fidelity |
| [EPI-CLM-prime-zeros](#epi-clm-prime-zeros) | see record | SRC-1 `closure_ea/src/zeta.rs`, doctrine/design | see record | No assessed zero-detection route; factor route is not its counterpart | None registered | Detector/example/proof correspondence unassessed | Attributed mathematical claim only in this account | No conclusion on correctness, novelty or formal proof |

## Bounded conclusion

The inspected system retains and consumes mutable numerical associations, not necessarily accepted propositions. The supplied [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption) establishes an enforcing numerical path to later reads and generation; [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration) extends it across sessions only when a caller saves and restores. Vocabulary has a separate map/file horizon. Neither persistence nor restoration grants source endorsement.

There are implemented evaluators, so an undifferentiated “no truth checking” verdict would be false. [EPI-RTE-verify-check](#epi-rte-verify-check) checks round-trip carrier closure, [EPI-RTE-feedback-check](#epi-rte-feedback-check) checks prediction-target gap, and [EPI-RTE-accuracy-report](#epi-rte-accuracy-report) computes recall/accuracy summaries. Their licenses differ. VERIFY can tag later admission; feedback changes edge weakening and consolidation pressure but does not gate the context/target write on correctness; accuracy reports have no inspected automatic acceptance consumer. None authenticates an arbitrary caller target. Direct writes, surprise and reconstruction refute any global independent-validation prerequisite for retention.

[EPI-RTE-category-check](#epi-rte-category-check) and [EPI-RTE-category-disposition](#epi-rte-category-disposition) use coupling, recurrence, salience, coherence and novelty to promote or remove operational attractors. This is evidence-responsive organization change in numerical state, not established acceptance and subsequent integration of an ampliative proposition. Its force reaches later field consumers; measured improved capacity and exercised self-improvement remain unestablished. Static update wiring alone does not close the subsequent-operation causal link. Self-observation measures field-versus-Cell-C discrepancy, rather than furnishing stated criticism of a formulated explanatory claim. These are separate findings, not a bundled negative about learning, reflection or autonomy.

For external text, [EPI-RTE-vocabulary-codec](#epi-rte-vocabulary-codec) acquires tokens with source warrant unknown and applies lossy normalization and numerical addressing. Exact lookup and nearest decoding have different guarantees. For mathematical outputs, [EPI-RTE-slot-solver](#epi-rte-slot-solver) yields checked nearest-slot agreement, and [EPI-RTE-factor-output](#epi-rte-factor-output) returns integer-search witnesses/flags subject to arithmetic and labeling limits. These local derivations do not depend on learning having succeeded. No assessed route establishes a produced accepted ampliative claim; arbitrary carrier entailment remains indeterminate, and unassessed mathematical/evaluator routes preclude a subsystem-complete negative. The convergence and prime-zero claims remain bounded by unassessed proof correspondence and missing run/causal evidence.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-prediction-feedback
Label: PredictionFeedback gap result

Part of: [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)

This returned object is a material output part of the supplied corrective route, not another pending prediction. Source-native `PredictionFeedback` has dense predicted/actual/context/correction carriers, a numerical sigma and symbolic Boolean correct; it resides in a returned `EvaluationReport`, not an independent durable ledger. SRC-1 `closure_ea/src/three_cell.rs`. The route part [EPI-RTE-feedback-check](#epi-rte-feedback-check) supplies the load-bearing passage.

#### EPI-OBJ-promotion-candidate
Label: PromotionCandidate eligibility packet

Part of: [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance)

This object is a material intermediate part of the supplied maintenance route. Source-native `PromotionCandidate` is a dense value carrier with localized numerical recurrence, salience, co-resonance and coherence statistics in an in-process vector returned by candidate collection; the packet is taken from the report and consumed at level 0. It is distinct from the enclosing runtime and its pending prediction. SRC-1 `closure_ea/src/consolidation.rs`, `closure_ea/src/three_cell.rs`; passages in [EPI-RTE-category-check](#epi-rte-category-check) and [EPI-RTE-category-disposition](#epi-rte-category-disposition).

#### EPI-OBJ-vocabulary
Label: Vocabulary token maps

Source-native `Vocabulary` stores token-to-carrier and bit-key-to-token HashMaps, and serializes only the forward map as JSON. Symbolic strings and keys coexist with dense numerical carrier values; fixed decoder rules, not a language model, consume them. Closest supplied counterpart is [RT-CMP-three-cell](runtime.md#rt-cmp-three-cell), but Vocabulary is a separate caller-side object, not its serialized BrainState or a duplicate. Its map can change through embed/register/load; exact state is not pinned by the code revision; no remote mutable model endpoint exists in this inspected implementation. SRC-1 `closure_ea/src/embed.rs`.

> let json = serde_json::to_string_pretty(&self.map)?;
> std::fs::write(path, json)?;
> --- `closure_ea/src/embed.rs`

### Routes

#### EPI-RTE-vocabulary-codec
Label: Vocabulary encoding and decoding

A distinct text boundary absent from supplied [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest): caller text → whitespace/lowercase tokens → phase-bearing carriers; caller carrier → exact or nearest token. Vocabulary owns hashing/cache/decoding, while caller owns statements, invocation and register overrides. Nearest decoding compares decomposed S² bases, ignores phase and has no rejection distance. Map save/load installs token associations without semantic checking. Register may overwrite a token while retaining old reverse aliases: later exact decode can therefore retain an earlier carrier-to-token association. These bodies establish possible lineage ambiguity, not an observed collision or wrong answer. SRC-1 `closure_ea/src/embed.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Token/carrier pairs, carrier sequence, optional exact/nearest strings, or file Result.
- Later read-back: Added or loaded map entries drive later lookup and decode calls; vocabulary file can extend this across sessions.
- Delegated visibility: inapplicable — no delegation; return values belong to caller.
- Selection predicate: Whitespace splitting and lowercase normalization; exact bit-key lookup or smallest S² base distance.
- Invalidation or expiry: register replaces forward token mapping; no expiry or reverse-alias cleanup in inspected register; load rebuilds reverse map.
- Activation or effect: Code selects returned strings and carrier sequences; semantic downstream correctness unobserved.
- Evidence limits: Direct static bodies; hashing dependency and any downstream semantic interpretation uninspected.

Concrete implementation deduction, not execution: `"US  is"` splits into `US`, `is`, then becomes `us`, `is`; phases are 0 and π. `"us is"` receives the same normalized tokens and phases. A country abbreviation and pronoun can therefore become indistinguishable at this boundary. This refutes unrestricted semantic preservation without proving that every use loses meaning. The relationship for unrestricted truth-apt text remains indeterminate between meaning-preserving normalization and changed content, not established ampliative conjecture.

> let tokens: Vec<String> = text
>     .split_whitespace()
>     .map(|tok| tok.to_lowercase())
>     .collect();
> --- `closure_ea/src/embed.rs`

> let gap = base_distance(&query_base, &stored_base);
> if gap < best_gap {
>     best_gap = gap;
>     best_token = Some(token.as_str());
> }
> --- `closure_ea/src/embed.rs`

#### EPI-RTE-verify-check
Label: Carrier closure checking

Part of: [RT-RTE-carrier-ingest](runtime.md#rt-rte-carrier-ingest)

This check part is distinct from the parent admission function. `verify` owns composition with inverse, sigma and tolerance classification. Its target is agreement/balance of two supplied carriers in quaternion geometry. At ingest, the consumer compares loaded genome reference with returned field hit; a non-self Identity **or Balance** result tags the just-pushed buffer entry. This is permissive admission evidence at buffer lifetime, not external truth endorsement. Caller sets input; software decides tags; there is no answer oracle in this check, and no per-item human approval. Surprise independently tags entries, as the supplied parent records. SRC-1 `closure_ea/src/verify.rs`, `closure_ea/src/three_cell.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: VerificationEvent with cycle, sigma, base, phase, kind and Hopf channel.
- Later read-back: Tag metadata can qualify expired carriers for genome ingestion and subsequent reads; bare verification results are not retained evidence records.
- Delegated visibility: inapplicable — synchronous local call.
- Selection predicate: Identity or balance within tolerance; ingest additionally excludes just-pushed self-match.
- Invalidation or expiry: Parent buffer expiry disposes untagged entries; verification itself changes no source content.
- Activation or effect: Classification is consumed by compiled tag branch; exercised promotion unobserved.
- Evidence limits: Geometric tolerance domain; no independent source/label validation.

> let cycle = compose(a, &inverse(b));
> let s = sigma(&cycle);
> --- `closure_ea/src/verify.rs`

> let fired = ev.closes() || ev.balances();
> if fired && !is_self_match {
> --- `closure_ea/src/three_cell.rs`

#### EPI-RTE-feedback-check
Label: Prediction target checking

Part of: [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)

This check produces [EPI-OBJ-prediction-feedback](#epi-obj-prediction-feedback); [EPI-RTE-response-write](#epi-rte-response-write) is its separate update consumer. Pending prediction → correction sigma and correct flag is owned by fixed Rust code. Target domain is supplied quaternion prediction versus actual carrier, with Cell A threshold. Teacher/example supplies the answer oracle; generic caller identity does not establish human approval or ground-truth authorship. Software computes verdict and caller can withhold/replace pending feedback. Correct controls weakening of an erroneous sequential edge; sigma adds consolidation pressure. It does not condition admission of the context/target association. SRC-1 `closure_ea/src/three_cell.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Optional feedback/report; no pending prediction returns None.
- Later read-back: Result shapes numerical updates consumed later; no inspected durable independent verdict ledger.
- Delegated visibility: inapplicable — local return to caller.
- Selection predicate: Take pending slot; correct iff sigma_gap is at most cell_a_threshold.
- Invalidation or expiry: Pending slot consumed; later commit replaces any outstanding slot.
- Activation or effect: Verdict controls edge weakening and sigma controls correction/pressure, not a truth acceptance gate.
- Evidence limits: Target provenance unknown; supplied parent records buffer/genome source-index inconsistency in teacher.

> let pending = self.pending_prediction.take()?;
> let correction = compose(actual, &inverse(&pending.predicted));
> let sigma_gap = sigma(&correction);
> let correct = sigma_gap <= self.cell_a_threshold;
> --- `closure_ea/src/three_cell.rs`

#### EPI-RTE-response-write
Label: Response correction and association

Part of: [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback)

A distinct update part, not duplicate whole feedback route. Fixed code admits target-directed Response updates from staged context/eligibility, correction sigma, salience and coherence; direct `learn_response` is an alternate caller-controlled entry described by [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance). Response proximity chooses interpolation versus a new association. Both correct and incorrect predictions proceed through learn_response. Caller can withhold target or recover prior saved state, but this body supplies no independent bad-label veto or automatic rollback. Guidance is compiled interpolation/credit rules; persisted result is values, activations and edges, not an accepted explanatory text. Intended mode is caller-led curriculum or explicit feedback; discrepancy scales update, rather than authorizing a knowledge claim. Consumer/force/horizon are see [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption). SRC-1 `closure_ea/src/three_cell.rs`, `closure_ea/src/genome.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parent EvaluationReport; learn_response itself returns unit.
- Later read-back: Response address/value and edge state enter later numerical reads and generation, and explicit snapshots.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Response eligibility indices and coupling; nearest Response address at reinforce_threshold chooses interpolation versus creation.
- Invalidation or expiry: Maintenance can merge/prune/reindex; caller replacement can overwrite state; no automatic correction rollback.
- Activation or effect: Implemented field/edge change has later consumer wiring; no observed benefit or causal attribution.
- Evidence limits: Numerical adaptation established; semantic entailment, label truth and source-index credit fidelity not established.

> genome.learn_response(&pending.context, actual);
> --- `closure_ea/src/three_cell.rs`

> let rate = (value_gap / std::f64::consts::PI).clamp(0.0, 1.0);
> self.entries[idx].value = slerp(&self.entries[idx].value, response, rate);
> self.entries[idx].activation_count += 1;
> --- `closure_ea/src/genome.rs:657-659`

#### EPI-RTE-category-check
Label: Category eligibility checking

Part of: [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance)

This candidate-check part takes a level-0 genome and returns PromotionCandidate packets before merging/pruning. Fixed program evaluates Response layer membership, BKT coupling, activation_count, mean salience, peak co-resonance and conditional coherence history. Check target is entry eligibility for operational level-1 promotion, not truth of a class explanation. Caller may trigger forced maintenance; ordinary pressure can trigger it automatically. No external answer oracle is used. Result licenses consideration for promotion, subject to level-1 novelty; [EPI-RTE-category-disposition](#epi-rte-category-disposition) owns that disposition. SRC-1 `closure_ea/src/consolidation.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate vector in consolidation report.
- Later read-back: inapplicable — packet is an intermediate check result; installed carriers, not packet retention, reach later consumers.
- Delegated visibility: inapplicable — synchronous local maintenance.
- Selection predicate: Layer/BKT/recurrence/salience/co-resonance and sufficiently sampled coherence gates.
- Invalidation or expiry: Failing entries excluded from candidate vector; vector taken by disposition consumer.
- Activation or effect: Program restricts promotable packets; no observed category validity or improved recall.
- Evidence limits: Activation_count increments on association/credit events; repetition is not evidence of independently validated targets.

> if entry.activation_count < PROMOTION_MIN_ACTIVATIONS {
>     continue;
> }
> let mean_salience = entry.mean_salience();
> if mean_salience < PROMOTION_MIN_SALIENCE {
>     continue;
> }
> --- `closure_ea/src/consolidation.rs`

> if entry.coherence_count >= PROMOTION_MIN_ACTIVATIONS
>     && mean_coherence < PROMOTION_MIN_COHERENCE
> {
>     continue;
> }
> --- `closure_ea/src/consolidation.rs`

#### EPI-RTE-category-disposition
Label: Category promotion and withdrawal

Part of: [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance)

This operational-disposition part consumes candidates, suppresses already-covered level-1 carriers and ingests others into that genome. Other maintenance gates admit same-layer merges and prune BKT-dead entries, with a Response coalition-survival exception when enabled; removals remap edges and co-resonance indices. This changes retention/organization without an epistemic acceptance decision. Software proposes from geometric history and decides by compiled gates; caller can force maintenance or replace state, not impose per-candidate human approval inside these methods. No expected-answer oracle is present. Guidance is geometry/threshold policy; values/statistics and reorganized entries persist. Recovery is caller-held prior state, not an automatic rejection journal. SRC-1 `closure_ea/src/consolidation.rs`, `closure_ea/src/three_cell.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reports including promoted and pruned counts.
- Later read-back: Surviving/promoted state reaches later field and hierarchy calls; removed entries and edges to them no longer do.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Level-1 novelty for promotion; same-layer/address and Response value/co-resonance gates for merging; BKT and coalition tests for pruning, DNA skips.
- Invalidation or expiry: Removed entry references remapped/dropped; counts do not establish semantic retraction.
- Activation or effect: Numerical membership and later selectable state change; exercised effects unobserved.
- Evidence limits: Merge arithmetic and full hierarchy consumer audit incomplete; no semantic-preservation or generalized category warrant inferred.

> if !already_covered {
>     self.hierarchy.genome_at_mut(1).ingest(
>         &candidate.carrier,
>         candidate.activation_count,
>         candidate.closure_sigma,
>         candidate.excursion_peak,
>     );
>     promoted += 1;
> }
> --- `closure_ea/src/three_cell.rs`

> entry.co_resonance = entry
>     .co_resonance
>     .iter()
>     .filter_map(|&(p, s)| new_index.get(p).copied().flatten().map(|new_p| (new_p, s)))
>     .collect();
> new_entries.push(entry);
> --- `closure_ea/src/consolidation.rs`

#### EPI-RTE-accuracy-report
Label: Accuracy and recall reporting

Distinct evaluator route with no counterpart after comparison to [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption), which supplies inference but not its scoring. `evaluate_accuracy` reads each caller input, defaults missing prediction to IDENTITY, compares with supplied target, and returns mean gap/hits. Associative example directly writes pairs, computes exact/noisy recall with 0.05 threshold and compares old recall before/after new pairs. Fixed code judges carrier-target agreement; the caller/example supplies oracle and contrast. The function calls the data held-out, but does not enforce independence from training. Mode is explicit scoring/bounded experiment; reporting does not trigger state updates, rollback or acceptance. Printed threshold markers are advisory to an inspecting person, not enforcing policy. SRC-1 `closure_ea/src/teach.rs`, `closure_ea/examples/exp_associative_memory.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Mean sigma and hit count, or printed recall/comparison markers.
- Later read-back: inapplicable — scoring retains no update consumed on a later invocation.
- Delegated visibility: inapplicable — no delegated execution.
- Selection predicate: Every supplied example; strict gap < chosen threshold; fixed noise rotations for example sweep.
- Invalidation or expiry: inapplicable — read-only scoring neither invalidates nor expires memory.
- Activation or effect: Returns/prints scores; no inspected automatic admission consumer or observed score.
- Evidence limits: Outcome fit under selected inputs/threshold does not establish mechanism, transfer or component effect; repeated missing predictions can match an IDENTITY label.

> let predicted = brain.evaluate(input).map(|h| h.carrier).unwrap_or(IDENTITY);
> let gap = sigma(&compose(&predicted, &inverse(target)));
> total_gap += gap;
> if gap < threshold {
>     exact_hits += 1;
> }
> --- `closure_ea/src/teach.rs`

> let hit = sigma(&compose(&pred, &inverse(&targets[k]))) < 0.05;
> if k < 500 && hit { after += 1; }
> if k >= 500 && hit { new_correct += 1; }
> --- `closure_ea/examples/exp_associative_memory.rs`

#### EPI-RTE-slot-solver
Label: Nearest slot equation selection

Distinct from supplied [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption): `solve` enumerates genome entries, applies caller expression to address geometry and chooses first result nearest to target's nearest slot. Runtime owns selection; caller owns expression and intended equation. Fixed nearest-index equality is evaluator and reference oracle in the quantized genome domain; there is no independent exact arithmetic check. This is a callback exposed operation omitted from the provisional runtime account: caller expression code is invoked locally. It is not target-owned remote/shell execution. Returned index has permissive force for a caller's solution choice, but no inspected post-return acceptance or retained change. SRC-1 `closure_ea/src/three_cell.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: First matching index, or None.
- Later read-back: inapplicable — no retained update in the method.
- Delegated visibility: inapplicable — callback is supplied local code, not delegation.
- Selection predicate: Genome-only nearest target/result index equality; first enumerated match.
- Invalidation or expiry: inapplicable — read-only selection does not invalidate state.
- Activation or effect: Enforces which index is returned; downstream use and equation correctness unobserved.
- Evidence limits: Different carriers may resolve to one slot; expression truth and algebraic encoding are caller contracts.

> let (target_idx, _) = self.hierarchy.genomes[0].nearest(target)?;
> for (k, entry) in self.hierarchy.genomes[0].entries.iter().enumerate() {
>     let result = make_expr(&entry.address.geometry());
>     if let Some((hit_idx, _)) = self.hierarchy.genomes[0].nearest(&result) {
>         if hit_idx == target_idx {
>             return Some(k);
>         }
>     }
> }
> --- `closure_ea/src/three_cell.rs`

#### EPI-RTE-factor-output
Label: Orbit integer factor output

No counterpart after comparison with [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption). `classify_orbit_irreducibility` and `explain_orbit_irreducibility` filter Epigenetic entries and label their enumeration k+2; they call integer primality/factor search, rather than inspect each carrier for smaller factors. Fixed integer program enumerates candidate a,b, builds four-square quaternions, multiplies and checks norm²=n. It returns a witness or no witness; CP6 inline test compares known 2..12 classification and integer factors. Test is implemented oracle code, not evidence it passed. Intended carrier interpretation requires caller-established pure orbit ordering; a richer/reorganized genome need only yield index labels. SRC-1 `closure_ea/src/three_cell.rs`, `closure_ea/src/zeta.rs`, `closure_ea/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Position/Boolean or position/optional integer-quaternion witness vectors.
- Later read-back: inapplicable — these functions install no learned or retained result.
- Delegated visibility: inapplicable — local caller/test consumption.
- Selection predicate: Epigenetic enumeration; a from 2 to floating sqrt bound; b at least a until checked product exceeds n; norm equality.
- Invalidation or expiry: inapplicable — read-only output does not invalidate memory.
- Activation or effect: Returns classifications/witnesses; inline assertions would enforce test failure on mismatch, not runtime admission.
- Evidence limits: Full four-square algorithm, float-bound and integer-overflow safety audit unperformed; no unrestricted machine-integer correctness theorem inferred.

The integer norm criterion supports local entailed output under exact arithmetic and valid four-square representatives. This is not a conjecture accepted because it was stored. Conversely, output labels alone cannot warrant that a learned carrier's content is irreducible.

> .filter(|e| e.layer == Layer::Epigenetic)
> .enumerate()
> .map(|(k, _)| {
>     let orbit = (k + 2) as u64;
>     (orbit, crate::zeta::is_prime_geometric(orbit))
> })
> --- `closure_ea/src/three_cell.rs`

> let q_b = hurwitz_int(b);
> let q_ab = hamilton_int(&q_a, &q_b);
> if norm_sq_int(&q_ab) == n {
> --- `closure_ea/src/zeta.rs`

> assert_eq!(f.a * f.b, *k, "factorization must multiply to k");
> assert!(f.a >= 2 && f.b >= 2, "factors must be > 1");
> --- `closure_ea/src/lib.rs`

### Claims

#### EPI-CLM-closure-convergence
Label: Closure convergence theorem claim

Broader than [RT-CLM-teaching-convergence](runtime.md#rt-clm-teaching-convergence), this README statement claims one closure loop updates genome/hierarchy/correction and that convergence has theorem warrant. It is doctrine/design, not observed outcome or an audited theorem/runtime correspondence. SRC-1 `closure_ea/README.md`.

> Learning happens
> through repeated closure. Convergence is a fixed-point theorem.
> --- `closure_ea/README.md`

#### EPI-CLM-semantic-type
Label: Token semantic type claim

No counterpart among supplied claims. Vocabulary declares token bytes define semantic type and phase separates position. Implementation establishes hash-derived addressing, not an independently warranted semantic embedding. SRC-1 `closure_ea/src/embed.rs`, doctrine/design.

> /// returns the same type carrier. Token bytes define semantic type, so
> /// they are projected to an S² base. The default carrier uses phase 0.
> --- `closure_ea/src/embed.rs`

#### EPI-CLM-prime-zeros
Label: Prime basis zero claim

No counterpart among supplied claims. Zeta module declares prime-basis closure events correspond to imaginary parts of Riemann zeros. This is a material mathematical warrant claim, not covered by the factor-search finding. Detector bodies, prime-zero example and proof correspondence remain unassessed here, so the claim is neither established nor refuted. SRC-1 `closure_ea/src/zeta.rs`, doctrine/design.

> //! local minima in that quantity, swept over `s`, are the closure
> //! events. For the prime basis (this module) the closures are the
> //! imaginary parts of the Riemann zeros.
> --- `closure_ea/src/zeta.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; field consumers are see [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption). New route records state their distinct return/report consumers locally.
