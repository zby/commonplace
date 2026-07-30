# Mechanism boundary adjudication results

**Date:** 2026-07-29

**Status:** maintainer adjudication complete for all 42 rows; no catalogue, contract, authorization, ADR, migration, or corpus change has been made.

**Protocol:** [mechanism boundary adjudication protocol](./mechanism-boundary-adjudication-protocol.md)

**Frozen surface:** [42-row manifest TSV](./mechanism-boundary-adjudication-manifest.tsv)

**All boundary records:** [126-vote TSV](./mechanism-boundary-adjudication-votes.tsv)

## Result

All 42 frozen rows received three independent exact-choice votes. Thirty-six rows (85.7%) have an exact 2/3-or-better majority: 22 unanimous (52.4%) and 14 contested (33.3%). Six rows (14.3%) are three-way UNSTABLE and have no aggregate recommendation.

The exact vocabulary materially narrows the proposed split. Only 11 of the 42 boundary rows return to it: 10 `explained-by` and one `operates-through`. Twenty-five stable rows instead map to a more exact existing relation or the prerequisite hold, and six remain unresolved. Combined with the accepted 87-row unanimous core, the current 129-row surface would contain 66 `explained-by`, 32 `operates-through`, 25 other exact dispositions, and 6 unresolved rows if the stable recommendations below are accepted.

The 18 rows whose coarse EX/OP result was contested are especially diagnostic: eight remain in the split, eight move to existing exact relations, and two remain unstable. The earlier ambiguity was therefore not only an EX-versus-OP boundary problem; broad labels had also absorbed development, exemplification, definition, and evidence relations.

## Exact distribution

| exact result | rows | unanimous | contested | authorization impact |
|---|---:|---:|---:|---|
| `explained-by` | 10 | 2 | 8 | `candidate-new` ×10 |
| `operates-through` | 1 | 1 | 0 | `candidate-new` ×1 |
| `exemplifies` | 8 | 6 | 2 | `authorized` ×8 |
| `extends` | 8 | 8 | 0 | `authorized` ×8 |
| `defined-in` | 2 | 2 | 0 | `authorized` ×2 |
| `evidenced-by` | 1 | 1 | 0 | `authorized` ×1 |
| `is-evidence-for` | 1 | 1 | 0 | `candidate-delta` ×1 |
| `contrasts` | 1 | 0 | 1 | `authorized` ×1 |
| `rests-on` | 1 | 1 | 0 | `authorized` ×1 |
| `see-also` | 2 | 0 | 2 | `candidate-delta` ×2 |
| `prerequisite-hold` | 1 | 0 | 1 | `deferred-family` ×1 |
| `UNSTABLE` | 6 | 0 | 0 | `—` ×6 |

### Coarse-to-exact movement

| full-run coarse result | rows | exact outcomes |
|---|---:|---|
| `EX` | 9 | `UNSTABLE` ×1, `exemplifies` ×3, `explained-by` ×4, `operates-through` ×1 |
| `OP` | 9 | `UNSTABLE` ×1, `defined-in` ×1, `evidenced-by` ×1, `exemplifies` ×1, `explained-by` ×3, `extends` ×2 |
| `EN` | 4 | `exemplifies` ×1, `explained-by` ×1, `extends` ×1, `prerequisite-hold` ×1 |
| `OTHER` | 18 | `UNSTABLE` ×4, `contrasts` ×1, `defined-in` ×1, `exemplifies` ×2, `explained-by` ×2, `extends` ×5, `is-evidence-for` ×1, `see-also` ×2 |
| `UNSTABLE` | 2 | `exemplifies` ×1, `rests-on` ×1 |

## Authorization readout

Authorization was assessed after semantic choice. Among the 36 stable recommendations:

- 21 use labels already authorized for the exact pairing;
- 11 use the accepted-but-not-yet-adopted notes→notes candidates: ten `explained-by` and one `operates-through`;
- 3 require separate notes→notes authorization decisions: `see-also` for `F043` and `F048`, and `is-evidence-for` for `F066`;
- 1, `F094`, remains `prerequisite-hold` pending the `enables` / `precondition` family review.

The sole reference→notes row, `F115`, is unanimously `rests-on`, which the reference contract already authorizes. The mechanism split therefore demonstrates no reference→notes authorization need. Do not widen that pairing.

The earlier grounds adjudication independently accepted `premised-on`; no boundary row receives a stable `premised-on` majority here. This packet neither reopens that decision nor adopts its pending catalogue and notes-contract entries.

The final maintainer decision removes every proposed notes→notes `see-also` edge rather than authorizing that pairing. `F043` and `F048` therefore do not create an authorization delta; `F066` remains the only boundary-row candidate delta (`is-evidence-for` notes→notes).

Accepting a semantic disposition below does not itself approve a contract delta. Pairing and catalogue changes remain a later maintainer gate after every row is settled.

## Rebaseline and execution

The dispatch re-resolved all 42 source links against their targets: 24 active `mechanism` rows and 18 deferred `grounds` rows, comprising 41 notes→notes pairs and one reference→notes pair. All tuples resolved exactly once before dispatch and again after the run; no row disappeared or moved.

Four deterministic batches received three fresh isolated classifier contexts each. All 126 records parsed with the required fields. Classifiers were barred from the prior result and vote ledgers and from one another's output. No model override was supplied; exact runtime identifiers were not exposed, so this demonstrates context-level independence rather than cross-model-family replication.

### Broader-surface syntax check

A syntax-aware post-run check against the full 129-row reclassification manifest found all 129 tuples: 82 active `mechanism` rows and all 47 deferred `grounds` rows. `F019`, `F022`, and `F054` now use the accepted ASCII `-- mechanism:` marker rather than the em-dash form. An em-dash-only check would falsely report those rows as deleted; tuple identity is source plus resolved target, not punctuation glyph. No active mechanism tuple was added or removed.

## Per-row adjudication ledger

Votes are `choice/confidence`. A 2/3 result is a recommendation, not an automatic disposition. Full reader needs, revision consequences, boundary tests, authorization records, and justifications are in the linked vote TSV.

| ID | source → target | coarse | A | B | C | exact result | status | auth |
|---|---|---|---|---|---|---|---|---|
| F006 | `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:51 → kb/notes/false-positive-generation-is-filtered-before-retention.md` | `OTHER/contested` | `exemplifies/medium` | `exemplifies/high` | `exemplifies/high` | `exemplifies` | unanimous | `authorized` |
| F013 | `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:58 → kb/notes/axes-of-artifact-analysis.md` | `OP/contested` | `extends/medium` | `explained-by/medium` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| F015 | `kb/notes/the-framework-is-often-larger-than-the-durable-contribution.md:62 → kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` | `OTHER/unanimous` | `explained-by/medium` | `explained-by/medium` | `explained-by/high` | `explained-by` | unanimous | `candidate-new` |
| F026 | `kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md` | `EX/contested` | `is-evidence-for/high` | `exemplifies/high` | `exemplifies/medium` | `exemplifies` | **contested** | `authorized` |
| F027 | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | `EX/contested` | `exemplifies/high` | `exemplifies/high` | `exemplifies/medium` | `exemplifies` | unanimous | `authorized` |
| F028 | `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:60 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | `UNSTABLE/unstable` | `exemplifies/medium` | `exemplifies/high` | `exemplifies/medium` | `exemplifies` | unanimous | `authorized` |
| F030 | `kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:64 → kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` | `OTHER/unanimous` | `operates-through/high` | `see-also/medium` | `premised-on/medium` | `UNSTABLE` | **UNSTABLE** | `—` |
| F031 | `kb/notes/design-for-the-first-time-human-except-on-access-cost.md:26 → kb/notes/feasibility-is-the-heaviest-forks-net-load.md` | `OTHER/unanimous` | `see-also/medium` | `explained-by/medium` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| F032 | `kb/notes/reflection-buys-addressability.md:68 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md` | `EN/contested` | `evidenced-by/high` | `explained-by/medium` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| F035 | `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → kb/notes/bounded-context-orchestration-model.md` | `EX/contested` | `premised-on/high` | `extends/high` | `operates-through/medium` | `UNSTABLE` | **UNSTABLE** | `—` |
| F040 | `kb/notes/retrieval-failure-is-reflection-failure.md:40 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | `EX/contested` | `operates-through/high` | `explained-by/high` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| F042 | `kb/notes/semantic-review-catches-content-errors-that-structural-validation.md:49 → kb/notes/text-testing-framework.md` | `OTHER/contested` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F043 | `kb/notes/bounded-context-orchestration-model.md:97 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | `OTHER/unanimous` | `see-also/medium` | `see-also/medium` | `other:exemplified-by/medium` | `see-also` | **contested** | `candidate-delta` |
| F044 | `kb/notes/error-messages-that-teach-are-a-constraining-technique.md:28 → kb/notes/frontloading-spares-execution-context.md` | `EX/contested` | `operates-through/high` | `operates-through/high` | `operates-through/high` | `operates-through` | unanimous | `candidate-new` |
| F046 | `kb/notes/codify-versus-llm-decision-heuristics.md:120 → kb/notes/ephemeral-computation-prevents-accumulation.md` | `OP/contested` | `explained-by/high` | `explained-by/medium` | `explained-by/medium` | `explained-by` | unanimous | `candidate-new` |
| F048 | `kb/notes/llm-context-is-composed-without-scoping.md:72 → kb/notes/instruction-specificity-should-match-loading-frequency.md` | `OTHER/contested` | `see-also/medium` | `see-also/medium` | `evidenced-by/medium` | `see-also` | **contested** | `candidate-delta` |
| F050 | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → kb/notes/verifiability-gradient.md` | `EX/contested` | `exemplifies/high` | `exemplifies/high` | `exemplifies/medium` | `exemplifies` | unanimous | `authorized` |
| F051 | `kb/notes/definitions/reach-assessment.md:66 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | `OTHER/unanimous` | `extends/high` | `extends/medium` | `extends/high` | `extends` | unanimous | `authorized` |
| F052 | `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:84 → kb/notes/oracle-strength-spectrum.md` | `EX/contested` | `explained-by/high` | `explained-by/high` | `premised-on/high` | `explained-by` | **contested** | `candidate-new` |
| F053 | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:49 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | `OP/contested` | `extends/high` | `exemplifies/high` | `exemplifies/medium` | `exemplifies` | **contested** | `authorized` |
| F057 | `kb/notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → kb/notes/frontloading-spares-execution-context.md` | `OP/contested` | `extends/medium` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F062 | `kb/notes/task-fitted-structure-costs-cross-task-reuse.md:71 → kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md` | `OTHER/unanimous` | `extends/medium` | `extends/medium` | `extends/high` | `extends` | unanimous | `authorized` |
| F063 | `kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | `EX/contested` | `explained-by/medium` | `premised-on/medium` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| F066 | `kb/notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md:72 → kb/notes/oracle-strength-spectrum.md` | `OTHER/unanimous` | `is-evidence-for/high` | `is-evidence-for/medium` | `is-evidence-for/medium` | `is-evidence-for` | unanimous | `candidate-delta` |
| F071 | `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | `EX/contested` | `explained-by/high` | `explained-by/high` | `operates-through/high` | `explained-by` | **contested** | `candidate-new` |
| F080 | `kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` | `OTHER/contested` | `premised-on/medium` | `extends/high` | `contrasts/medium` | `UNSTABLE` | **UNSTABLE** | `—` |
| F086 | `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:59 → kb/notes/definitions/constraining.md` | `OP/contested` | `defined-in/high` | `defined-in/high` | `defined-in/high` | `defined-in` | unanimous | `authorized` |
| F088 | `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:44 → kb/notes/process-structure-and-output-structure-are-independent-levers.md` | `OTHER/contested` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F092 | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | `EN/contested` | `exemplifies/high` | `exemplifies/high` | `exemplifies/high` | `exemplifies` | unanimous | `authorized` |
| F094 | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | `EN/unanimous` | `prerequisite-hold/medium` | `explained-by/medium` | `prerequisite-hold/high` | `prerequisite-hold` | **contested** | `deferred-family` |
| F095 | `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:61 → kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md` | `OTHER/unanimous` | `evidenced-by/medium` | `extends/high` | `contrasts/medium` | `UNSTABLE` | **UNSTABLE** | `—` |
| F102 | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:59 → kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` | `OTHER/contested` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F103 | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:50 → kb/notes/definitions/codification.md` | `OTHER/unanimous` | `defined-in/high` | `defined-in/high` | `defined-in/high` | `defined-in` | unanimous | `authorized` |
| F104 | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → kb/notes/ephemeral-computation-prevents-accumulation.md` | `OP/contested` | `explained-by/high` | `explained-by/high` | `operates-through/high` | `explained-by` | **contested** | `candidate-new` |
| F107 | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | `EN/unanimous` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F111 | `kb/notes/reflective-coverage-is-graded-across-representational-forms.md:100 → kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md` | `OP/contested` | `evidenced-by/medium` | `evidenced-by/medium` | `evidenced-by/high` | `evidenced-by` | unanimous | `authorized` |
| F112 | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:54 → kb/notes/verifiability-gradient.md` | `OTHER/unanimous` | `exemplifies/high` | `exemplifies/medium` | `exemplifies/medium` | `exemplifies` | unanimous | `authorized` |
| F113 | `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:62 → kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` | `OTHER/unanimous` | `see-also/medium` | `other:reframed-in/medium` | `other:developed-by/medium` | `UNSTABLE` | **UNSTABLE** | `—` |
| F115 | `kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md:46 → kb/notes/spec-mining-as-codification.md` | `UNSTABLE/unstable` | `rests-on/high` | `rests-on/high` | `rests-on/high` | `rests-on` | unanimous | `authorized` |
| F116 | `kb/notes/bounded-context-orchestration-model.md:90 → kb/notes/frontloading-spares-execution-context.md` | `OP/contested` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| F119 | `kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → kb/notes/frontloading-spares-execution-context.md` | `OP/contested` | `exemplifies/high` | `operates-through/high` | `explained-by/high` | `UNSTABLE` | **UNSTABLE** | `—` |
| F122 | `kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md:61 → kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md` | `OTHER/unanimous` | `contrasts/high` | `extends/high` | `contrasts/high` | `contrasts` | **contested** | `authorized` |

## Non-unanimous diagnostics

Every contested and unstable row is repeated here with all three justifications. The vote TSV retains the fuller reader-need, revision-consequence, and boundary-test record.

### F013 — explained-by (contested)

`kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:58 → kb/notes/axes-of-artifact-analysis.md`

- A — `extends/medium`: The source argues reusable checks require declared classes and invokes mixed consumption and authority paths; the target supplies storage, form, lineage, and behavioral-authority fields for classifying those paths.
- B — `explained-by/medium`: The source argues that reusable checks need a declared class and identifies mixed consumption paths as the hard case; the target explains that the same stored object can act through different paths and that form and authority determine review evidence, supplying the account for that hard case.
- C — `explained-by/high`: The source argues that reusable verification is unwarranted until artifacts belong to a declared class and invokes mixed consumption paths; the target shows that identical stored bytes can have different forms, authority paths, and review evidence, supplying the account of why classification must precede reusable checking.

### F026 — exemplifies (contested)

`kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md`

- A — `is-evidence-for/high`: The source reports stance drift after a contaminating verdict entered flat context despite explicit detection and refusal; the target identifies contamination as the failure produced when flat context composition lacks scoping or isolation.
- B — `exemplifies/high`: The source reports a blind controlled case where contaminated writers showed directional fine-grained drift despite detection and refusal; the target states the general claim that composition without scoping or isolation produces contamination.
- C — `exemplifies/medium`: The source reports directional stance drift despite detection and refusal; the target classifies information left live in a flat unisolated substrate as the contamination mode of uncoordinated composition.

### F030 — UNSTABLE

`kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:64 → kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`

- A — `operates-through/high`: The source locates unsafe ephemerality where resolutions must survive across contexts and says codification commits them; the target describes codification as extracting and fixing regularities in artifacts, with relaxing when that commitment encodes a proxy theory.
- B — `see-also/medium`: The source locates durability pressure where an operational resolution must transfer across runs, users, or audits; the target locates codification fitness in spec completeness and the risk that scale exposes a proxy theory, making it a useful adjacent companion rather than a dependency.
- C — `premised-on/medium`: The source locates durability pressure where operational resolutions transfer across contexts and says codification commits them; the target supplies the theory of codification as a commitment whose payoff depends on exact-spec versus proxy-theory regime.

### F031 — explained-by (contested)

`kb/notes/design-for-the-first-time-human-except-on-access-cost.md:26 → kb/notes/feasibility-is-the-heaviest-forks-net-load.md`

- A — `see-also/medium`: The source distinguishes linear from sublinear access and proposes consumer-specific query materializations; the target models decomposed feasibility by residual fork load and names preselection and navigation as ways to shed irrelevant bodies.
- B — `explained-by/medium`: The source argues that agents pay linear context cost for whole artifacts and proposes scoped query materializations; the target explains fork feasibility through residual volume, complexity, and interference and explicitly shows preselection shedding irrelevant bodies.
- C — `explained-by/high`: The source contrasts linear whole-artifact loading with sublinear slice access, while the target explains feasibility as the largest residual fork load and identifies preselection and navigation as ways to shed that load.

### F032 — explained-by (contested)

`kb/notes/reflection-buys-addressability.md:68 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md`

- A — `evidenced-by/high`: The source presents selective revision and related benefits as expected consequences of addressability, while the target limits those benefits to sparse edits in a matching decomposition with an explicit, small impact closure.
- B — `explained-by/medium`: The source makes selective revision and related benefits expectations of addressable retention; the target explains their materialization by requiring a pre-existing matching decomposition plus a small explicit impact closure and supplies the dense-change boundary.
- C — `explained-by/high`: The source makes retained commitments inspectable and lists selective revision and related benefits as expected advantages; the target supplies the missing account that edits and validation stay local only under sparse change in matching units with a small explicit dependency closure.

### F035 — UNSTABLE

`kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → kb/notes/bounded-context-orchestration-model.md`

- A — `premised-on/high`: The source explicitly casts compiled workflow control as codifying next-call selection in a bounded-context model; the target formalizes that control as select over explicit state followed by bounded calls.
- B — `extends/high`: The target formalizes orchestration as a symbolic scheduler selecting bounded calls from explicit state; the source takes that decomposition, compiles the selection strategy into an executable artifact, and derives the further result that primitive channels stay fixed while aggregate reachable effect expands.
- C — `operates-through/medium`: The source describes moving call-A-then-B selection from repeated inference into an external script while effects still pass through delegated agents and tools; the target formalizes that same path as symbolic select over K followed by bounded calls whose results return to K.

### F040 — explained-by (contested)

`kb/notes/retrieval-failure-is-reflection-failure.md:40 → kb/notes/stale-indexes-are-worse-than-no-indexes.md`

- A — `operates-through/high`: The source treats discovery as the causal wire from retained artifacts to behavior and singles out trusted membership gaps; the target shows that no index falls back to current search whereas a stale index satisfies navigation and makes omitted notes invisible.
- B — `explained-by/high`: The source places discovery inside the reflective causal connection and identifies trusted incomplete membership as its sharpest break; the target explains the asymmetry directly: no index triggers current search, while a stale index appears exhaustive and causes the reader to stop looking.
- C — `explained-by/high`: The source places discovery inside the causal connection from retained self-representation to behavior; the target explains that an apparently exhaustive index satisfies the navigation need and stops the search that could have found omitted members.

### F043 — see-also (contested)

`kb/notes/bounded-context-orchestration-model.md:97 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md`

- A — `see-also/medium`: The source separates full symbolic state K from the bounded prompt selected for a call, while the target separates a narrowed methodology fast path from an accessible fuller theory fallback; their analogy is useful but neither artifact establishes the other's mechanism.
- B — `see-also/medium`: The source keeps full symbolic state K outside bounded calls and selects task-facing prompts from it; the target instead retains a theory as live fallback beside a durable theory-derived methodology, making the two neighboring full-versus-shaped-layer patterns useful but not identical.
- C — `other:exemplified-by/medium`: Here exemplified-by means that the target is a worked instance of the source's general model: the source keeps full explicit state K outside bounded calls and selects task-facing prompts, while the target keeps fuller theory available behind a cheaper derived methodology layer for out-of-coverage fallback.

### F048 — see-also (contested)

`kb/notes/llm-context-is-composed-without-scoping.md:72 → kb/notes/instruction-specificity-should-match-loading-frequency.md`

- A — `see-also/medium`: The source argues that concatenated tokens are globally visible and that real boundaries must be imposed outside the model; the target offers an always-loaded versus on-demand instruction hierarchy that limits exposure without creating within-window scope.
- B — `see-also/medium`: The source shows that all loaded tokens share one unscoped attention field and says boundaries must be imposed outside it; the target supplies the useful neighboring rule that universal instructions load always while task-specific instructions load on demand.
- C — `evidenced-by/medium`: The source argues natural-language context has no enforced local scope and must be bounded externally; the target describes always-loaded routers plus on-demand skill bodies and task documents that impose such loading boundaries.

### F052 — explained-by (contested)

`kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:84 → kb/notes/oracle-strength-spectrum.md`

- A — `explained-by/high`: The source makes verification one of four constraints pruning objective choice and orders descriptive, prescriptive, and theoretical profiles by judge strength; the target explains the hard-to-no-oracle gradient and why weak discrimination limits automated verification and generator-verifier designs.
- B — `explained-by/high`: The source makes verification one of four constraints that turn KB objective choice into engineering and differentiates profile judges by oracle strength; the target supplies the hard, soft, interactive, delayed, and no-oracle account and explains the consequences of hardening that gradient.
- C — `premised-on/high`: The source treats verifiability as one of four inherited constraints and ranks descriptive, prescriptive, and theoretical profiles by their available judges; the target provides the oracle-strength spectrum on which those rankings depend.

### F053 — exemplifies (contested)

`kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:49 → kb/notes/deploy-time-learning-is-the-missing-middle.md`

- A — `extends/high`: The source proposes promoting recurring tested select fragments while leaving task state ephemeral; the target defines deploy-time learning as durable, inspectable system-definition change across sessions and describes reversible movement toward code.
- B — `exemplifies/high`: The source proposes retaining tested recurring select fragments in a durable library while discarding task state; the target defines deploy-time learning as durable, inspectable system-definition artifacts updated across sessions during deployment.
- C — `exemplifies/medium`: The source proposes promoting recurring tested select fragments into a durable repository while leaving run state ephemeral; the target defines cross-session artifact updates during deployment as the missing learning timescale.

### F063 — explained-by (contested)

`kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

- A — `explained-by/medium`: The source says directives, uncompressed reflection, and process checks preserve the condition clause needed for safe abstraction; the target distinguishes diagnostic evidence from selection scores and shows that trace access lets an outer-loop proposer search through causes rather than outcomes alone.
- B — `premised-on/medium`: The source requires a condition clause before turning an episode into a rule and says directive, inspectable failure evidence carries that boundary; the target distinguishes selection scores from diagnostic evidence and shows why traces and drill-down surfaces support causal hypothesis formation.
- C — `explained-by/high`: The source makes boundary-statability the test for safe abstraction and identifies directive and process evidence as boundary carriers; the target explains that traces, diffs, and tool state support causal hypothesis formation whereas scores alone mainly select winners.

### F071 — explained-by (contested)

`kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`

- A — `explained-by/high`: The source argues that weakly discriminated qualities drift and proposes combining genuinely discriminating, differently failing checks; the target explains that amplification works only with TPR above FPR and sufficiently decorrelated errors.
- B — `explained-by/high`: The source proposes heterogeneous checks to strengthen weak quality oracles and warns that repeated correlated review amplifies blind spots; the target explains this with the TPR-FPR gap and decorrelated-error requirements and quantifies the amplification cost.
- C — `operates-through/high`: The source proposes combining maintainability and KB-quality signals only when they discriminate and fail differently; the target specifies error correction by above-chance checks with decorrelated errors as the process that amplifies such weak signals rather than merely multiplying a shared blind spot.

### F080 — UNSTABLE

`kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`

- A — `premised-on/medium`: The source limits itself to remembered artifacts and places capture, activation, lifecycle, and governance around its quality triad; the target argues that full memory systems cross storage, context activation, and learning machinery.
- B — `extends/high`: The target argues that memory is crosscutting machinery distributed over storage, context engineering, and learning; the source explicitly narrows from that whole system to remembered material and develops a three-property artifact-quality basis while placing the target's machinery around it.
- C — `contrasts/medium`: The source deliberately limits itself to the quality of remembered material and places capture, activation, and governance around that basis; the target analyzes the broader system as storage, retrieval or activation, and learning distributed across runtime concerns.

### F094 — prerequisite-hold (contested)

`kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

- A — `prerequisite-hold/medium`: The source distinguishes outcome checks from checks over intermediate steps and requires the latter for rule abstraction; the target shows that scores select winners while traces and structured evidence expose the mechanisms needed for explanation.
- B — `explained-by/medium`: The source separates replay licensed by a final-outcome pass from rule abstraction licensed by inspecting the route; the target independently separates selection signals from diagnostic traces and explains that only the richer evidence exposes mechanisms rather than merely identifying what won.
- C — `prerequisite-hold/high`: The source says process verification distinguishes a transferable mechanism from a coincidental correct result by inspecting intermediate steps; the target shows that scores can select winners without explanation while traces and structured drill-down surfaces expose the mechanism needed for that inspection.

### F095 — UNSTABLE

`kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:61 → kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`

- A — `evidenced-by/medium`: The source characterizes dynamic workflows as model-authored compiled coordination while analyzing their primitive and aggregate authority; the target documents the concrete RLM case in which a model writes Python orchestration over recursive sub-agent calls for symbolic execution.
- B — `extends/high`: The target explains how RLM has a model emit ephemeral REPL orchestration over sub-agents; the source develops that distinction into compiled persistent coordination and derives the further result that primitive channels stay fixed while aggregate effect volume expands.
- C — `contrasts/medium`: The source analyzes reusable external coordination that escapes a single-context envelope and expands aggregate authority; the target describes the same model-authored symbolic sub-agent orchestration but emphasizes that its REPL code is discarded after each run.

### F104 — explained-by (contested)

`kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → kb/notes/ephemeral-computation-prevents-accumulation.md`

- A — `explained-by/high`: The source compares task-local RLM artifacts with Tendril's durable capabilities and names their governance and reuse consequences; the target derives those same consequences from ephemeral generation-execution-discard versus accumulation.
- B — `explained-by/high`: The source contrasts discarded RLM orchestration with Tendril's retained capabilities and assigns reuse and lifecycle consequences to that boundary; the target explains those consequences as ephemerality's exchange of accumulation, testing, review, and reuse for a clean slate.
- C — `operates-through/high`: The source places standard and typed-combinator RLM variants at a per-task boundary because their orchestration state is discarded, while Tendril keeps generated tools; the target describes that exact generate, execute, discard process and its no-reuse and no-governance consequences.

### F113 — UNSTABLE

`kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:62 → kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md`

- A — `see-also/medium`: The source argues that naming a discovered structure makes later recognition cheap; the target uses that argument as one of two mechanisms for defining a minimum viable vocabulary, making it a useful downstream companion rather than a premise of the source.
- B — `other:reframed-in/medium`: reframed-in means that the target recasts a source subclaim in a new analytic frame without making the source depend on the target; here the source argues that naming a discovered structure amortizes later recognition, and the target uses that mechanism to formulate minimum vocabulary as maximal extraction-cost reduction for a bounded observer.
- C — `other:developed-by/medium`: The source argues that naming a newly conjectured structure amortizes recognition cost for later instances; the target explicitly takes that result as one of two mechanisms and develops it into a smallest-name-set objective for reducing a bounded observer's extraction cost.

### F119 — UNSTABLE

`kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → kb/notes/frontloading-spares-execution-context.md`

- A — `exemplifies/high`: The source describes resolving paths and settings before the first agent message, while the target defines frontloading as computing already-known instruction inputs before the consuming call to spare execution context.
- B — `operates-through/high`: The source's configuration surface resolves paths, settings, and environment-specific values before first use, while the target specifies frontloading as computing known instruction inputs before the consuming call and inserting the result to spare runtime context.
- C — `explained-by/high`: The source describes build-time or session-start resolution of paths, settings, and environment-specific values before the agent sees them; the target explains how precomputing known inputs and inserting their results spares the later call's discovery, indirection, and reasoning context.

### F122 — contrasts (contested)

`kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md:61 → kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`

- A — `contrasts/high`: The source walks outbound links and compares git modification times to flag possible staleness before a reader encounters it; the target captures staleness noticed during traversal and defers repair through a log.
- B — `extends/high`: The target describes stale references as one class of defect noticed during ordinary traversal and captured for a later pass; the source starts from that happenstance detection path and adds link-graph plus git-time scanning so review can be prompted before traversal encounters the stale note.
- C — `contrasts/high`: The source proposes dependency-aware timestamp review because staleness is currently found only when a note is reread; the target describes that neighboring traversal-time path, where an agent notices stale references during another task and logs them for a later pass.

## Agent synthesis for the unstable rows

The six three-way rows have no aggregate recommendation. After the vote freeze, the takeover agent read all twelve endpoint artifacts and compared the three proposed reader needs and revision consequences. The following are adjudication recommendations, not extra votes and not a reclassification of the unstable result:

| ID | recommendation | why this boundary wins | authorization impact |
|---|---|---|---|
| F030 | `remove` | The target's codify/relax boundary is only adjacent context: rejecting it would not reopen the source's explanatory-reach criterion and the target is not the process producing that criterion. Under the maintainer's no-`see-also` policy, the edge does not earn a formal successor. | `not-applicable` |
| F035 | `extends` | The source takes the target's select/call orchestration model and develops the further compiled-authority result; the target is a model being extended, not the literal runtime path of the source claim. | `authorized` |
| F080 | `contrasts` | The source deliberately isolates artifact-quality requirements while the target describes the whole crosscutting memory system; the useful traversal is the neighboring-scope distinction, not a truth premise. | `authorized` |
| F095 | `evidenced-by` | The target is a concrete RLM case showing ephemeral symbolic orchestration, which bears on the source's general claim about compiling coordination without becoming the argument it extends. | `authorized` |
| F113 | `remove` | The target develops the source's naming-amortizes-discovery observation into an observer-relative optimization, but one site does not justify a new `developed-by` identifier. Under the maintainer's no-`see-also` policy, the weak formal edge is removed. | `not-applicable` |
| F119 | `exemplifies` | Configuration injection in the source is a concrete instance of the target's general frontloading pattern: known values are resolved before the consuming call. | `authorized` |

This synthesis settles the six rows without inventing another identifier. Together with the stable-row decision, the current 129-row surface contains 66 `explained-by`, 32 `operates-through`, 27 other exact dispositions, and 4 removals. `F094` is one of the 27 dispositions but remains a prerequisite hold rather than a migration label. No row is unresolved.

## Recorded maintainer decision

The maintainer accepted the recommendation with one explicit policy change: **drop the link wherever the proposed exact successor is `see-also`.** The resulting 42-row decision is:

- accept 34 of the 36 stable exact-majority recommendations as written;
- keep `F094` as `prerequisite-hold`;
- override stable `see-also` rows `F043` and `F048` to `remove`;
- accept synthesis recommendations `F035` → `extends`, `F080` → `contrasts`, `F095` → `evidenced-by`, and `F119` → `exemplifies`;
- set synthesis rows `F030` and `F113` to `remove` instead of `see-also`.

This explicitly adjudicates all 42 rows. It does not authorize their contract or corpus implementation, and it establishes no new notes→notes `see-also` pairing.

The independent choices remain visible as evidence behind the overrides:

| ID | independent choices | decision needed |
|---|---|---|
| F030 | `operates-through` / `see-also` / `premised-on` | choose one exact disposition, `connective-prose`, or `remove` |
| F035 | `premised-on` / `extends` / `operates-through` | choose one exact disposition, `connective-prose`, or `remove` |
| F080 | `premised-on` / `extends` / `contrasts` | choose one exact disposition, `connective-prose`, or `remove` |
| F095 | `evidenced-by` / `extends` / `contrasts` | choose one exact disposition, `connective-prose`, or `remove` |
| F113 | `see-also` / `other:reframed-in` / `other:developed-by` | choose one exact disposition, `connective-prose`, or `remove` |
| F119 | `exemplifies` / `operates-through` / `explained-by` | choose one exact disposition, `connective-prose`, or `remove` |

The authorized next step is the exact source→destination pairing audit and a proposed catalogue/contract/ADR/migration packet; implementation remains separately gated.
