---
type: kb/sources/types/ingest-report.md
description: "FALSIFYBENCH links negative testing to semantic rule recovery under deliberately narrow initial hypotheses; it measures within-game revision, not persistent theory learning."
source: https://arxiv.org/abs/2606.04751
captured: "2026-09-19"
ingested: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 560e8e012ef675b7e0d8daf04ee7b1825c022ee8477784b496ccaf800fc3c04f
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
learning_claims: true
domains: [learning-theory, hypothesis-testing, evaluation]
---

# Ingest: FALSIFYBENCH rule-discovery games

## Classification

Scientific paper by Leonardo Bertolazzi, Katya Tentori, and Raffaella Bernardi, affiliated with the University of Trento and the Free University of Bozen-Bolzano. The retained observation is the full June 2026 arXiv v1 paper, including methods, prompts, statistical analysis, and example traces. Its contribution is an empirical benchmark and process analysis, grounded explicitly in Wason's task and Klayman and Ha's account of testing strategies.

## Summary

[FALSIFYBENCH](https://arxiv.org/abs/2606.04751) evaluates twelve LLMs on 100 semantic rule-discovery games each. Players propose test triples or guesses, receive feedback, and retain their interaction history for up to twenty turns. Each model also supplies its own stateless oracle through separate calls. Games use five curated WordNet target categories, with initial examples drawn from narrower descendants to encourage overly specific hypotheses. Within this construction, greater positive testing correlates with lower success across models (Spearman ρ = −0.779); the best reported success rate is 75%. Turn-level analysis distinguishes testing intent from actual falsification and associates failures with partially overlapping, disjoint, or surface-linguistic hypotheses. Crucially, positive tests can refute an overly broad hypothesis: the paper's negative-testing result is specific to the dominant overly narrow case. It measures discovery behavior inside a supplied game, without testing a persistent learning architecture or a causal intervention that prescribes negative testing.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the Popper-grounded learning question, this source supplies a bounded empirical case of explicit conjectures, self-selected probes, and feedback-driven revision. It sharpens the existing caution in [the sample-efficiency conjecture](../notes/retained-theories-may-improve-sample-efficiency.md): the full methods establish that the benchmark deliberately encourages hypotheses narrower than the target, so the negative-testing association concerns informative exploration under that construction. It does not test retained-theory reuse across a shift, nor establish that an epistemic commitment caused better performance.

The paper also supplies a process-level example for [known-target discovery benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md). Hypothesis-target relations and conclusive falsifications reveal more than final recovery alone, while the authored target and semantic-equivalence oracle still determine success. The result therefore adds evidence about reaching a known target without closing the problem of judging unknown scientific contributions.

## Learning Claims (our opinion)

The player learns within an episode by carrying forward its proposed hypotheses, actions, and oracle responses in conversation history. It can change a natural-language hypothesis, choose new items, or submit a guess; an incorrect guess also provides rejection feedback. Test-strategy annotations are for later analysis and do not teach the player. The oracle receives only the current judgment inputs, and a separate offline GPT-5-Mini annotator classifies hypothesis-target set relations.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), the player is unclassified, and condition 2 (consumption) decides it. Hypotheses are explicit natural-language statements whose changes of category or scope can be inspected (condition 1). Condition 2 (consumption) is unestablished: the experiment does not show that the declared hypothesis mediates the next decision. Semantic membership supplies consequences that tests can contradict, and traces show revision following informative tests, which meets condition 3 at the strength of those traces. Condition 4 (iteration) is met where a revision follows a test: test results stay in the conversation and shape the next hypothesis. Persistence is at the lowest grade, within one game; the benchmark measures no cross-game retention. Learning is a separate claim that the benchmark does not test; selective repair and preservation of useful prior knowledge are also left unisolated. The testing machinery is not revised, and no weight updates are part of the reported mechanism.

The epistemic contribution is narrower than endorsing a complete Popperian learning paradigm. The source's stated lineage is Wason and Klayman and Ha, rather than a direct implementation of Popper's philosophy. Its useful distinction is between seeking an example outside the current hypothesis and obtaining evidence that contradicts that hypothesis. For a hypothesis narrower than the target, an outside example accepted by the oracle refutes the hypothesized boundary; an outside example rejected by the oracle does not. For an overly broad hypothesis, a positive test rejected by the oracle can instead refute it. Thus attempted criticism, successful error detection, and productive revision need separate measurements.

The [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters here. Players can propose arbitrary strings, including non-taxonomic hypotheses; they are not restricted to choosing WordNet nodes. Nevertheless, the experiment fixes semantic membership as feedback, triple testing and guessing as actions, the target categories, the turn limit, and oracle acceptance as closure. Better play inside that arrangement does not compare alternative feedback, theory representations, retention policies, or acceptance criteria. Success shows episode-level adaptation toward the supplied target, not a general advantage for this decomposition.

## Extractable Value

- **[quick-win] Scope criticism by the hypothesis-target relation.** The full text resolves the existing sample-efficiency note's uncertainty about benchmark construction: initial examples deliberately encourage overly narrow hypotheses. Negative testing is particularly informative there, whereas positive testing can refute overly broad hypotheses. This is a reusable qualification for claims about falsification-seeking behavior, not evidence of persistent learning.
- **[experiment] Measure criticism at separate stages.** Record the declared hypothesis, selected probe, expected response, observed response, resulting contradiction, and subsequent revision. FALSIFYBENCH distinguishes intended test direction from conclusive falsification, showing how a benchmark can inspect part of the conjecture–criticism–revision pathway instead of scoring only final answers. Extending that measurement to retained-theory reuse would be a new experiment.
- **[just-a-reference] Preserve the bounded quantitative result.** Across twelve models and 1,200 games under the fixed semantic-game design, positive-testing frequency negatively correlates with success and with conclusive falsification (the latter ρ = −0.937). These are useful reference observations about active testing under predominantly narrow hypotheses; neither comparison manipulates epistemic commitments or retention.

## Limitations (our opinion)

The paper's language of a primary driver exceeds what the observational comparisons isolate. Models vary in training, scale, reasoning configuration, and provider settings. Testing strategy is measured during the same games whose success it predicts; model quality and evolving game difficulty can affect both. A regression with a model random effect and an oracle-error covariate does not substitute for a matched strategy intervention.

Oracle reliability remains a consequential measurement boundary. Each model plays against itself through separate calls; human checks cover only one Test and one Guess turn per game. The resulting binary error flag cannot establish that errors elsewhere in the trajectory are inconsequential. The reported lack of a credible independent oracle-error association should not be generalized to perfect-oracle equivalence. Hypothesis-target relation labels additionally depend on an offline LLM, and surface-feature classifications use regex heuristics. These readouts are useful proxies rather than independently established semantic ground truth for every turn.

The five curated, English-centric semantic categories and deliberately narrow initial examples make the test favorable to upward category revision. Target recovery is not explanatory progress in an open scientific domain. The benchmark does not compare negative testing with a matched information-gain policy, or show that a philosophical stance explains performance beyond useful probe selection. It also supplies no controlled persistence, transfer, or forgetting test. The full paper was analyzed, but its released code was not inspected or executed here; reported outcomes have not been independently reproduced.

## Recommended Next Action

Update the FALSIFYBENCH discussion in [the sample-efficiency conjecture](../notes/retained-theories-may-improve-sample-efficiency.md) using this full-text observation, replacing uncertainty about construction with the explicit narrow-hypothesis design while preserving the distinction from causal strategy interventions and retained-theory reuse.
