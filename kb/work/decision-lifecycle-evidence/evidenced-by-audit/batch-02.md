# evidenced-by audit — batch_02 (34 files, all kb/notes/)

66 `evidenced-by` edges, all footer lines. Non-edge prose mentions of the word: 0.

| class | count |
|---|---|
| CORROB-OK | 4 |
| QUALIFY | 42 |
| CORROB-UNTESTED | 2 |
| ORIGIN | 12 |
| MISLABEL | 6 |
| **total** | **66** |

Dates were checked only for the three ADR edges: each ADR predates its note (ADR 004 2026-03-13 vs note 2026-08-24; ADR 020 2026-04-20 vs 2026-06-12; ADR 025 2026-06-09 vs 2026-08-24).

## Non-QUALIFY edges

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| kb/notes/false-positive-generation-is-filtered-before-retention.md:70 | notes/maintenance-capacity-must-match-harmful-artifact-inflow.md | MISLABEL | Target is a theory note that states the general capacity pathology the body invokes ("exactly the pathology in"). It is not an observation. | `extends: the capacity failure that automated search produces when evaluation cannot neutralize the harmful candidates it admits` |
| kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:56 | sources/causal-inference-using-invariant-prediction.ingest.md | ORIGIN | The note's causal-route account (line 18) is built from this source's invariance procedure. The source does not test the note's claim. | `abstracted-from: invariance across environments and interventions as a causal acceptance signal` |
| kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:58 | sources/towards-causal-representation-learning.ingest.md | ORIGIN | The note quotes this source as the premise that causal models reach beyond one distribution (line 16). The source supplied the premise; it did not test the claim. | `abstracted-from: causal models support intervention and counterfactual generalization beyond one observed distribution` |
| kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:59 | sources/causal-learn-causal-discovery-in-python.ingest.md | ORIGIN | The body cites the library as an instance of causal discovery under declared assumptions. It is a source case for the generalization, not a test. | `abstracted-from: causal discovery under explicit method assumptions` |
| kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:60 | sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md | ORIGIN | The body cites DoWhy as an instance that "makes the same boundary operational." It is a source case for the generalization, not a test. | `abstracted-from: assumption declaration and partial validation` |
| kb/notes/human-analogies-suggest-functions-not-component-boundaries.md:27 | notes/llm-learning-phases-fall-between-human-learning-modes.md | MISLABEL | Target is a theory note whose claim supplies this note's premise. It is not an observation. | `grounds: human learning categories fail to preserve their boundaries across LLM training and context use` |
| kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes.md:31 | Lampinen et al. (external URL) | ORIGIN | The shared-failure-mode premise ("content effects") is taken from this study. The study's test was of LLM content effects, not of this note's transfer claim, and "empirical demonstration" asserts confirmation. External URLs cannot take `abstracted-from`. | Ingest the paper into kb/sources/ and use `abstracted-from: the three-task content-effects study this note's shared-failure-mode premise is built on; Wason divergence bounds the transfer`. Without ingest, use `evidenced-by: the three-task content-effects study this note's shared-failure-mode premise is built on; Wason divergence bounds the transfer` |
| kb/notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md:42 | reference/adr/020-theoretical-default-contrasts-mechanism.md | ORIGIN | The ADR predates the note and records the forward-canonical design decision that the note generalizes. | `abstracted-from: the directional-asymmetry decision rests on forward edges being canonical and the inverse view computed` |
| kb/notes/increasing-computational-autonomy-relocates-human-effort.md:67 | notes/evidence/commonplace-as-a-reflective-system.md | ORIGIN | The phrase says this system "motivated the pattern," and line 51 says the pattern is "stated from" it. The target is a note, so `abstracted-from` is not allowed. | `evidenced-by: the human-inclusive system this pattern was first stated from; its growing computational allocation alongside continued human involvement is the originating observation, not a test` |
| kb/notes/increasing-computational-autonomy-relocates-human-effort.md:70 | Bainbridge, Ironies of Automation (external PDF) | ORIGIN | Line 51 says the pattern is stated from this industrial precedent. The precedent is an origin, not a test of the claim for self-improving systems. | Ingest the paper into kb/sources/ and use `abstracted-from: the industrial precedent this pattern generalizes — automation leaves the operator the residue the designer could not automate`. Without ingest, use `evidenced-by: the industrial precedent the pattern was generalized from; it bounds the claim to role transformation, not to self-improving systems` |
| kb/notes/index-completeness-does-not-determine-editorial-orientation.md:44 | reference/adr/004-replace-areas-with-tags.md | ORIGIN | The ADR (2026-03) predates the note (2026-08). The note says the design "embeds this distinction," so the note reads its claim out of the design. | `abstracted-from: the generated-tail design architecturally separates the two kinds of index value this note distinguishes` |
| kb/notes/information-value-is-observer-relative.md:70 | notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md | MISLABEL | Target is a theory note about recognition cost. The body applies observer-relativity to it. It is not an observation. | `extends: recognition cost varies with the observer's vocabulary and tools, and with the depth of what must be recognized` |
| kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md:72 | sources/machine-studying.ingest.md | ORIGIN | The phrase says the source "supplies the changed-agent formulation," so the note takes its formulation from this source. | `abstracted-from: supplies the changed-agent formulation and the bounded low-budget repository-map result` |
| kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:83 | sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md | CORROB-OK | The phrase names a measured discovery-versus-interaction split that could have tracked together. Timing and independence are not stated. | Optional: append `; an external experiment not designed around this note's distinction` |
| kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:85 | sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md | CORROB-OK | The phrase names causal perturbations that could have shown equal dependence, and it states the scope limits. | None needed; optionally add an independence note |
| kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:86 | sources/tulving-pearlstone-availability-versus-accessibility.ingest.md | CORROB-OK | The phrase names a cued-recall test of the storage-to-retrieval distinction, which predates the note by decades, and scopes out the context-to-action step. | None |
| kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:88 | sources/verbalizable-representations-global-workspace-llms.ingest.md | CORROB-OK | The phrase names controlled causal-routing tasks that could have shown the information routing through J-space. | Optional: append `; an independent interpretability study` |
| kb/notes/llm-frameworks-should-keep-the-tool-loop-optional.md:76 | preprints.org agent-harness survey (external) | CORROB-UNTESTED | "Independently … converging" asserts confirmation. A survey's list of components is not a test the should-keep-optional claim could have failed. | `evidenced-by: an independently written survey that also names lifecycle hooks as a first-class harness component; this is convergent framing, not a test of the claim that the middle layer is needed` |
| kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:66 | Sutton, The Bitter Lesson (external) | MISLABEL | The quoted passage is the premise and the text the note interprets. It is not an observation. | `grounds: the meta-methods passage quoted in the body — build in the meta-methods, not the discoveries` |
| kb/notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md:44 | notes/evidence/commonplace-as-a-reflective-system.md | ORIGIN | The body calls these episodes the "direct evidence base." The note's two paths (boundary movement and cross-form feedback) are generalized from them. The target is a note, so `abstracted-from` is not allowed. | `evidenced-by: the codification crossing and the symbolic-feedback episode this note's two paths were generalized from; they illustrate the paths but do not test the coverage requirement` |
| kb/notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md:45 | instructions/review-gates/frontmatter/claim-strength.md | MISLABEL | Target is a review-gate instruction, not an observation. The observation is the witness episode, and the phrase says "showing." Pointing at the gate also cannot be `evidenced-by` from this collection. | `see-also: the claim-strength gate that passed the analytic title in the witness episode` |
| kb/notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md:46 | sources/combinatorial-sketching-finite-programs.ingest.md | MISLABEL | SKETCH is the honest contrast case: its specification sits outside the revise step. It is not evidence for the drift claim. | `contrasts: an exact propose-and-counterexample loop stays honest because the specification is outside the revise step and "no completion" is a reportable outcome` |
| kb/notes/open-domain-memory-retention-needs-a-declared-output-spec.md:47 | agent-memory-systems/agentic-memory-systems-comparative-review.md | CORROB-UNTESTED | The phrase says "corroborates," but the camp classification is a Commonplace survey that does not report a test the split could have failed. The classification may have been made with this note's lens. | `evidenced-by: the automatic-capture-and-push versus curated-pull-only camps across 148 reviewed systems illustrate the input-driven/output-driven split at aggregate scale; the survey was not designed as a test of the split` |
| kb/notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md:75 | reference/adr/025-complete-generated-indexes-are-build-time-only.md | ORIGIN | The ADR (2026-06) predates the note (2026-08). It is the design case the segmentation point is read from, not a test. | `abstracted-from: one maintained metadata source can supply generated and query-time access paths without making both canonical` |

## QUALIFY edges (fine as is)

- kb/notes/evolving-understanding-needs-holistic-rewrite-not-composition.md:63 → x.com/augmentcode (What spec-driven development gets wrong)
- kb/notes/exact-implementation-does-not-validate-a-requirement.md:58 → sources/lessons-from-building-ai-agents-for-financial-services.ingest.md
- kb/notes/exact-implementation-does-not-validate-a-requirement.md:59 → sources/meyerson-maker-million-step-llm-zero-errors.ingest.md
- kb/notes/exact-implementation-does-not-validate-a-requirement.md:60 → sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md
- kb/notes/exact-implementation-does-not-validate-a-requirement.md:61 → sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md
- kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md:57 → sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md
- kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md:59 → deming.org Moen PDSA history
- kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:55 → sources/goedel-machines-schmidhuber.ingest.md
- kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:57 → sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md
- kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:61 → agentic-systems/reviews/eigenius.md
- kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:62 → sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md
- kb/notes/frontloading-spares-execution-context.md:58 → sources/machine-studying.ingest.md
- kb/notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md:62 → sources/efficiently-intertwining-widening-narrowing.ingest.md
- kb/notes/history-has-one-chance-to-become-checkable.md:39 → sources/prov-overview.ingest.md
- kb/notes/history-has-one-chance-to-become-checkable.md:40 → sources/in-toto-farm-to-table-guarantees.ingest.md
- kb/notes/improvements-can-accumulate-without-compounding.md:56 → notes/evidence/commonplace-as-a-reflective-system.md
- kb/notes/increasing-computational-autonomy-relocates-human-effort.md:68 → reference/tag-readme-trace-as-self-improving-loop.md
- kb/notes/increasing-computational-autonomy-relocates-human-effort.md:71 → x.com/frgx Figma security review thread
- kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md:45 → x.com/molt_cornelius (Notes Without Reasons)
- kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md:73 → sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md
- kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md:74 → sources/monkey-patch.ingest.md
- kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md:75 → sources/fast-properties-in-v8.ingest.md
- kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md:76 → sources/erlang-release-handling.ingest.md
- kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:81 → x.com/KatanaLarp (the bug that shipped)
- kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:82 → sources/the-second-brain-trap-2041486539067154753.ingest.md
- kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:84 → sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md
- kb/notes/knowledge-storage-does-not-imply-contextual-activation.md:87 → sources/gick-holyoak-analogical-problem-solving.ingest.md
- kb/notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md:54 → giants-insights.github.io
- kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md:58 → sources/co-harness-co-evolving-harness-and-model-weights.ingest.md
- kb/notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md:49 → sources/lessons-from-building-ai-agents-for-financial-services.ingest.md
- kb/notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md:50 → notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md
- kb/notes/link-following-and-search-impose-different-metadata-requirements.md:57 → sources/teevan-perfect-search-engine-orienteering.ingest.md
- kb/notes/llm-frameworks-should-keep-the-tool-loop-optional.md:77 → x.com/mfpiccolo (iii harness)
- kb/notes/llm-frameworks-should-keep-the-tool-loop-optional.md:79 → agentic-systems/reviews/claude-code-dynamic-workflows.md
- kb/notes/llm-output-deviation-requires-three-way-diagnosis.md:83 → sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md
- kb/notes/llm-output-deviation-requires-three-way-diagnosis.md:84 → notes/context-contamination-operates-below-an-agents-compliance-reasoning.md
- kb/notes/maintenance-capacity-must-match-harmful-artifact-inflow.md:36 → reference/where-change-candidates-come-from-in-commonplace.md
- kb/notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:34 → reference/where-change-candidates-come-from-in-commonplace.md
- kb/notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md:19 → notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md
- kb/notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md:46 → sources/knowledge-centric-self-improvement-2607.19592.ingest.md
- kb/notes/natural-language-project-state-specializes-search-heuristics.md:56 → notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
- kb/notes/oracle-strength-spectrum.md:84 → openai.com Harness Engineering (Lopopolo)

## Borderline calls

- The Lopopolo edge (oracle-strength-spectrum:84), the GIANTS edge (known-target:54), and the seven-documentation-cases edge (linked-note:50) may also be origins. They stay QUALIFY because their phrases assert no confirmation.
- The four instantiation "attests" edges (MOP, monkey patch, V8, Erlang) are likely source cases too. They stay QUALIFY for the same reason.
