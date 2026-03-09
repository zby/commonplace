---
source_snapshot: towards-a-science-of-ai-agent-reliability.md
ingested: 2026-03-09
type: scientific-paper
domains: [agent-reliability, evaluation-methodology, safety-engineering, deployment-governance]
---

# Ingest: Towards a Science of AI Agent Reliability

Source: towards-a-science-of-ai-agent-reliability.md
Captured: 2026-02-25
From: https://arxiv.org/pdf/2602.16666

## Classification
Type: scientific-paper -- Princeton preprint with formal metric definitions, cross-domain survey of safety-critical engineering (aviation, nuclear, automotive), systematic evaluation of 14 models across two benchmarks (GAIA, tau-bench), multi-run protocols with fault injection and prompt perturbation. Structured as a proper empirical study with methodology, experimental results, and stated limitations.
Domains: agent-reliability, evaluation-methodology, safety-engineering, deployment-governance
Author: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan (Princeton University). Narayanan is a well-known voice on AI accountability and measurement methodology; Kapoor co-authored influential work on AI evaluation pitfalls. This team has credibility on "how we measure AI systems" questions.

## Summary

The paper argues that mean task success rate is an inadequate measure for deployed AI agents and proposes a four-dimensional reliability framework grounded in safety-critical engineering: consistency (repeatable outcomes across runs), robustness (stability under perturbations), predictability (calibrated confidence), and safety (bounded harm severity). Evaluating 14 models from OpenAI, Google, and Anthropic over 18 months of releases, they find that capability gains have far outpaced reliability gains. Key empirical findings: outcome consistency remains low across all models; prompt robustness is the weakest robustness dimension (models handle real infrastructure faults better than paraphrased instructions); calibration has improved but discrimination has not; larger models are sometimes less consistent than smaller ones because they have more solution strategies; and safety is deliberately excluded from the aggregate reliability score and reported as a hard constraint, because averaging would obscure tail risks.

## Connections Found

The source connects deeply into the KB's learning theory and oracle verification stack. The primary synthesis note -- [reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) -- was written in direct response to this paper and maps the four reliability dimensions onto oracle-hardening moves. That note is the main hub connecting this source into the knowledge graph.

Eight connections identified:

1. **[reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md)** -- grounds: this source provides the four-dimension framework that the note maps onto oracle hardening; the empirical finding that reliability lags capability is the oracle-strength prediction confirmed at scale.

2. **[oracle-strength-spectrum](../notes/oracle-strength-spectrum.md)** -- grounds: "reliability is independent of capability" is direct empirical support for oracle strength as the bottleneck, not compute or model scale.

3. **[softening-signals](../notes/softening-signals.md)** -- grounds: R_prompt operationalises brittleness-under-paraphrase as a quantitative metric at scale. The counterintuitive finding (models handle real faults but break under rephrasings) is the softening signal pattern confirmed across 14 models.

4. **[error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)** -- extends: the discrimination finding (calibration improves but discrimination does not) constrains error correction -- models are getting better at aggregate confidence but not at distinguishing individual correct from incorrect outputs, limiting amplification via voting.

5. **[spec-mining-as-crystallisation](../notes/spec-mining-as-crystallisation.md)** -- exemplifies: Table 3's mapping of real-world agent failures to reliability metrics is spec mining applied to evaluation itself -- each failure class becomes a testable property.

6. **[agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)** -- extends: prompt robustness findings are empirical evidence that semantic underspecification (not execution noise) is the deeper issue -- models break under paraphrase because the instruction interpretation space is fragile, not because of stochastic execution.

7. **[stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../notes/stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md)** -- grounds: the four reliability dimensions operationalise the "compound" (reliability/speed/cost) that stabilisation and distillation trade generality for.

8. **[storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md)** -- exemplifies: the consistency dimension quantifies exactly what output stabilisation prevents -- 50x cost swings and outcome variance on identical inputs.

## Extractable Value

1. **The four-dimension reliability decomposition as evaluation vocabulary.** Formal, operationalised definitions of consistency, robustness, predictability, and safety with computable metrics. Already integrated into the KB via the reliability-dimensions-map note, but the paper's metric definitions remain a reference for anyone building evaluation harnesses. [just-a-reference]

2. **Prompt robustness as the weakest link.** Models handle genuine infrastructure faults (API timeouts, malformed responses) but break under semantically equivalent instruction rephrasings. This is counterintuitive and actionable: invest in prompt robustness testing before worrying about fault tolerance. Already captured in softening-signals note. [just-a-reference]

3. **Larger models are less consistent because they have more solution strategies.** Run-to-run variability increases with capability because capable models have more valid interpretations of the same instruction. Directly extends the underspecification theory: a wider interpretation space means more variance when the LLM projects to a concrete execution. Implications for model selection when consistency matters. [experiment]

4. **Calibration improves but discrimination does not.** Models are getting better at aggregate confidence alignment (saying 80% and being right 80% of the time) but not at assigning higher confidence to correct answers than incorrect ones. This constrains the predictability oracle and limits confidence-based filtering. Not yet integrated into any KB note; the error-correction note could reference this as a ceiling on confidence-based amplification. [quick-win]

5. **Safety as hard constraint, not continuous trade-off.** The design choice to exclude safety from the aggregate score because averaging obscures tail risks is a transferable architectural principle. Safety violations are inherently tail phenomena that should be reported as gates, not gradients. Already captured in reliability-dimensions-map note. [just-a-reference]

6. **The augmentation/automation reliability threshold (Recommendation 4).** An agent that succeeds 90% but fails unpredictably is fine as augmentation (human catches failures) but unacceptable as automation (nobody catches them). This quantifies when human-in-the-loop shifts from optional to mandatory, based on predictability oracle strength. No dedicated KB note captures this distinction. [quick-win]

7. **Multi-run evaluation protocol as a methodology contribution.** K=5 runs with different seeds, J=5 prompt paraphrases, fault injection at p=0.2 -- a concrete recipe for reliability evaluation that goes beyond single-run benchmarking. Useful reference for anyone designing agent evaluation. [just-a-reference]

## Limitations (our opinion)

The paper tests relatively naive multi-agent coordination patterns. Several error correction strategies known in the literature — and discussed in this KB — were never tried:

- **No adversarial review** — no agents reviewing or critiquing other agents' outputs. Debate-style architectures and structured verification loops (generate-verify-revise) are absent from the tested topologies.
- **Simple majority voting only** — no weighted ensembles, consistency-based filtering, or confidence-calibrated aggregation.
- **No prompt perturbation for stability testing** — varying prompts in ways that shouldn't change the answer (a decorrelation strategy) to identify robust consensus patterns was not explored.
- **No deliberate decorrelation** — the [error-correction-works-above-chance-oracles](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) note argues that decorrelated checks are essential for effective error correction. The paper's topologies all use identical prompts and tools, maximizing correlated failure modes.

The headline finding (-3.5% mean MAS improvement) and the high error amplification ratios (up to 17.2x) may therefore reflect the limitations of naive multi-agent coordination rather than multi-agent coordination in general. The paper's own data hints at this: centralized verification already cuts error amplification to 4.4x — suggesting that more sophisticated verification (structured review, decorrelated checks) could push further.

This does not diminish the paper's contribution — the controlled methodology is unusually rigorous, and the finding that naive coordination usually hurts is valuable. But the paper should not be read as evidence that multi-agent coordination is inherently negative-sum.

## Recommended Next Action

Update `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`: add a paragraph in the "When can an oracle be amplified?" section noting that the discrimination finding from this paper (calibration improves but discrimination stagnates across 18 months of model releases) establishes a practical ceiling on confidence-based error correction. Even as models get better at aggregate calibration, their confidence scores remain poor at distinguishing individual correct from incorrect outputs -- meaning confidence-based voting hits a plateau unless discrimination specifically improves. This sharpens the note's existing TPR > FPR analysis with empirical evidence about the current state of model discrimination. Link to the source snapshot.
