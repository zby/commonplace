---
description: "Frozen small-model falsification operators show limited selection gains; extraction recovery supplies a bounded positive and separates search coverage from criticism."
type: kb/sources/types/ingest-report.md
source: https://arxiv.org/abs/2606.16999
captured: "2026-09-19"
ingested: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: eea89382b3ddfab28253c8de8a078ab52e8ea8d1c8bbae6293a6369d8bb3dd8a
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
domains: [learning-theory, code-generation, falsification, evaluation]
learning_claims: true
---

# Ingest: Selection Without Signal, Recovery Through Expression

## Classification

Scientific paper: Mehmet İşcan, affiliated with PythaLab and Yıldız Technical University, reports a measurement study of post-hoc code-generation operators. The captured work is arXiv v1, dated 15 June 2026. Its evidential contribution is controlled operator comparisons, executable test outcomes, and finite-sample analysis; affiliation and philosophical motivation do not independently establish its conclusions.

## Summary

The paper tests whether executable falsification, selection, verification, repair, and related operators improve frozen small code models beyond a first-public-test-passer Best-of-N baseline. Across its twenty-six-operator survey, no semantic operator establishes the targeted accuracy improvement at matched generation budgets; external consensus-selection comparisons retain this negative on HumanEval+ and MBPP+ across three model cells. Within those fixed generators, tests, and candidate budgets, the diagnostics distinguish absent correct candidates from weak usable discrimination among candidates that already pass public tests. The strongest positive changes the extraction boundary: robust extraction and public-test function-name alignment recover code already emitted by DeepSeek-Coder-1.3B, adding 12/164 HumanEval+ and 33/370 MBPP+ successes with zero observed harm. A separate early-stop policy saves 19.1% of a full eight-sample run on one local cell, with zero observed harm against full-budget consensus at a threshold selected on the evaluation set. These are evidence about a particular implementation regime, not a general refutation of falsification or a demonstration of persistent learning.

## Quotes

No source quotes have been retained yet.

## Connections Found

For assessing a Popper-grounded learning paradigm, this source is a limiting case for implementation choices. It supplies bounded evidence for [the separation of search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): a selector cannot recover a correct program absent from its admissible pool, and stronger criticism need not widen that pool. The paper measures that boundary under frozen generators and finite sample budgets; it does not exercise the note's retention requirement. M1's positive sharpens the distinction: broadening what the harness accepts can recover existing correct code without improving the model's semantic revision ability. Neither result establishes what happens when a persistent learner changes its generator, tests, or revision procedures across tasks.

## Learning Claims (our opinion)

The source's Popperian commitment is to expose candidates to attempted refutation rather than count agreement as sufficient support. Its implementation translates candidates into executable programs, criticism into tests or behavioral probes, and revision into bounded model calls. Some probes use candidate agreement as a surrogate expected output; that is a fallible implementation choice, not an independent falsifier merely because execution is deterministic. Hidden tests supply the experimenter's assessment, while deployment generally receives prompts and public tests. Learned verifier and router experiments also use hidden-correctness labels in offline fitting or replay, so their evidence channels differ from those of a selector operating only on a fresh pool.

Relative to [theory refinement](../notes/definitions/theory-refinement.md), code repair can instantiate a local revision of an addressable conjecture: execution exposes a failure and a model edits a program. Pure selection uses conjectures without revising them, and extraction recovery changes their usable expression. The paper does not demonstrate that successful criticism produces retained theories or procedures consumed on later tasks. Frozen generator weights alone would not preclude persistent learning through external artifacts; the missing evidence is a cross-task retention-and-reuse path, not simply a lack of weight updates. Accordingly, this is primarily an evaluation of local search and correction operations, with some offline fitted components, rather than evidence for a recurrent theory-refinement learner.

The important constraint is the [effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Selectors operate on supplied candidate pools; repair methods draw from the same frozen generator under a bounded call budget; public tests and hand-designed probes constrain what errors can guide deployment. The nulls show limits of the tested compound configurations, not that all useful distinctions are mathematically absent from the prompt and code. M1 varies one consequential boundary—the conversion from raw response to runnable program—and succeeds especially where the standard extractor loses many candidates. This supports measuring representation losses separately from reasoning failures. It does not establish that this decomposition is best for learning, or require a revision of Commonplace's definition of theory refinement.

## Extractable Value

- [quick-win] **Empirical boundary on criticism without adequate search.** Retain the study as evidence for the existing search/evaluation distinction: 16 of 30 hard tasks still lack a hidden-correct candidate at sampling depth 16. This is a finite-budget observation about frozen small models, not proof that future sampling or a different generator cannot solve them. It limits what one should infer from adding a refutation stage to a learning architecture.
- [experiment] **Measure harness losses before attributing gains to learning.** M1 adds 12 and 33 successes on the two external suites for DeepSeek-Coder-1.3B by recovering emitted code and aligning its function name to public tests. Qwen gains are only one to four tasks and non-significant. A KB experiment could separately count usable candidates lost during parsing, candidates absent from generation, and incorrect acceptance; the paper establishes the usefulness of this separation for code generation, not its prevalence in KB work.
- [quick-win] **Keep the tested control attached to an effect.** ACE's 19.1% saving compares against generating all eight samples, while its zero observed harm compares against full-budget consensus. It is not a demonstrated saving over a sequential first-public-passer implementation, and threshold selection lacks a held-out calibration split or multiplicity correction. This is a reusable warning when evaluating the cost of a criticism loop.
- [just-a-reference] **Zero observed harm has a sample-dependent scope.** For independent Bernoulli harm trials, zero harms require at least 45 observations to place a 90% one-sided upper confidence bound at 5%. The parameters and independence assumption belong with this result; 45 is not a universal minimum experiment size.

## Limitations (our opinion)

The twenty-six-method survey does not establish that every leakage-free selector fails. External replication directly compares consensus selection with Best-of-N, not every surveyed operator on every cell. Some external pools retain oracle headroom of 6–17 tasks that the tested consensus selector does not significantly exploit. Failure of that selector is weaker than proof that no deployment-accessible signal can exploit it. The consensus-trap lemma additionally assumes majority symmetry; its reasoning about the majority must not silently equate majority selection with the first-public-passer baseline.

The coverage and discrimination mechanisms are plausible, measured explanations of local failures, but their strongest rhetoric exceeds the comparisons. Ten of twelve hidden failures evade the tested sound metamorphic relations; that does not establish invisibility to every sound relation. Sixteen unsolved tasks at depth sixteen do not prove a permanent coverage ceiling. Model families, small parameter counts, finite Python-function benchmarks, fixed public-test filtering, and the eight-sample default bound reuse. The MBPP+ count excludes eight tasks rejected by the determinism/serialization gate.

Matching generator-call counts is narrower than matching total compute: execution probes, embeddings, repairs of different lengths, and serving costs can differ. A few methods use hidden outcomes or known-good references for training or diagnostic contrasts. Their deployment claims must be distinguished from those oracle-assisted analyses. The report derives from the paper; no implementation was inspected or experiment reproduced here.

M1 preserves standard public-passing outputs, which explains its safety under the benchmark's success conditions; its gains remain relative to the particular standard extractor. They are not newly synthesized program logic. ACE does not share an unconditional do-no-harm property: aggressive thresholds produce observed harm, and the selected threshold's reported bound is not corrected for threshold search. The paper acknowledges this later despite earlier language describing both survivors as safe by construction.

Finally, the study tests operator performance, not philosophical commitments in isolation. Its negative neither rejects Popper's epistemology nor compares persistent Popper-grounded learning with alternative learning paradigms. A deterministic oracle computes consequences of supplied tests; the adequacy of those tests, candidate generation, diagnosis, and retention remain separate design questions.

## Recommended Next Action

Update [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) with this finite-pool code-generation example under its search-range claim, preserving the frozen-generator and finite-budget scope and explicitly excluding any demonstrated cross-task retention.

---

Relevant Notes:

- [Original paper](https://arxiv.org/abs/2606.16999) — derived-from: primary source for the reported experiment and its statistical qualifications
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — is-evidence-for: finite-pool coverage constrains selection independently of evaluation strength
