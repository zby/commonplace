# evidenced-by audit — batch 03

34 files; 66 footer `evidenced-by` edges in 33 files; 0 inline labelled uses; 0 prose-only mentions of the word.

| class | count |
|---|---|
| CORROB-OK | 1 |
| CORROB-UNTESTED | 9 |
| ORIGIN | 17 |
| MISLABEL | 3 |
| QUALIFY | 36 |
| **total** | **66** |

Paths are under `kb/notes/`. Dates are from `git log --follow` (first add) and were checked only where they decide timing.

## Non-QUALIFY edges

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| orchestration-needs-privilege-quarantine-not-permission-scope.md:41 | agentic-systems/reviews/gbrain-garrytan.md | CORROB-UNTESTED | The phrase asserts independent convergence but does not name the risk. The review (2026-09-24) came after the note (2026-07-07), so this edge could be upgraded to real corroboration. | `evidenced-by: recorded after this note and independently of it, GBrain could have relied on per-call scope for agent callers but instead classifies every remote caller, including the host agent, as untrusted at the API boundary` |
| orchestration-strategies-and-run-state-have-opposite-persistence.md:54 | agentic-systems/reviews/claude-code-dynamic-workflows.md | CORROB-UNTESTED | The body says it "partially confirms the prediction". The review (2026-06-12) came after the note (2026-05-29), but the phrase states neither the risk nor the timing. | `evidenced-by: recorded after the prediction (review 2026-06-12, note 2026-05-29), the prediction could have failed if no shipped harness promoted model-authored orchestrators; Claude Code saves them as /commands, but only coarsely and by hand, with no test gate or fragment-level split` |
| parametric-reproduction-cannot-replace-an-authoritative-record.md:47 | sources/we-should-take-text-optimization-more-seriously.ingest.md | CORROB-UNTESTED | "Argues the same routing" presents a concurring argument as evidence, but an argument is not a test. | `see-also: argues a parallel routing — stable repeated information toward weights, volatile auditable information in text` |
| pointer-design-tradeoffs-in-progressive-disclosure.md:76 | agent-memory-systems/reviews/openviking.md | CORROB-UNTESTED | "Shows" asserts support. The target is really an existence witness that the pointer categories can coexist, and the phrase does not say so. | `evidenced-by: existence witness — one code-inspected system combines fixed L0/L1 sidecars with ranked, reranked query-time selection, so the categories are not rival architectures` |
| scheduler-llm-separation-exploits-an-error-correction-asymmetry.md:79 | rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md | CORROB-UNTESTED | The target is a note, not an observation. The phrase asserts that LLMs "delegate" as if this were a finding. | `evidenced-by: limit case — the model writes whole recursive programs, yet the REPL still runs the call stack; an illustration, not a test` (or `extends` if the RLM note should be read as developing the argument) |
| scheduler-llm-separation-exploits-an-error-correction-asymmetry.md:80 | https://arxiv.org/abs/2606.10662 (DeLM) | CORROB-UNTESTED | "Supports" asserts corroboration, while the body calls DeLM "a layered instance rather than a clean test". | `evidenced-by: layered instance — queue and visibility mechanics are symbolic, while decomposition and semantic admission are model-mediated; the OOLONG hybrid is consistent with moving exact aggregation into code but does not isolate the separation causally`; retarget to `../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md` |
| scheduler-llm-separation-exploits-an-error-correction-asymmetry.md:87 | https://xinmingtu.cn/... (Tu 2026) | CORROB-UNTESTED | "Supports", even though the phrase itself hedges. A formal analysis is an argument, not a test. | `evidenced-by: an independent formal argument for separating global coordination from bounded leaf-level reasoning; it does not test the three-phenomena account`; retarget to `../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md` |
| solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md:44 | sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md | CORROB-UNTESTED | The body says CSP search "tests the same rule". The source was grounded on 2026-08-28, after the rule (2026-03-07), but the phrase names neither the test nor the timing. | `evidenced-by: added after the rule (2026-08-28 grounding), the rule could have lost to static ordering on binary CSP benchmarks; MRV beat static orders in every reported test except enumerating all n-Queens solutions; fail-first is a rival explanation, and hard-to-reverse commitments are not covered` |
| task-families-and-product-families-classify-different-things.md:87 | sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md | CORROB-UNTESTED | "Shows why" presents a survey's explanation as support. The target reports no test. | `evidenced-by: qualifies — the survey explains why initial examples or natural-language instructions may need later interaction to discriminate intended behavior` |
| psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md:102 | flat-memory-predicts-specific-cross-contamination-failures-that-are.md | MISLABEL | The target is a prediction note ("testable via an observation protocol"), not an observation. Both the edge and the body (line 28, "documents this") treat a prediction as documented evidence. | `grounds: supplies the predicted search-pollution failure mode that principles 1 and 2 address (a prediction, not yet an observation)`; also soften "documents this" at line 28 |
| specific-intent-may-out-yield-local-rationales-facts-stay-separate.md:55 | a-bare-writing-prompt-does-not-determine-its-intended-contribution.md | MISLABEL | The target is a sibling claim note that supplies a premise, not an observation. | `grounds: supplies the premise that topic and output form do not recover the intended contribution` |
| structured-output-is-easier-for-humans-to-review.md:23 | https://owl.purdue.edu/... (Toulmin, Purdue OWL) | MISLABEL | The phrase itself calls Toulmin the "theoretical basis". It is a theory source the claim is built on, not evidence. | `abstracted-from: Toulmin's separation of grounds from warrant, from which this note draws the Evidence/Reasoning split`; retarget to `../sources/purdue-owl-toulmin-argument.ingest.md` |
| readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:52 | agent-memory-systems/reviews/meta-harness.md | ORIGIN | The review (2026-04-16) predates the note (2026-04-17) by one day, and the phrase "showing a readable-artifact loop in practice" marks it as the case the claim was built from. | `abstracted-from: a code-inspected system where a fixed-weight proposer mutates harness code and context/memory logic from raw traces` |
| rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md:37 | https://x.com/neural_avb/... | ORIGIN | The phrase says "that this note abstracts". | `abstracted-from: practitioner walkthrough of the REPL mechanism, symbolic variable return, and scaffold-level truncation`; retarget to `../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md` and drop the duplicate inline "(ingest)" link |
| rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:49 | sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md | ORIGIN | This note is a comparison built from the RLM variants, Tendril, and llm-do (see its title and description), so the compared systems are its origin. | `abstracted-from: λ-RLM keeps prompt-as-environment recursion but replaces model-authored code with a deterministic, typed combinator runtime; post-return persistence is unspecified` |
| rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:51 | agent-memory-systems/reviews/tendril.md | ORIGIN | Tendril is one of the compared systems. | `abstracted-from: source-inspected generated-capability system at the cross-session workspace persistence point` |
| rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:56 | sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md | ORIGIN | The RLM case in the comparison comes from this source. | `abstracted-from: practitioner walkthrough of RLM's REPL mechanism, within-execution variable persistence, and symbolic variable return; post-return lifecycle and sub-call API unspecified` |
| rule-based-context-selection-needs-a-pre-existing-signal.md:30 | agent-memory-systems/agentic-memory-systems-comparative-review.md | ORIGIN | The target is the observed pattern ("the push/pull split this mechanism explains") that the mechanism was built to explain. | `abstracted-from: the cross-system push/pull split this mechanism explains` |
| runtime-structure-determines-governance-control-surfaces.md:59 | reference/review-architecture.md | ORIGIN | The worked matrix's substrate/context-engine cells are drawn from Commonplace's shipped review subsystem. The reference doc is the source of that case, not a test of the claim. | `abstracted-from: the shipped review subsystem supplies the substrate/context-engine governance cells of the worked matrix` |
| semantic-work-can-be-relocated-but-not-eliminated.md:22 | frontloading-spares-execution-context.md | ORIGIN | The general rule was generalized from this sibling note ("instantiates this rule"). The target is a note, so `abstracted-from` is not allowed. | `extends: develops the time-axis case — pre-compute where inputs are known`; the frontloading note may add a reverse `exemplifies` edge |
| semantic-work-can-be-relocated-but-not-eliminated.md:24 | rule-based-context-selection-needs-a-pre-existing-signal.md | ORIGIN | Same pattern as line 22: an instance note that the rule generalizes. | `extends: develops the context-selection case, where the pre-existing signal is semantic work already paid upstream` |
| superseded-choices-are-retained-superseded-beliefs-are-not.md:114 | reference/types/adr.md | ORIGIN | The claim generalizes an established append-only ADR practice. The type spec realizes the rule and is not an observation that tests it. | `abstracted-from: the append-only decision-record contract preserves the choice event and alternatives after the prescription loses authority` (use `see-also` if the note was not built from ADR practice) |
| synthesis-is-not-error-correction.md:67 | https://arxiv.org/pdf/2512.08296 (Kim et al.) | ORIGIN | The note exists to reconcile Kim et al. with MAKER (line 12, "The concrete case"). | `abstracted-from: 17.2× error amplification with synthesis-only Independent topology vs 4.4× with centralized verification`; retarget to `../sources/towards-a-science-of-scaling-agent-systems.ingest.md` |
| synthesis-is-not-error-correction.md:68 | https://arxiv.org/abs/2511.09030 (MAKER) | ORIGIN | This is the other half of the reconciled pair. | `abstracted-from: zero errors over 1M steps with first-to-ahead-by-k voting, maximal decomposition, and decorrelation`; retarget to `../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md` |
| the-boundary-of-automation-is-the-boundary-of-verification.md:58 | https://x.com/amytam01/... (Tam) | ORIGIN | The note is a synthesis from five converging sources (line 12), which it admits are "not fully independent". | `abstracted-from: labor-economics argument that engineering automates (hard oracle) while research taste resists (no oracle)`; retarget to `../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md` |
| the-boundary-of-automation-is-the-boundary-of-verification.md:59 | https://www.dwarkesh.com/p/dario-amodei-2 | ORIGIN | This is a synthesis input; per the body, the oracle reading is "our interpretation". | `abstracted-from: the confidence split across domains, read here as tracking oracle strength`; retarget to `../sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md` |
| the-boundary-of-automation-is-the-boundary-of-verification.md:60 | https://www.usenix.org/... (in-toto) | ORIGIN | This is a synthesis input. | `abstracted-from: supply-chain trust becomes automatable once the chain is signed, hash-checkable metadata`; retarget to `../sources/in-toto-farm-to-table-guarantees.ingest.md` |
| the-boundary-of-automation-is-the-boundary-of-verification.md:61 | Bainbridge PDF | ORIGIN | "Independent arrival" describes independence from other authors, not from how this note was built: Bainbridge is one of the five synthesis inputs and predates the claim. | `abstracted-from: the monitoring irony — a human cannot verify in real time a system installed because it outperforms the human`; retarget to `../sources/ironies-of-automation.ingest.md` |
| the-boundary-of-automation-is-the-boundary-of-verification.md:62 | https://arxiv.org/pdf/2602.16666 (Rabanser) | ORIGIN | This is a synthesis input, and the body notes that the oracle notes already cite it. | `abstracted-from: calibration improves while discrimination trends are mixed across benchmarks`; retarget to `../sources/towards-a-science-of-ai-agent-reliability.ingest.md` |
| pointer-design-tradeoffs-in-progressive-disclosure.md:77 | sources/tombros-sanderson-query-biased-summaries.ingest.md | CORROB-OK | The phrase names a controlled comparison against a static-summary baseline that the query-time branch could have lost, and states its limits. It does not state timing (prior published work). | Optional: add "prior work, not an input to the taxonomy" if that is true |

## QUALIFY edges

- out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md:44 → sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md
- parametric-reproduction-cannot-replace-an-authoritative-record.md:43 → agent-memory-systems/reviews/agent-r.md
- parametric-reproduction-cannot-replace-an-authoritative-record.md:44 → agent-memory-systems/reviews/KBLaM.md
- parametric-reproduction-cannot-replace-an-authoritative-record.md:45 → sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md
- parametric-reproduction-cannot-replace-an-authoritative-record.md:46 → agentic-systems/reviews/exo.md
- process-structure-and-output-structure-are-independent-levers.md:50 → https://arxiv.org/html/2603.01896v2
- process-structure-and-output-structure-are-independent-levers.md:52 → sources/verbalizable-representations-global-workspace-llms.ingest.md
- program-theory-sustains-search-under-delayed-feedback.md:196 → evidence/commonplace-revision-used-theory-guided-computational-search.md (upgrade candidate: the evidence is dated 2026-08-30, the note 2026-08-29)
- readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:53 → https://yoonholee.com/meta-harness/paper.pdf
- reflection-buys-addressability.md:85 → sources/ashby-design-for-a-brain-ultrastability.md
- reflective-coverage-is-graded-across-representational-forms.md:100 → evidence/commonplace-as-a-reflective-system.md
- retained-artifacts-enable-persistent-deployment-time-adaptation.md:57 → sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md
- retained-artifacts-enable-persistent-deployment-time-adaptation.md:58 → sources/machine-studying.ingest.md
- retained-theories-may-improve-sample-efficiency.md:241 → sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md
- retained-theories-may-improve-sample-efficiency.md:242 → sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md
- retained-theories-may-improve-sample-efficiency.md:243 → sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md
- retained-theories-may-improve-sample-efficiency.md:244 → sources/concept-bottleneck-models-paper-v3.ingest.md
- retained-theories-may-improve-sample-efficiency.md:245 → sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md
- retained-theories-may-improve-sample-efficiency.md:246 → sources/in-search-of-lost-domain-generalization.ingest.md
- retained-theories-may-improve-sample-efficiency.md:247 → sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md
- reverse-compression-is-when-llm-output-expands-without-adding.md:45 → sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md
- revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md:52 → sources/concept-bottleneck-models-paper-v3.ingest.md
- revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md:54 → sources/language-models-dont-always-say-what-they-think.ingest.md
- revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md:55 → https://arxiv.org/html/2601.22436v3
- rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:57 → agentic-systems/reviews/claude-code-dynamic-workflows.md
- self-improvement-is-relative-to-a-declared-objective.md:65 → sources/ashby-design-for-a-brain-ultrastability.md
- solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md:45 → sources/chaff-engineering-an-efficient-sat-solver.ingest.md
- stale-self-description-conceals-its-own-staleness.md:73 → agentic-systems/reviews/exo.md
- structured-prompt-gains-do-not-establish-distribution-selection.md:40 → sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md
- structured-prompt-gains-do-not-establish-distribution-selection.md:41 → sources/agentic-code-reasoning.ingest.md
- structured-prompt-gains-do-not-establish-distribution-selection.md:42 → sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md
- structure-inference-needs-capture-at-the-decision-surface.md:48 → agent-memory-systems/lightweight/trajectory-informed-memory-generation.md
- systematic-prompt-variation-serves-verification-and-diagnosis-not.md:68 → https://arxiv.org/pdf/2509.13680
- the-bitter-lesson-selects-production-methods-not-representational.md:96 → https://arxiv.org/pdf/2406.18532
- the-bitter-lesson-selects-production-methods-not-representational.md:97 → https://arxiv.org/pdf/2603.18743
- the-bitter-lesson-selects-production-methods-not-representational.md:98 → https://arxiv.org/pdf/2607.22688

## Side observations (outside the classification)

- Several QUALIFY edges point at external URLs that already have an ingest. They could be retargeted:
  - process-structure:50 → `agentic-code-reasoning.ingest.md`
  - readable-artifact:53 → `meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md`; its link text says "Ingest:" but the link points to the PDF
  - revision-guided:55 → `llm-agents-are-not-always-faithful-self-evolvers.ingest.md`
  - systematic-prompt-variation:68 → `prompt-stability-code-llms-emotion-personality-variations.ingest.md`
  - bitter-lesson:96–98 → `symbolic-learning-enables-self-evolving-agents`, `memento-skills-let-agents-design-agents`, `co-harness-co-evolving-harness-and-model-weights` ingests
- Two edges could be upgraded to genuine corroboration because the evidence postdates the claim: orchestration-strategies:54 (listed above) and program-theory:196 (evidence dated 2026-08-30, note dated 2026-08-29; currently QUALIFY).
