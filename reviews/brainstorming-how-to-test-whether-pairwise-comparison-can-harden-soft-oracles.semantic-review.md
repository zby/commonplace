<!-- REVIEW-METADATA
note-path: kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md
last-full-review-note-sha: 4153e0186b9fd1dfa17415ad22a7f890cdb08b87
last-full-review-note-commit: 328009802f9033ab971afc8a1f0918d052115c52
last-full-review-at: 2026-03-23T21:56:08+01:00
last-accepted-note-sha: 4153e0186b9fd1dfa17415ad22a7f890cdb08b87
last-accepted-note-commit: 328009802f9033ab971afc8a1f0918d052115c52
last-accepted-at: 2026-03-23T21:56:08+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md ===

Claims identified: 14

### Claims extracted

1. **[Intro]** Pairwise comparison is "still only a hypothesis" — it needs a test design that can "distinguish genuine oracle hardening from mere prompt reformulation."
2. **[What would count as "hardening"]** Hardening requires improvement in at least one of: discrimination, variance, optimization utility, bias behavior. Four-item enumeration presented as exhaustive ("at least one of these should improve").
3. **[The simplest test is not enough]** Evaluator comfort is not the point; the resulting signal must support selection and improvement better than scalar scoring.
4. **[The simplest test is not enough]** The test plan should climb a three-rung ladder: judgment quality, ranking quality, loop-improvement quality.
5. **[Test 1]** Judgment quality can be measured by agreement with human pairwise labels, run-to-run variance, position bias rate, and intransitivity rate. Four measures enumerated.
6. **[Test 1]** "If pairwise judgment does not beat scalar judgment here, there is no strong reason to spend more effort on ranking or loop-level tests." — gate claim.
7. **[Test 2]** Ranking quality is a separate test from judgment quality because "pairwise comparison might work locally while still producing unstable or misleading global rankings."
8. **[Test 3]** Optimization-loop value is "the test that decides whether pairwise comparison is actually useful in context engineering."
9. **[Good benchmark choices]** Enumeration of four promising and two poor benchmark candidates, with the scope claim that benchmarks should be "hard enough that absolute scoring is noisy, but bounded enough that human adjudication remains feasible."
10. **[Failure modes]** Five false positives enumerated that the experiment must rule out.
11. **[What would falsify]** Five outcomes that should count against the thesis.
12. **[The easiest high-value experiment]** A concrete 20-30 prompt, 4-candidate design is proposed as the cheapest useful first experiment.
13. **[Intro]** The Koylan source "suggests a plausible mechanism: in open-ended tasks, asking a judge 'which of these two outputs is better?' may be easier and more stable than asking 'score this output 1-5.'" — attribution to the source.
14. **[Test 1]** Position-swapping "as recommended in Agent Skills for Context Engineering" — attribution to that source.

---

WARN:
- **[Completeness]** The four-item "hardening" enumeration (discrimination, variance, optimization utility, bias behavior) omits **cost-efficiency** as an independent dimension. A pairwise oracle that achieves equal discrimination but at far lower cost per unit of signal would also count as hardening on the oracle-strength-spectrum (moving the "cheaply" axis in "how cheaply and reliably you can check whether output is correct"). The note later discusses cost under "failure modes" (cost masking) and Test 3 measures (improvement per unit judge cost), but the top-level definition of hardening does not include it. A reader using the four-item list as a gate could dismiss a cost-efficient oracle as "just changing the judge's interface."
- **[Completeness]** The five falsification conditions are structured as a conjunction ("if most of these happen"), but individual conditions have very different diagnostic weight. Condition 5 ("gains disappear once prompts are rewritten or models are swapped") tests generalizability, not the core pairwise-vs-scalar comparison. Pairwise could genuinely harden the oracle for a given model and prompt family while failing to transfer. The note treats all five as roughly equivalent evidence against the thesis, but conditions 1-4 falsify the mechanism while condition 5 falsifies only the scope. Lumping them under "most of these" risks premature dismissal if 3 out of 5 fail but the core three (stability, agreement, ranking) hold.

INFO:
- **[Completeness]** The three-rung ladder (judgment quality, ranking quality, loop-improvement quality) is presented as strictly ordered: "each step asks a stricter question than the one before it." A boundary case challenges this strict ordering: a pairwise judge might perform poorly on isolated pair judgments (Test 1 fails) while still producing useful rankings via round-robin aggregation (Test 2 passes), if systematic biases cancel in aggregation. The ladder structure assumes signal quality composes monotonically, but aggregation can be more forgiving than individual judgment. The note could acknowledge this by noting that the gate at Test 1 is a heuristic, not a proof of futility for Test 2.
- **[Completeness]** The failure-modes enumeration lists five false positives but omits **non-transitivity masking** as a distinct failure mode, though the note discusses intransitivity elsewhere (Test 1 measures, Test 2 narrative). The "tournament illusion" item (item 5) is close but focuses on false confidence in rankings, not on the possibility that non-transitivity itself could be a feature rather than a bug (cyclic preferences might reflect genuine multidimensional quality where no single ranking exists). This is a conceptual boundary case: the experiment framework assumes a single ground-truth ranking exists, which may not hold for sufficiently open-ended tasks.
- **[Grounding alignment]** The note attributes to the Koylan source the claim that "asking a judge 'which of these two outputs is better?' may be easier and more stable than asking 'score this output 1-5.'" The ingest summary confirms this is a fair characterization of Koylan's argument. However, the ingest's Limitations section explicitly notes that "the post is a conceptual extrapolation, not evidence" and that "pairwise form does not automatically solve the oracle problem." The brainstorming note correctly frames this as "still only a hypothesis," so the hedge is present, but the note never surfaces the ingest's specific concern that discriminative power and decorrelation (the properties error-correction requires) are not measured by the source. This is not a misattribution — it is an omission of a relevant caveat already documented in the KB.
- **[Grounding alignment]** The note references "position-swapping as recommended in Agent Skills for Context Engineering." The Agent Skills note does recommend "swap positions twice in pairwise comparison, check consistency" in its Evaluation Methodology section. The attribution is accurate. However, the brainstorming note describes this as an optional enhancement ("optionally with position-swapping"), whereas the Agent Skills note frames it as a standard practice for bias mitigation. The downgrade from standard practice to optional could lead a reader to skip the mitigation in Test 1, which would then fail to measure position bias properly.
- **[Internal consistency]** The note says the easiest first experiment should "avoid pretending we already have a mature autonomous loop," yet the overall test plan culminates in Test 3, which requires exactly such a loop. The note is internally consistent (the easy experiment is explicitly a first pass, not the whole plan), but the "good first pass" framing could obscure the fact that the strongest evidence (Test 3) requires infrastructure the KB does not yet have. This is a pragmatic tension, not a contradiction.

PASS:
- **[Internal consistency]** The note's definition of hardening (improvement in discrimination, variance, optimization utility, or bias behavior) is consistently applied across all three tests. Test 1 measures discrimination and variance, Test 2 measures ranking fidelity (a form of discrimination at the set level), and Test 3 measures optimization utility. No section uses "hardening" in a way that drifts from the top-level definition.
- **[Internal consistency]** The falsification conditions are logically consistent with the success criteria. Each falsification condition corresponds to a negation of one of the hardening dimensions or a generalizability concern. No falsification condition contradicts the success criteria.
- **[Grounding alignment]** The link to oracle-strength-spectrum is described as "extends: turns that note's abstract oracle-hardening question into a concrete experimental program." The oracle-strength-spectrum note does propose "harden the oracle" as the primary engineering move and lists "preference pairs" as an interactive-oracle example. The brainstorming note genuinely extends this by designing tests for that specific mechanism. The relationship semantics are accurate.
- **[Grounding alignment]** The link to error-correction-works-above-chance-oracles-with-decorrelated-checks is described as "qualifies: asks whether pairwise comparison improves the base signal before amplification, rather than replacing amplification." The error-correction note establishes that amplification requires TPR > FPR and decorrelation. The brainstorming note's Test 1 effectively asks whether pairwise comparison improves the base TPR-FPR gap. The "qualifies" relationship is accurate — the brainstorming note does not claim pairwise replaces amplification; it tests whether it improves the input to amplification.
- **[Grounding alignment]** The link to quality-signals-for-kb-evaluation is described as "parallel: another brainstorming note about manufacturing better soft oracles, but at KB-wide rather than candidate-ranking scope." The quality-signals note indeed addresses oracle manufacturing through composite signals at the KB level. The parallel relationship holds: both notes address oracle hardening through different mechanisms at different scales.
- **[Completeness]** The good/poor benchmark selection criteria ("hard enough that absolute scoring is noisy, but bounded enough that human adjudication remains feasible") is well-calibrated. The four promising candidates all plausibly satisfy both constraints; the two poor candidates are excluded for clear, distinct reasons (hard oracle already exists; no adjudicable difference). No obvious candidate type is missing from this enumeration.

Overall: 2 warnings, 5 info
===
